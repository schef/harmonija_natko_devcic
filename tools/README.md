# Crop-review tool

Use the interactive reviewer to refine an existing musical-example crop:

```bash
python tools/review_crop.py 2.48
```

List the examples available in a chapter before reviewing them:

```bash
python tools/review_crop.py --list 1
python tools/review_crop.py --list 2
```

For a space-separated sequence that can be passed directly to a shell loop:

```bash
python tools/review_crop.py --list 1 --compact
# 1.1 1.2 1.3 1.4 1.5 1.6 1.7

for example in $(python tools/review_crop.py --list 1 --compact); do
  python tools/review_crop.py "$example" || exit
done
```

The tool reads `tools/crop-locations.json` to select a single rendered source
page and starting rectangle, then displays it as a cyan rectangle. Drag inside
the rectangle to move it, or drag a cyan corner to resize it. The right pane
previews the exact source crop that will be written.

Every explicit save updates that image's local source-page rectangle in the
manifest as well as writing the source-only PNG. No PDF rendering or template
matching is performed while opening an example.

`tools/build_crop_locations.py` is a legacy recovery utility for the former
two-page-spread workflow. Do not run it after creating `sources/index.json`:
the current workflow uses the local source-page coordinates already recorded
in `tools/crop-locations.json`.

## Full-PDF score discovery

To inventory likely score regions throughout the source PDF, run:

```bash
python tools/discover_score_regions.py
```

This writes `tools/score-region-candidates.json`. It records a 300 dpi source
rectangle, PDF spread, printed-page side, and review status for every region
detected from staff lines. It intentionally does **not** claim that the
candidate list is complete or that its rectangles are approved crops: a human
must check the source, assign the printed example number, and set its status
before it can be used for extraction.

## Single-page source images

Create the lossless, 300 dpi source-page set before reviewing crops:

```bash
python tools/split_source_pages.py
```

It creates `sources/pages/front-001.png` followed by
`sources/pages/page-001.png` through `sources/pages/page-411.png`, and writes
the PDF-spread/printed-page map to `sources/index.json`. The split is at the
exact source-pixel midpoint of each rendered two-page spread; it does not
resample, clean, deskew, or otherwise alter the scans.

The command also migrates the existing crop and score-candidate rectangles to
local source-page coordinates. An entry that genuinely crosses a spread seam
is retained as an explicit seam-crossing exception rather than clipping any
source content.

- **Enter** or **Save crop**: overwrite the image with the selected original
  source pixels.
- **Esc**: close without changing the image.
- **Arrow keys**: move the rectangle one source pixel.
- **+**, **-**, or the buttons: zoom the source page.

An entry that crosses the source-page seam is intentionally blocked from the
single-page reviewer. It must be resolved manually without clipping its source
content.

## Musical-example catalog

Build the compact catalog of currently extracted, assigned musical examples:

```bash
python tools/build_musical_example_catalog.py
```

The generated `tools/musical-examples.json` is the machine-readable catalog;
each entry contains its name, original printed page, original PDF spread,
local source-page location, and cropped image path. Its companion,
`tools/musical-examples.md`, presents the same catalog as a review table.

This is not yet a catalog of every musical example in the book. Only examples
already assigned a printed number and crop image are listed. Unassigned
detection candidates intentionally remain separate in
`tools/score-region-candidates.json`; they must be visually identified,
numbered, extracted, and reviewed before they can enter the catalog.

## Provisional full-book review set

Create source-only crops for all automatically detected score regions and
tentative OCR labels for manual review:

```bash
python tools/build_unverified_example_review_set.py
```

This writes `tools/unverified-musical-examples.json`, a linked review table at
`tools/unverified-musical-examples.md`, and one unaltered, approximate crop per
detector candidate under `review-candidates/`. OCR is run only on the rendered
`sources/pages/*.png` pixels using Tesseract; the tool does not read, extract,
or use any embedded PDF OCR/text. These candidate crops and names are
unverified and must never be added to the verified catalog without source-image
review.

The script needs Python's Pillow/Tk bindings plus the existing `pdftoppm` and
ImageMagick `magick` commands. It saves no artificial border or padding.
