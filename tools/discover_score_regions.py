#!/usr/bin/env python3
"""Create a review manifest of likely musical-score regions in the full PDF.

The output deliberately records *candidates*, not verified examples. It finds
five-line staffs by their repeated long horizontal rules, then merges nearby
systems on the same printed page. Each rectangle is in 300 dpi source pixels,
ready for use by the crop reviewer after a human supplies the example number.
"""

import argparse
import json
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
PDF = next(ROOT.glob("*.pdf"))
CACHE = Path("/tmp/opencode/harmonija-score-discovery")
OUTPUT = ROOT / "tools" / "score-region-candidates.json"
KNOWN_LOCATIONS = ROOT / "tools" / "crop-locations.json"
RENDER_DPI = 150
SOURCE_DPI = 300


def render(pdf_page):
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / f"pdf-page-{pdf_page:03d}-{RENDER_DPI}dpi.png"
    if not path.is_file():
        subprocess.run(["pdftoppm", "-f", str(pdf_page), "-l", str(pdf_page), "-r", str(RENDER_DPI), "-png", "-singlefile", str(PDF), str(path.with_suffix(""))], check=True)
    return path


def runs(values, max_gap=1):
    positions = np.flatnonzero(values)
    if not len(positions):
        return []
    groups = [[int(positions[0])]]
    for value in positions[1:]:
        if value - groups[-1][-1] <= max_gap + 1:
            groups[-1].append(int(value))
        else:
            groups.append([int(value)])
    return [(group[0], group[-1]) for group in groups]


def staff_systems(page):
    """Return approximate score-system rectangles on one printed-page half."""
    ink = np.asarray(page.convert("L")) < 150
    height, width = ink.shape
    window = min(100, width - 1)
    cumulative = np.cumsum(ink, axis=1, dtype=np.int32)
    horizontal_strength = (cumulative[:, window:] - cumulative[:, :-window]).max(axis=1)
    line_runs = runs(horizontal_strength >= 70, max_gap=2)
    centers = [(start + end) // 2 for start, end in line_runs]
    groups = []
    for center in centers:
        if not groups or center - groups[-1][-1] > 16:
            groups.append([center])
        else:
            groups[-1].append(center)
    systems = []
    for group in groups:
        if len(group) < 5 or group[-1] - group[0] > 95:
            continue
        top, bottom = max(0, group[0] - 28), min(height, group[-1] + 29)
        column_ink = ink[top:bottom].sum(axis=0)
        spans = [(start, end) for start, end in runs(column_ink >= 3, max_gap=7) if end - start >= 100]
        if not spans:
            continue
        left, right = spans[0][0], spans[-1][1]
        if right - left < 250:
            continue
        systems.append([max(0, left - 18), top, min(width, right + 19), bottom])
    return systems


def merge_systems(systems):
    """Merge vertically adjacent systems that belong to one likely example."""
    merged = []
    for system in sorted(systems, key=lambda value: (value[1], value[0])):
        if not merged:
            merged.append(system)
            continue
        previous = merged[-1]
        overlap = max(0, min(previous[2], system[2]) - max(previous[0], system[0]))
        narrower = min(previous[2] - previous[0], system[2] - system[0])
        gap = system[1] - previous[3]
        if narrower and overlap / narrower >= 0.55 and gap <= 115:
            previous[0] = min(previous[0], system[0])
            previous[1] = min(previous[1], system[1])
            previous[2] = max(previous[2], system[2])
            previous[3] = max(previous[3], system[3])
        else:
            merged.append(system)
    return merged


def source_rectangle(rectangle, x_offset):
    scale = SOURCE_DPI // RENDER_DPI
    left, top, right, bottom = rectangle
    return [(left + x_offset) * scale, top * scale, (right + x_offset) * scale, bottom * scale]


def page_candidates(pdf_page):
    with Image.open(render(pdf_page)) as image:
        page = image.convert("L")
    width, height = page.size
    midpoint = width // 2
    candidates = []
    for side, left, printed_page in (("left", 0, pdf_page * 2 - 2), ("right", midpoint, pdf_page * 2 - 1)):
        half = page.crop((left, 0, midpoint if side == "left" else width, height))
        for sequence, rectangle in enumerate(merge_systems(staff_systems(half)), start=1):
            candidates.append(
                {
                    "id": f"pdf-{pdf_page:03d}-{side}-{sequence:02d}",
                    "pdf_page": pdf_page,
                    "printed_page": printed_page if printed_page > 0 else None,
                    "page_side": side,
                    "rect": source_rectangle(rectangle, left),
                    "status": "needs_review",
                    "example": None,
                    "notes": "Automated staff-line detection; confirm boundaries, labels, and whether this is a distinct example.",
                }
            )
    return candidates


def known_examples():
    """Preserve every existing hand-maintained crop location in the inventory."""
    if not KNOWN_LOCATIONS.is_file():
        return []
    locations = json.loads(KNOWN_LOCATIONS.read_text())
    result = []
    for image_path, entry in sorted(locations["images"].items()):
        filename = Path(image_path).stem
        parts = filename.split("-")
        example = f"{parts[1]}.{parts[2]}" if len(parts) == 3 else filename
        result.append(
            {
                "example": example,
                "image": image_path,
                "pdf_page": entry["pdf_page"],
                "printed_pages": entry["printed_pages"],
                "rect": entry["rect"],
                "status": "existing_crop_needs_review",
                "notes": "Imported from crop-locations.json; preserve this entry while reviewing the full-PDF discovery candidates.",
            }
        )
    return result


def main():
    parser = argparse.ArgumentParser(description="Discover likely score regions throughout Harmonija.")
    parser.add_argument("--first-page", type=int, default=1)
    parser.add_argument("--last-page", type=int, default=206)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    assert 1 <= args.first_page <= args.last_page <= 206
    candidates = []
    for pdf_page in range(args.first_page, args.last_page + 1):
        found = page_candidates(pdf_page)
        candidates.extend(found)
        print(f"PDF {pdf_page:03d}: {len(found)} candidate regions", flush=True)
    output = {
        "version": 1,
        "source_pdf": PDF.name,
        "source_dpi": SOURCE_DPI,
        "detection_dpi": RENDER_DPI,
        "scope": {"pdf_pages": [args.first_page, args.last_page]},
        "candidates": candidates,
        "warning": "This is an automated discovery inventory, not a verified list. It can split one multi-system example, merge nearby examples, miss weak or short notation, and include false positives. Review every entry against the source scan before extraction.",
        "known_examples": known_examples(),
        "candidates": candidates,
        "candidates": candidates,
    }
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {len(output['known_examples'])} known and {len(candidates)} candidate score regions to {args.output}")


if __name__ == "__main__":
    main()
