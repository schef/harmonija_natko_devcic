#!/usr/bin/env python3
"""Serve the book review workspace locally; never alter originals or approvals."""

import argparse
import json
import re
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit

from PIL import Image

from book_review_workflow import CleanupWorkflow, load_json, now, review_reason, save_json, triage


ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "review-candidates/book/review-queue.json"
STATE = ROOT / "review-candidates/book/human-review-state.json"
DECISIONS = {"accept", "recrop", "cleanup", "reject"}
ASSETS = Path(__file__).resolve().parent / "review_book_assets"

HTML = """<!doctype html><html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Harmonija — image review workspace</title><link rel="stylesheet" href="/assets/review.css">
<header><h1>Harmonija — image review</h1><div id="progress" role="status"></div>
<div class="toolbar"><button id="prev">← Previous</button><button id="next">Next / skip →</button>
<button data-choice="accept" id="accept">Accept [A]</button><button data-choice="cleanup">Cleanup [C]</button>
<button data-choice="recrop">Recrop [R]</button><button data-choice="reject">Reject [X]</button>
<button id="undo">Undo last decision [U]</button></div>
<div class="toolbar"><label>View <select id="status-filter">
<option value="independent_pass">Passed — confirm</option><option value="cleanup_required">Cleanup / layout holds</option>
<option value="source_damage">Source damage — notation decision</option><option value="ready">Edited copies awaiting review</option>
<option value="pending_independent_review">Original review pending</option><option value="all">All images</option></select></label>
<label>Chapter <select id="chapter-filter"><option value="all">All chapters</option></select></label>
<label>Issue <select id="issue-filter"><option value="all">All issue types</option>
<option value="handwriting">Handwriting</option><option value="layout">Layout / adjacent ink</option>
<option value="notation_check">Notation needs judgment</option><option value="inline_glyph">Inline glyph</option>
<option value="other">Other / unclassified</option></select></label>
<label>Sort <select id="sort"><option value="source">Source order</option><option value="triage">Suggested triage order</option></select></label>
<label>Page <input id="page-filter" type="number" min="1" max="411" placeholder="Any"></label>
<label><input type="checkbox" id="pending" checked>Undecided only</label>
<label><input type="checkbox" id="full">Native size [F]</label></div>
<div class="toolbar"><label><input type="checkbox" id="highlight" checked>Highlight crop on source</label><button id="focus-source">Focus source region</button></div>
<div class="toolbar"><label>Find <input id="search" placeholder="Example, ID or finding"></label>
<label>Note <input id="note" placeholder="Optional decision note"></label><span id="saved"></span></div>
<div id="error" role="alert"></div></header>
<main><section class="summary"><h2 id="crop-title">Loading…</h2><div id="message"></div>
<p id="safety">Issue tags are suggestions, not new review decisions. Do not invent missing notation.</p>
<div class="toolbar"><button id="prepare">Prepare working copy</button><button id="gimp">Open working copy in GIMP [G]</button>
<button id="queue-saved">Queue saved PNG for review</button><button id="refresh">Refresh jobs</button>
<a id="chapter-link" href="#context">Chapter context ↓</a></div><div id="job" role="status"></div></section>
<div class="panes"><section class="pane"><h3 id="candidate-title">Prepared crop</h3><a id="crop-link" target="_blank" rel="noopener"><img id="crop" alt="Prepared or edited crop"></a>
<details id="original-details"><summary>Original crop (compare with edited candidate)</summary><img id="original" alt="Unmodified original crop"></details></section>
<section class="pane" id="source-pane"><h3 id="source-title">Original source page</h3><div id="source-stage"><a id="source-link" target="_blank" rel="noopener"><img id="source" alt="Authoritative source scan"></a><div id="source-rect" aria-hidden="true"></div></div></section></div>
<section id="context"><h2>Chapter context</h2><p id="context-label"></p><pre id="context-text"></pre></section>
<details><summary>How to use this workspace</summary><p>A accept · C cleanup · R recrop · X reject · U undo · G GIMP · F native size · ←/→ previous/skip.
Shortcuts are disabled while typing. Acceptance is available only for independently passing originals.
Edited copies require a separate independent review and are never automatically approved.</p>
<p>For cleanup, export to the displayed working.png, optionally save an XCF beside it, then close the dedicated GIMP instance.
Changed exports are snapshotted automatically. If the viewer restarted or you used another editor, close the editor and use Queue saved PNG.
Progress and filters resume in this browser; human decisions and cleanup jobs are saved separately on disk.</p>
<p>Tags and triage order are advisory. Source damage is not a handwriting-removal task. Review the source before removing any uncertain mark.</p></details>
</main><script src="/assets/review.js" defer></script></html>"""


