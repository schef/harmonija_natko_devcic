#!/usr/bin/env python3
"""Non-destructive cleanup jobs and advisory triage for the book review viewer."""

import hashlib
import json
import re
import shutil
import subprocess
import threading
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def load_json(path, default):
    return json.loads(path.read_text()) if path.is_file() else default


def save_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    temporary.replace(path)


def fingerprint(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def review_reason(record):
    """Review manifests use several schemas; show actual findings, not just drafts."""
    reasons = []
    for key in ("independent_review_reason", "review_reason", "review_note", "source_condition_note"):
        value = record.get(key)
        if isinstance(value, str) and value.strip() and value.strip() not in reasons:
            reasons.append(value.strip())
    return "\n".join(reasons)


def triage(record):
    """Advisory tags only: never change independent review or certify cleanup."""
    if record.get("review_status") == "source_damage":
        return ["source_damage"]
    if record.get("review_status") == "independent_pass":
        return ["confirmation"]
    text = (review_reason(record) + " " + str(record.get("source_damage", ""))).lower()
    tags = []
    # Ignore negative statements commonly found in the review reports.
    positive = re.sub(r"\b(?:no|without)\s+(?:visible\s+)?(?:handwriting|pencil|annotation)[^.;]*", "", text)
    if re.search(r"handwrit|pencil|rukopis|olovk", positive):
        tags.append("handwriting")
    if re.search(r"overlap|layout|foreign|prose|punctuation|separat|adjacent|parenthes|neighbour|neighbor|interleav|preceding|following|vertical band|footer", text):
        tags.append("layout")
    if re.search(r"abrasion|damaged|uncertified|obscur|missing.*(?:note|notation)|worn", text):
        tags.append("notation_check")
    if record.get("kind") in {"notation", "glyph", "inline"} or "slika-38" in record.get("image", ""):
        tags.append("inline_glyph")
    return tags or ["other"]


class CleanupWorkflow:
    def __init__(self, root, launcher=None):
        self.root = Path(root).resolve()
        self.state_path = self.root / "review-candidates/book/cleanup-state.json"
        self.lock = threading.RLock()
        self.active = set()
        self.launcher = launcher or self.launch_gimp

    def inside(self, relative):
        if not isinstance(relative, str):
            raise ValueError("Expected a repository-relative path")
        path = (self.root / relative).resolve()
        if not path.is_relative_to(self.root):
            raise ValueError("Path must remain inside the repository")
        return path

    def state(self):
        with self.lock:
            return load_json(self.state_path, {})

    def relative(self, path):
        return path.relative_to(self.root).as_posix()

    def working_path(self, job):
        path = self.inside(job["working"])
        base = self.root / "review-candidates/manual-cleanup/book"
        if not path.is_relative_to(base) or path.name != "working.png":
            raise ValueError("Working copy must remain in its cleanup folder, not an original/source path")
        for original in (self.inside(job["original"]), self.inside(job["source_image"])):
            if path == original or (path.exists() and original.exists() and path.samefile(original)):
                raise ValueError("Working copy cannot be an original or source image")
        return path

    def prepare(self, record):
        with self.lock:
            state = self.state()
            if record["id"] in state:
                return state[record["id"]]
            source = self.inside(record["image"])
            if source.suffix.lower() != ".png" or not source.is_file():
                raise ValueError("The original crop must be an existing repository PNG")
            token = hashlib.sha256(record["id"].encode()).hexdigest()[:20]
            folder = self.inside(f"review-candidates/manual-cleanup/book/{token}")
            if folder.exists() and any(folder.iterdir()):
                raise ValueError("Cleanup folder already contains files without job metadata; inspect it manually")
            folder.mkdir(parents=True, exist_ok=True)
            working = folder / "working.png"
            # Never overwrite an orphaned working file, even without metadata.
            if working.exists():
                raise ValueError("Working copy already exists without job metadata; inspect it manually")
            shutil.copy2(source, working)
            job = {
                "id": record["id"], "status": "prepared", "created_at": now(),
                "original": record["image"], "original_sha256": fingerprint(source),
                "working": self.relative(working), "folder": self.relative(folder),
                "source_image": record["source_image"], "printed_page": record["printed_page"],
                "pdf_page": record["pdf_page"], "reason": review_reason(record),
                "original_rect": record.get("rect"),
                "history": [], "reviews": [],
            }
            (folder / "INSTRUCTIONS.md").write_text(
                f"# Cleanup: {record['id']}\n\nPrinted page {record['printed_page']}; PDF {record['pdf_page']}.\n\n"
                + review_reason(record) + "\n\n"
                "Original crop and source scan must remain unchanged. Edit working.png only.\n"
                "Save an XCF beside it if useful, but export the edited result to working.png.\n"
                "Close the dedicated GIMP instance when finished. A changed PNG is snapshotted\n"
                "for independent review; closing GIMP never approves or integrates it.\n"
                "Do not invent missing notation or erase uncertain musical marks.\n"
            )
            state[record["id"]] = job
            save_json(self.state_path, state)
            return job

    @staticmethod
    def launch_gimp(path):
        executable = shutil.which("gimp")
        if not executable:
            raise ValueError("GIMP is not installed; edit the prepared working.png manually")
        # A dedicated instance lets process exit mean this job's editor closed.
        return subprocess.Popen([executable, "--new-instance", str(path)],
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def start(self, record):
        with self.lock:
            if self.active or any(job["status"] in {"editing", "interrupted"} for job in self.state().values()):
                raise ValueError("A cleanup editor is open or its state is unknown; close it and queue its saved PNG first")
            job = self.prepare(record)
            state = self.state()
            job = state[record["id"]]
            working = self.working_path(job)
            if not working.is_file():
                raise ValueError("Working PNG is missing; restore it manually before opening")
            before = fingerprint(working)
            process = self.launcher(working)
            job["previous_status"] = job["status"]
            job["status"] = "editing"
            job["editor_started_at"] = now()
            job["editor_pid"] = process.pid
            job.pop("error", None)
            save_json(self.state_path, state)
            self.active.add(record["id"])
            threading.Thread(target=self._watch, args=(record["id"], process, before), daemon=True).start()
            return job

    def _watch(self, identity, process, before):
        try:
            code = process.wait()
            with self.lock:
                state = self.state()
                job = state[identity]
                job["editor_exit_code"] = code
                job["editor_closed_at"] = now()
                save_json(self.state_path, state)
            if code != 0:
                raise ValueError(f"GIMP exited with code {code}; saved changes were not queued automatically")
            self.queue_saved(identity, before)
        except Exception as error:
            with self.lock:
                state = self.state()
                if identity in state:
                    state[identity]["status"] = "editor_error"
                    state[identity]["error"] = str(error)
                    save_json(self.state_path, state)
        finally:
            with self.lock:
                self.active.discard(identity)

    def queue_saved(self, identity, before=None):
        """Snapshot a changed exported PNG; never approve it or update the book."""
        with self.lock:
            state = self.state()
            if identity not in state:
                raise ValueError("Prepare a working copy first")
            job = state[identity]
            working = self.working_path(job)
            original = self.inside(job["original"])
            if fingerprint(original) != job["original_sha256"]:
                raise ValueError("Original crop changed outside this workflow; inspect provenance before continuing")
            with Image.open(working) as image:
                image.load()
                if image.format != "PNG":
                    raise ValueError("Export an actual PNG to working.png")
                size = list(image.size)
            digest = fingerprint(working)
            baseline = before or job.get("candidate_sha256", job["original_sha256"])
            if digest == baseline:
                job["status"] = job.get("previous_status", "unchanged") if before else job["status"]
                if job["status"] in {"editing", "interrupted", "editor_error"}:
                    job["status"] = job.get("previous_status", "prepared")
                job.pop("error", None)
                job["last_result"] = "No changed exported PNG; no new review queued"
                save_json(self.state_path, state)
                return job
            folder = self.inside(job["folder"])
            revision = len(job["history"]) + 1
            candidate = folder / f"candidate-{revision:03}-{digest[:12]}.png"
            if candidate.exists():
                raise ValueError("Snapshot already exists; no file was overwritten")
            shutil.copy2(working, candidate)
            job.update(status="pending_independent_review", candidate=self.relative(candidate),
                       candidate_sha256=digest, candidate_size=size, queued_at=now())
            job.pop("error", None)
            job["last_result"] = "Changed PNG snapshotted; independent review required, not approved"
            job["history"].append({"candidate": job["candidate"], "sha256": digest, "queued_at": job["queued_at"]})
            save_json(self.state_path, state)
            self.write_review_bundle(state)
            return job

    def write_review_bundle(self, state):
        lines = ["# Cleaned copies awaiting independent visual review", "",
                 "These edited copies are NOT source-pixel-equal and are NOT approved.",
                 "Compare each with both original crop and authoritative source page; inspect all four edges,",
                 "every notation mark and removed ink. Do not integrate merely because GIMP closed.", ""]
        records = []
        for identity, job in sorted(state.items()):
            if job["status"] != "pending_independent_review":
                continue
            lines.extend([f"## {identity}", "", f"- Candidate: `{job['candidate']}`",
                          f"- SHA-256: `{job['candidate_sha256']}`", f"- Original: `{job['original']}`",
                          f"- Source: `{job['source_image']}`",
                          f"- Printed/PDF page: {job['printed_page']} / {job['pdf_page']}",
                          f"- Original finding: {job['reason']}", ""])
            records.append({
                "id": identity, "image": job["candidate"], "sha256": job["candidate_sha256"],
                "original": job["original"], "original_sha256": job["original_sha256"],
                "source_image": job["source_image"], "original_rect": job.get("original_rect"),
                "printed_page": job["printed_page"], "pdf_page": job["pdf_page"],
                "review_status": "pending_independent_review", "approved": False,
                "source_pixel_equality_expected": False, "review_reason": job["reason"],
            })
        (self.root / "review-candidates/book/CLEANUP-REVIEW-READY.md").write_text("\n".join(lines) + "\n")
        save_json(self.root / "review-candidates/book/cleanup-review-queue.json", {
            "warning": "Edited snapshots require independent visual review; never approve by process exit or source-pixel equality.",
            "records": records,
        })

    def recover(self):
        """After a server restart, never infer that a previously opened editor closed."""
        with self.lock:
            state = self.state()
            changed = False
            for job in state.values():
                if job["status"] == "editing":
                    job["status"] = "interrupted"
                    job["error"] = "Viewer restarted; editor state is unknown. Close GIMP, export working.png, then queue saved copy manually."
                    changed = True
            if changed:
                save_json(self.state_path, state)
