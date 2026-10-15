#!/usr/bin/env python3
"""Build the initial source-location manifest for all existing score crops."""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import review_crop


def caption_pages(markdown, example):
    content = markdown.read_text()
    match = re.search(rf"\*Primjer {re.escape(example)}\..*?Izvor: tiskan[ae] stranic[ae] ([\d–-]+)", content)
    assert match, f"No source-page caption found for example {example}"
    return [int(page) for page in re.findall(r"\d+", match.group(1))]


def candidate_pdf_pages(pages):
    return sorted({review_crop.pdf_page_for_printed_page(page) for page in pages})


def source_match(pdf_page, image):
    source = review_crop.render_source(pdf_page, False)
    rectangle, certainty = review_crop.coarse_rectangle(source, image)
    return rectangle, certainty


def main():
    entries = {}
    manifest = {"version": 1, "dpi": 300, "images": entries}
    for chapter in ("1", "2"):
        section = "01-uvod" if chapter == "1" else "02-dijatonika-a"
        markdown = review_crop.ROOT / "chapters" / ("01-uvod.md" if chapter == "1" else "02-dijatonika-a.md")
        for image in sorted((review_crop.ROOT / "images" / section).glob("primjer-*.png")):
            match = re.match(r"primjer-(\d+)-(\d+)", image.stem)
            assert match and match.group(1) == chapter, image
            example = f"{match.group(1)}.{match.group(2)}"
            pages = caption_pages(markdown, example)
            candidates = [(pdf_page, *source_match(pdf_page, image)) for pdf_page in candidate_pdf_pages(pages)]
            pdf_page, rectangle, certainty = max(candidates, key=lambda item: item[2])
            entries[review_crop.manifest_key(image)] = {"pdf_page": pdf_page, "printed_pages": pages, "rect": rectangle, "match_ncc": round(certainty, 6)}
            review_crop.write_manifest(manifest)
            print(f"{example:<6} {image.name:<35} PDF {pdf_page:<3} {rectangle} NCC {certainty:.6f}")
    review_crop.write_manifest(manifest)
    print(f"Wrote {len(entries)} crop locations to {review_crop.MANIFEST}")


if __name__ == "__main__":
    main()