def safe_image(relative, root=ROOT):
    root = Path(root).resolve()
    path = (root / relative).resolve()
    if not path.is_relative_to(root) or path.suffix.lower() != ".png":
        raise ValueError("Only repository PNG files may be viewed")
    if not path.is_file():
        raise ValueError("Image not found")
    return path


def validate_decision(payload, records):
    if not isinstance(payload, dict):
        raise ValueError("Expected a JSON object")
    row = next((row for row in records if row["id"] == payload.get("id")), None)
    if row is None:
        raise ValueError("Unknown queue image")
    if payload.get("decision") not in DECISIONS:
        raise ValueError("Unknown decision")
    if payload["decision"] == "accept" and row.get("review_status") != "independent_pass":
        raise ValueError("This original has not independently passed. Cleanup and source-damage holds cannot be accepted here.")
    if not isinstance(payload.get("note", ""), str) or len(payload.get("note", "")) > 10000:
        raise ValueError("Note must be text, at most 10,000 characters")
    return {"decision": payload["decision"], "note": payload.get("note", "")}


class ReviewApp:
    def __init__(self, root=ROOT, launcher=None):
        self.root = Path(root).resolve()
        self.queue_path = self.root / "review-candidates/book/review-queue.json"
        self.state_path = self.root / "review-candidates/book/human-review-state.json"
        self.history_path = self.root / "review-candidates/book/human-review-history.json"
        self.workflow = CleanupWorkflow(self.root, launcher)
        self.workflow.recover()

    def records(self):
        return load_json(self.queue_path, {"records": []})["records"]

    def record(self, identity):
        row = next((r for r in self.records() if r["id"] == identity), None)
        if row is None:
            raise ValueError("Unknown queue image")
        return row

    def decide(self, payload):
        decision = validate_decision(payload, self.records())
        if decision["decision"] == "accept":
            record = self.record(payload["id"])
            # The independent pass belongs to the reviewed source-only original,
            # not a file replaced externally since that review.
            with Image.open(safe_image(record["image"], self.root)) as crop, Image.open(safe_image(record["source_image"], self.root)) as source:
                expected = source.crop(record["rect"])
                if (crop.mode, crop.size, crop.tobytes()) != (expected.mode, expected.size, expected.tobytes()):
                    raise ValueError("This original no longer matches its reviewed source rectangle. Queue an edited copy for independent review instead.")
        with self.workflow.lock:
            state = load_json(self.state_path, {})
            previous = state.get(payload["id"])
            event = {"id": payload["id"], "previous": previous, "new": decision, "at": now()}
            history = load_json(self.history_path, [])
            # Persist the journal before state; undo checks the current value.
            history.append(event)
            save_json(self.history_path, history)
            state[payload["id"]] = decision
            save_json(self.state_path, state)
            return state

    def undo(self):
        with self.workflow.lock:
            history = load_json(self.history_path, [])
            state = load_json(self.state_path, {})
            event = next((e for e in reversed(history) if not e.get("undone_at")), None)
            if event is None:
                raise ValueError("No decision from this workspace is available to undo")
            if state.get(event["id"]) != event["new"]:
                raise ValueError("Decision changed outside this workspace; no state was overwritten")
            if event["previous"] is None:
                state.pop(event["id"], None)
            else:
                state[event["id"]] = event["previous"]
            event["undone_at"] = now()
            save_json(self.state_path, state)
            save_json(self.history_path, history)
            return {"state": state, "id": event["id"]}

    def context(self, identity):
        row = self.record(identity)
        chapter = row.get("integration_output") or row.get("chapter") or row.get("chapter_path")
        if not chapter:
            return {"chapter": None, "text": "Chapter context is not recorded for this image."}
        path = (self.root / chapter).resolve()
        if not path.is_relative_to(self.root / "chapters") or path.suffix != ".md":
            raise ValueError("Invalid chapter path")
        text = path.read_text()
        markers = list(re.finditer(r"<!--\s*source-page:\s*(\d+);\s*pdf-page:\s*\d+\s*-->", text))
        for number, marker in enumerate(markers):
            if int(marker[1]) == row["printed_page"]:
                end = markers[number + 1].start() if number + 1 < len(markers) else len(text)
                section = text[marker.start():end]
                # End-of-chapter generated footnotes can be very long: keep context focused.
                return {"chapter": chapter, "text": section[:24000], "truncated": len(section) > 24000}
        return {"chapter": chapter, "text": "No source-page marker found; inspect the chapter file."}


