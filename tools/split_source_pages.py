#!/usr/bin/env python3
"""Render the source PDF into lossless, single-printed-page PNG files.

The source pages are never resized, enhanced, deskewed, or otherwise altered.
Each two-page PDF render is split only at its exact pixel midpoint. Existing
crop manifests are migrated from spread coordinates to local source-page
coordinates without changing the extracted score images themselves.
"""

import argparse
import json
import subprocess
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
PDF = next(ROOT.glob("*.pdf"))
SOURCES = ROOT / "sources"
PAGES = SOURCES / "pages"
INDEX = SOURCES / "index.json"
TEMP = Path("/tmp/opencode/harmonija-source-pages")
CROP_LOCATIONS = ROOT / "tools" / "crop-locations.json"
CANDIDATES = ROOT / "tools" / "score-region-candidates.json"
DPI = 300
PDF_PAGE_COUNT = 206


def page_name(printed_page):
    return "front-001" if printed_page == 0 else f"page-{printed_page:03d}"


def api_render_spread(pdf_page, rerender):
    TEMP.mkdir(parents=True, exist_ok=True)
    path = TEMP / f"pdf-page-{pdf_page:03d}-{DPI}dpi.png"
    if rerender or not path.is_file():
        subprocess.run(["pdftoppm", "-f", str(pdf_page), "-l", str(pdf_page), "-r", str(DPI), "-png", "-singlefile", str(PDF), str(path.with_suffix(""))], check=True)
    return path


def source_records(rerender):
    PAGES.mkdir(parents=True, exist_ok=True)
    records = []
    for pdf_page in range(1, PDF_PAGE_COUNT + 1):
        spread_path = api_render_spread(pdf_page, rerender)
        with Image.open(spread_path) as spread:
            width, height = spread.size
            midpoint = width // 2
            for side, left, right, printed_page in (("left", 0, midpoint, pdf_page * 2 - 2), ("right", midpoint, width, pdf_page * 2 - 1)):
                name = page_name(printed_page)
                relative_path = Path("sources") / "pages" / f"{name}.png"
                target = ROOT / relative_path
                if rerender or not target.is_file():
                    spread.crop((left, 0, right, height)).save(target)
                records.append(
                    {
                        "source_page": name,
                        "printed_page": printed_page if printed_page else None,
                        "pdf_page": pdf_page,
                        "side": side,
                        "image": relative_path.as_posix(),
                        "spread_rect": [left, 0, right, height],
                        "size": [right - left, height],
                    }
                )
        print(f"Rendered and split PDF spread {pdf_page:03d}", flush=True)
    return records


def write_index(records):
    index = {
        "version": 1,
        "source_pdf": PDF.name,
        "dpi": DPI,
        "warning": "Each PNG is a direct, lossless half of the 300 dpi rendered PDF spread. No resampling, deskewing, cleaning, or artificial border has been applied.",
        "pages": records,
    }
    INDEX.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n")


def record_map(records):
    return {(record["pdf_page"], record["side"]): record for record in records}


def local_location(rectangle, pdf_page, records):
    left, top, right, bottom = rectangle
    midpoint = records[(pdf_page, "right")]["spread_rect"][0]
    if right <= midpoint:
        record = records[(pdf_page, "left")]
        return bounded_location(record, [left, top, right, bottom])
    if left >= midpoint:
        record = records[(pdf_page, "right")]
        return bounded_location(record, [left - midpoint, top, right - midpoint, bottom])
    return {
        "source_pages": [records[(pdf_page, "left")]["source_page"], records[(pdf_page, "right")]["source_page"]],
        "rect_on_spread": rectangle,
        "status_note": "This location crosses the source-page seam and remains in spread coordinates until manually resolved.",
    }


def bounded_location(record, rectangle):
    left, top, right, bottom = rectangle
    width, height = record["size"]
    bounded = [max(0, left), max(0, top), min(width, right), min(height, bottom)]
    location = {"source_page": record["source_page"], "source_image": record["image"], "rect": bounded}
    if bounded != rectangle:
        location["status_note"] = "The prior automatically matched rectangle extended beyond the source image and was bounded to the actual source edge; visually review this crop before approval."
    return location


def migrate_crop_locations(records):
    manifest = json.loads(CROP_LOCATIONS.read_text())
    if manifest.get("coordinate_system", "").startswith("Local 300 dpi source-page"):
        return
    mapped = record_map(records)
    for entry in manifest["images"].values():
        location = local_location(entry["rect"], entry["pdf_page"], mapped)
        entry.update(location)
    manifest["coordinate_system"] = "Local 300 dpi source-page coordinates, except explicitly marked seam-crossing entries."
    CROP_LOCATIONS.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")


def migrate_candidates(records):
    manifest = json.loads(CANDIDATES.read_text())
    if manifest.get("coordinate_system", "").startswith("Local 300 dpi source-page"):
        return
    mapped = record_map(records)
    for collection in (manifest["known_examples"], manifest["candidates"]):
        for entry in collection:
            location = local_location(entry["rect"], entry["pdf_page"], mapped)
            entry.update(location)
    manifest["coordinate_system"] = "Local 300 dpi source-page coordinates, except explicitly marked seam-crossing entries."
    CANDIDATES.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser(description="Create lossless single-page source PNGs and migrate score locations.")
    parser.add_argument("--rerender", action="store_true", help="Regenerate cached renders and source PNGs")
    args = parser.parse_args()
    records = source_records(args.rerender)
    write_index(records)
    migrate_crop_locations(records)
    migrate_candidates(records)
    print(f"Wrote {len(records)} source-page images and migrated both location manifests.")


if __name__ == "__main__":
    main()
