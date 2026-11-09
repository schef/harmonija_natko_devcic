#!/usr/bin/env python3
"""Generate reviewer-specified source-only recrops without replacing originals."""

import argparse
import json
import re
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]


def load_records(path):
    data = json.loads(path.read_text())
    if isinstance(data, list):
        return data
    for key in ("records", "reviews", "images"):
        if key in data:
            return data[key]
    raise ValueError(f"No record list found in {path}")


def apply(milestone, batch=None):
    folder = ROOT / "review-candidates/book" / milestone
    if batch is not None and not re.fullmatch(r"\d{3}-\d{3}", batch):
        raise ValueError("Batch must look like 101-118")
    suffix = f"-{batch}" if batch else ""
    records = load_records(folder / f"images{suffix}.json")
    reviews = {row["id"]: row for row in load_records(folder / f"visual-review{suffix}.json")}
    source_pages = {
        page["image"]: page
        for page in json.loads((ROOT / "sources/index.json").read_text())["pages"]
    }
    corrected = []
    for original in records:
        row = dict(original)
        source_page = source_pages[row["source_image"]]
        if source_page["printed_page"] != row["printed_page"]:
            raise ValueError(f"Printed page disagrees with source index: {row['id']}")
        if row["pdf_page"] != source_page["pdf_page"]:
            row["original_pdf_page"] = row["pdf_page"]
            row["pdf_page"] = source_page["pdf_page"]
        review = reviews[row["id"]]
        row["review_note"] = review["reason"]
        if review.get("proposed_rect"):
            rect = review["proposed_rect"]
            source = ROOT / row["source_image"]
            target = ROOT / Path(row["image"]).parent / "recrops" / Path(row["image"]).name
            with Image.open(source) as image:
                left, top, right, bottom = rect
                if not (0 <= left < right <= image.width and 0 <= top < bottom <= image.height):
                    raise ValueError(f"Invalid rectangle for {row['id']}: {rect}")
                crop = image.crop(rect)
                target.parent.mkdir(parents=True, exist_ok=True)
                if target.exists():
                    with Image.open(target) as existing:
                        if existing.mode != crop.mode or existing.size != crop.size or existing.tobytes() != crop.tobytes():
                            raise ValueError(f"Existing recrop differs; refusing overwrite: {target}")
                else:
                    crop.save(target)
            row["original_image"] = row["image"]
            row["original_rect"] = row["rect"]
            row["image"] = target.relative_to(ROOT).as_posix()
            row["rect"] = rect
            row["review_status"] = "pending_recrop_review"
        elif review["decision"] == "PASS":
            row["review_status"] = "independent_pass"
        else:
            row["review_status"] = "source_limited" if review.get("source_limited") else "recrop_required"
        corrected.append(row)
    output = folder / f"images-corrected{suffix}.json"
    output.write_text(json.dumps(corrected, ensure_ascii=False, indent=2) + "\n")
    print(f"Prepared {sum(row['review_status'] == 'pending_recrop_review' for row in corrected)} recrops; originals unchanged.")
    return corrected


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("milestone", choices=[f"M{number:02}" for number in range(2, 12)])
    parser.add_argument("--batch", help="Optional printed-page shard, for example 101-118")
    args = parser.parse_args()
    apply(args.milestone, args.batch)


if __name__ == "__main__":
    main()