class ReviewHandler(BaseHTTPRequestHandler):
    @property
    def app(self):
        return self.server.app

    def send(self, status, body, content_type="application/json"):
        data = body if isinstance(body, bytes) else body.encode()
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", "default-src 'self'; img-src 'self'; style-src 'self'; script-src 'self'; frame-ancestors 'none'")
        try:
            self.end_headers()
            self.wfile.write(data)
        except (BrokenPipeError, ConnectionResetError):
            # Switching images can cancel an in-flight browser request.
            pass

    def local_request(self, write=False):
        hosts = {f"127.0.0.1:{self.server.server_port}", f"localhost:{self.server.server_port}"}
        host = self.headers.get("Host")
        if host not in hosts:
            raise ValueError("Only this loopback server's Host is allowed")
        origin = self.headers.get("Origin")
        if origin and origin != f"http://{host}":
            raise ValueError("Cross-origin access is disabled")
        if self.headers.get("Sec-Fetch-Site") == "cross-site":
            raise ValueError("Cross-site access is disabled")
        if write and self.headers.get("Content-Type", "").split(";")[0] != "application/json":
            raise ValueError("Writes require application/json")

    def do_GET(self):
        try:
            self.local_request()
        except ValueError as error:
            self.send(403, str(error), "text/plain")
            return
        parsed = urlsplit(self.path)
        route = unquote(parsed.path)
        try:
            if route == "/":
                self.send(200, HTML, "text/html; charset=utf-8")
            elif route in {"/assets/review.js", "/assets/review.css"}:
                asset = ASSETS / route.rsplit("/", 1)[1]
                self.send(200, asset.read_bytes(), "text/javascript" if asset.suffix == ".js" else "text/css")
            elif route == "/api/queue":
                records = [{**r, "triage_tags": triage(r), "review_note": review_reason(r)} for r in self.app.records()]
                self.send(200, json.dumps({"records": records}))
            elif route == "/api/state":
                self.send(200, json.dumps(load_json(self.app.state_path, {})))
            elif route == "/api/jobs":
                self.send(200, json.dumps(self.app.workflow.state()))
            elif route == "/api/context":
                identity = parse_qs(parsed.query).get("id", [None])[0]
                self.send(200, json.dumps(self.app.context(identity)))
            elif route.startswith("/file/"):
                relative = route[6:]
                allowed = {r[key] for r in self.app.records() for key in ("image", "source_image")}
                for job in self.app.workflow.state().values():
                    allowed.add(job["working"])
                    allowed.update(r["candidate"] for r in job.get("history", []))
                if relative not in allowed:
                    raise ValueError("Only queued images and recorded cleanup copies may be viewed")
                self.send(200, safe_image(relative, self.app.root).read_bytes(), "image/png")
            else:
                self.send(404, "Not found", "text/plain")
        except (ValueError, KeyError, OSError) as error:
            self.send(400, str(error), "text/plain")

    def do_POST(self):
        try:
            self.local_request(write=True)
        except ValueError as error:
            self.send(403, str(error), "text/plain")
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= 65536:
                raise ValueError("Invalid request size")
            payload = json.loads(self.rfile.read(length))
            if not isinstance(payload, dict):
                raise ValueError("Expected a JSON object")
            if self.path == "/api/decision":
                result = self.app.decide(payload)
            elif self.path == "/api/undo":
                result = self.app.undo()
            elif self.path in {"/api/cleanup/prepare", "/api/cleanup/open", "/api/cleanup/queue"}:
                record = self.app.record(payload.get("id"))
                workflow = self.app.workflow
                if self.path.endswith("/prepare"):
                    result = workflow.prepare(record)
                elif self.path.endswith("/open"):
                    result = workflow.start(record)
                else:
                    if record["id"] in workflow.active:
                        raise ValueError("Close the dedicated GIMP instance before queueing its export")
                    result = workflow.queue_saved(record["id"])
            else:
                self.send(404, "Not found", "text/plain")
                return
            self.send(200, json.dumps(result))
        except (ValueError, KeyError, OSError) as error:
            self.send(400, str(error), "text/plain")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    if not QUEUE.is_file():
        parser.error("No consolidated queue yet: review-candidates/book/review-queue.json")
    server = HTTPServer(("127.0.0.1", args.port), ReviewHandler)
    server.app = ReviewApp()
    print(f"Open http://127.0.0.1:{server.server_port} — decisions save to {STATE.relative_to(ROOT)}", flush=True)
    print("Original images and independent-review metadata are never modified. GIMP edits queue for review only.", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
