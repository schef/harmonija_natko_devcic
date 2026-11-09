#!/usr/bin/env python3
"""Consolidate milestone hand-offs; independent passes are not human acceptance."""

import argparse
import collections
import json
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "review-candidates/book"


def load_records(path):
    data = json.loads(path.read_text())
    if isinstance(data, list):
        return data
    return data.get("records", data.get("images", []))


def repository_image(relative):
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT) or path.suffix.lower() != ".png" or not path.is_file():
        raise ValueError(f"Invalid repository PNG: {relative}")
    return path


def build(milestones):
    queue = []
    coverage = []
    for milestone in milestones:
        folder = BOOK / milestone
        candidates = [folder / name for name in ("images-integrated.json", "images-corrected.json", "images.json")]
        manifest = next((path for path in candidates if path.is_file()), None)
        if manifest is None:
            coverage.append({"milestone": milestone, "status": "no_image_manifest", "images": 0})
            continue
        records = load_records(manifest)
        for item in records:
            row = dict(item)
            row["local_id"] = row["id"]
            row["id"] = f"{milestone}:{row['id']}"
            row["milestone"] = milestone
            row["manifest"] = manifest.relative_to(ROOT).as_posix()
            row["human_review_status"] = "undecided"
            status = row.get("review_status", "pending_independent_review")
            aliases = {"pass": "independent_pass", "PASS": "independent_pass", "cleanup required": "cleanup_required"}
            if status in aliases:
                row["original_review_status"] = status
                row["review_status"] = aliases[status]
            crop_path = repository_image(row["image"])
            source_path = repository_image(row["source_image"])
            with Image.open(crop_path) as crop, Image.open(source_path) as source:
                rect = row["rect"]
                left, top, right, bottom = rect
                if not (0 <= left < right <= source.width and 0 <= top < bottom <= source.height):
                    raise ValueError(f"Source rectangle out of bounds: {row['id']}")
                if crop.size != (right - left, bottom - top):
                    raise ValueError(f"Crop size disagrees with rectangle: {row['id']}")
            queue.append(row)
        coverage.append({"milestone": milestone, "status": "prepared", "images": len(records)})
    queue.sort(key=lambda row: (row["printed_page"], row["rect"][1], row["rect"][0], row["id"]))
    if len({row["id"] for row in queue}) != len(queue):
        raise ValueError("Duplicate queue identifiers")
    BOOK.mkdir(parents=True, exist_ok=True)
    output = BOOK / "review-queue.json"
    output.write_text(json.dumps({
        "warning": "Preparation queue, not human approval. Read independent-review status and unresolved notes before accepting.",
        "coverage": coverage,
        "records": queue,
    }, ensure_ascii=False, indent=2) + "\n")
    lines = ["# Whole-book image confirmation queue", "",
             "This queue is not a claim of whole-book completion or human approval.", "",
             "Run `python tools/review_book.py` and open the printed local URL.", "",
             "Decisions are saved separately in `review-candidates/book/human-review-state.json`.", "",
             "| ID | Printed page | Independent review | Crop | Source |",
             "| --- | ---: | --- | --- | --- |"]
    for row in queue:
        lines.append(f"| {row['id']} | {row['printed_page']} | {row.get('review_status', 'pending')} | "
                     f"[crop](../../{row['image']}) | [source](../../{row['source_image']}) |")
    # This Markdown is inside review-candidates/book: two parent traversals reach root.
    (BOOK / "REVIEW-QUEUE.md").write_text("\n".join(lines) + "\n")
    counts = collections.Counter(row.get("review_status", "pending") for row in queue)
    print(f"Built {len(queue)} image records; statuses: {dict(counts)}")
    return queue


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--milestone", action="append", choices=[f"M{n:02}" for n in range(2, 12)])
    args = parser.parse_args()
    build(args.milestone or [f"M{n:02}" for n in range(2, 12)])


if __name__ == "__main__":
    main()
