#!/usr/bin/env python3
"""Prepare explicitly unverified OCR drafts from rendered source pixels only."""

import argparse
import concurrent.futures
import json
import os
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def transcribe(page):
    destination = ROOT / "review-candidates/book/ocr" / page["source_page"]
    destination.parent.mkdir(parents=True, exist_ok=True)
    text = destination.with_suffix(".txt")
    boxes = destination.with_suffix(".tsv")
    if not (text.is_file() and boxes.is_file()):
        result = subprocess.run(
            ["tesseract", str(ROOT / page["image"]), str(destination),
             "-l", "hrv", "--psm", "3", "txt", "tsv"],
            capture_output=True, text=True,
            env={**os.environ, "OMP_THREAD_LIMIT": "1"},
        )
        if result.returncode:
            return {"printed_page": page["printed_page"], "status": "failed", "error": result.stderr}
    return {
        "printed_page": page["printed_page"],
        "pdf_page": page["pdf_page"],
        "source_image": page["image"],
        "text": text.relative_to(ROOT).as_posix(),
        "word_boxes": boxes.relative_to(ROOT).as_posix(),
        "status": "ocr_draft_not_visually_verified",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--first", type=int, default=47)
    parser.add_argument("--last", type=int, default=411)
    parser.add_argument("--workers", type=int, default=2)
    args = parser.parse_args()
    pages = json.loads((ROOT / "sources/index.json").read_text())["pages"]
    pages = [page for page in pages if page["printed_page"] is not None
             and args.first <= page["printed_page"] <= args.last]
    records = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(transcribe, page) for page in pages]
        for future in concurrent.futures.as_completed(futures):
            record = future.result()
            records.append(record)
            print(f"{len(records)}/{len(pages)}: page {record['printed_page']} {record['status']}", flush=True)
    output = ROOT / "review-candidates/book/ocr/index.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({
        "warning": "OCR DRAFTS ONLY. Every paragraph must be compared with the scan before chapter integration.",
        "ocr_policy": "Tesseract hrv on existing rendered PNG pixels; no PDF text extraction.",
        "records": sorted(records, key=lambda row: row["printed_page"]),
    }, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
