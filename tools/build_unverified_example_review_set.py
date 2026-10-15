#!/usr/bin/env python3
"""Create provisional score-review records and source-only candidate crops.

OCR is performed by Tesseract on rendered `sources/pages/*.png` pixels only.
The source PDF is never opened for text extraction, and OCR-derived labels are
explicitly tentative. This tool does not add entries to the verified catalog.
"""

import json
import os
import re
import subprocess
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "tools" / "score-region-candidates.json"
OUTPUT = ROOT / "tools" / "unverified-musical-examples.json"
REVIEW_MARKDOWN = ROOT / "tools" / "unverified-musical-examples.md"
OCR_OUTPUT = ROOT / "tools" / "source-page-ocr-labels.json"
CROPS = ROOT / "review-candidates"
LABEL_RE = re.compile(r"^(?:primjer|pr\.?\s*)?(\d+)\s*[.,]\s*(\d+)\.?\s*$", re.IGNORECASE)


def api_ocr_tsv(source):
    environment = os.environ | {"OMP_THREAD_LIMIT": "1"}
    result = subprocess.run(["tesseract", str(source), "stdout", "-l", "hrv+eng", "--psm", "11", "tsv"], check=True, text=True, capture_output=True, env=environment)
    return result.stdout


def ocr_labels(source):
    lines = defaultdict(list)
    for row in api_ocr_tsv(source).splitlines()[1:]:
        fields = row.split("\t")
        if len(fields) != 12 or fields[0] != "5" or not fields[11].strip():
            continue
        lines[tuple(fields[:5])].append({"left": int(fields[6]), "top": int(fields[7]), "width": int(fields[8]), "height": int(fields[9]), "text": fields[11].strip()})
    labels = []
    for words in lines.values():
        normalized = re.sub(r"\s+", " ", " ".join(word["text"] for word in words)).strip()
        match = LABEL_RE.fullmatch(normalized)
        if not match:
            continue
        left = min(word["left"] for word in words)
        top = min(word["top"] for word in words)
        right = max(word["left"] + word["width"] for word in words)
        bottom = max(word["top"] + word["height"] for word in words)
        labels.append({"text": f"{int(match.group(1))}.{int(match.group(2))}", "rect": [left, top, right, bottom], "ocr_text": normalized})
    return labels


def point_rect_distance(x, y, rectangle):
    left, top, right, bottom = rectangle
    horizontal = max(left - x, 0, x - right)
    vertical = max(top - y, 0, y - bottom)
    return horizontal * horizontal + vertical * vertical


def nearby_labels(candidate, labels):
    left, top, right, bottom = candidate["rect"]
    centre_x = (left + right) // 2
    centre_y = (top + bottom) // 2
    nearby = []
    for label in labels:
        label_left, label_top, label_right, label_bottom = label["rect"]
        if label_bottom < top - 160 or label_top > bottom + 240:
            continue
        nearby.append((point_rect_distance(centre_x, centre_y, label["rect"]), label))
    return sorted(nearby, key=lambda item: item[0])


def write_crop(candidate):
    target = CROPS / f"{candidate['id']}.png"
    source = ROOT / candidate["source_image"]
    with Image.open(source) as image:
        left, top, right, bottom = candidate["rect"]
        assert 0 <= left < right <= image.width and 0 <= top < bottom <= image.height, candidate
        image.crop((left, top, right, bottom)).save(target)
    return target.relative_to(ROOT).as_posix()


def review_markdown(records):
    lines = [
        "# Provisional musical-example review queue",
        "",
        "These are automatically detected score regions, not verified musical examples. Every name, boundary, and crop must be checked against the rendered source page before it is accepted. OCR was run only on source-page PNG pixels, never on PDF embedded text.",
        "",
        "Coordinates are `[left, top, right, bottom]` in local 300 dpi source-page pixels.",
        "",
        "| Candidate | Tentative name | Printed page | Source location | Provisional crop |",
        "| --- | --- | ---: | --- | --- |",
    ]
    for record in records:
        location = f"`{record['source_page']}` `{record['approximate_rect']}`"
        image = Path(record["provisional_crop"]).name
        lines.append(f"| `{record['candidate_id']}` | {record['name']} | {record['original_printed_page']} | {location} | [{image}](../{record['provisional_crop']}) |")
    return "\n".join(lines) + "\n"


def main():
    manifest = json.loads(CANDIDATES.read_text())
    candidates = manifest["candidates"]
    CROPS.mkdir(exist_ok=True)
    sources = sorted({candidate["source_image"] for candidate in candidates})
    cached = json.loads(OCR_OUTPUT.read_text())["labels_by_source_image"] if OCR_OUTPUT.is_file() else {}
    missing = [source_name for source_name in sources if source_name not in cached]
    for source_name in sources:
        assert (ROOT / source_name).is_file(), source_name
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(ocr_labels, ROOT / source_name): source_name for source_name in missing}
        for number, future in enumerate(as_completed(futures), 1):
            source_name = futures[future]
            cached[source_name] = future.result()
            OCR_OUTPUT.write_text(
                json.dumps({"version": 1, "method": "Tesseract hrv+eng --psm 11 applied only to rendered source-page PNG pixels; no PDF text extraction was used.", "labels_by_source_image": cached}, ensure_ascii=False, indent=2) + "\n"
            )
            print(f"OCR {number}/{len(missing)}: {source_name}", flush=True)
    labels_by_source = {source_name: cached[source_name] for source_name in sources}
    OCR_OUTPUT.write_text(
        json.dumps({"version": 1, "method": "Tesseract hrv+eng --psm 11 applied only to rendered source-page PNG pixels; no PDF text extraction was used.", "labels_by_source_image": labels_by_source}, ensure_ascii=False, indent=2) + "\n"
    )
    records = []
    for number, candidate in enumerate(candidates, 1):
        labels = nearby_labels(candidate, labels_by_source[candidate["source_image"]])
        tentative_label = labels[0][1]["text"] if labels else None
        name = f"Primjer {tentative_label} (OCR, unverified)" if tentative_label else f"Unverified score candidate {candidate['id']}"
        records.append(
            {
                "name": name,
                "tentative_printed_example": tentative_label,
                "candidate_id": candidate["id"],
                "original_printed_page": candidate["printed_page"],
                "original_pdf_spread": candidate["pdf_page"],
                "source_page": candidate["source_page"],
                "source_image": candidate["source_image"],
                "approximate_rect": candidate["rect"],
                "provisional_crop": write_crop(candidate),
                "nearby_ocr_labels": [label["text"] for _, label in labels[:5]],
                "status": "unverified",
                "review_note": "Detector rectangle and any OCR-derived name are provisional. Verify the scan, example identity, boundaries, labels, and crop before adding it to the verified catalog.",
            }
        )
        print(f"Crop {number}/{len(candidates)}: {candidate['id']}", flush=True)
    OUTPUT.write_text(
        json.dumps(
            {
                "version": 1,
                "warning": "This is a provisional review queue, not a list of verified examples. It may contain duplicate fragments, merged examples, false positives, and OCR label errors.",
                "ocr_policy": "Tesseract was run only on rendered source-page PNG pixels. No embedded or extracted PDF OCR/text was used.",
                "coordinate_system": "[left, top, right, bottom] local 300 dpi source-page pixels.",
                "records": records,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n"
    )
    REVIEW_MARKDOWN.write_text(review_markdown(records))
    labelled = sum(record["tentative_printed_example"] is not None for record in records)
    print(f"Wrote {len(records)} provisional review records, crops, and review-table rows; {labelled} received an OCR-derived tentative example label.")


if __name__ == "__main__":
    main()
