# M03 extraction hand-off — printed pages 119–136

## Assignment and outputs

- Role: extraction only; one worker, no delegation, model subprocess, API, or GUI.
- Printed pages **119–136**, PDF pages **60–69**. All 18 authoritative
  `sources/pages/page-119.png` through `sources/pages/page-136.png` were opened
  visually. Smaller temporary viewing copies were also used to select coordinates.
- Slot source: `review-candidates/book/M03/text-119-136.md` (read only).
- **67 separate PNGs** created under `images/02-dijatonika-b/`: numbered examples
  `primjer-2-256.png` through `primjer-2-301.png` (46); exercises
  `zadatak-2-130-1.png` through `zadatak-2-130-10.png` (10),
  `zadatak-2-135-1.png` through `zadatak-2-135-9.png` (9); realizations
  `realizacija-2-131-6.png` and `realizacija-2-136-9.png` (2).
- Manifest: `review-candidates/book/M03/images-119-136.json`.
- Extraction script: `review-candidates/book/M03/extract-119-136.py`.
- This report: `review-candidates/book/M03/extraction-119-136.md`.

No chapter, candidate text, shared manifest, tracker, prior material through page
118, or another worker's output was changed. No commit or push was made.

## Coverage and review status

**Exact ordered 67/67 slot identity coverage** was asserted against the candidate
text. Every identity below has status **`pending_independent_review`**; none is
self-approved. The manifest gives each identity its own source page, PDF page,
caption, original-pixel rectangle, output path, and review note.

| Printed page | PDF page | Extracted identities (all pending independent review) |
| --- | --- | --- |
| 119 | 60 | 2.256, 2.257 |
| 120 | 61 | 2.258, 2.259, 2.260, 2.261 |
| 121 | 61 | 2.262, 2.263, 2.264, 2.265 |
| 122 | 62 | 2.266, 2.267 |
| 123 | 62 | 2.268, 2.269, 2.270 |
| 124 | 63 | 2.271, 2.272, 2.273 |
| 125 | 63 | 2.274, 2.275 |
| 126 | 64 | 2.276, 2.277, 2.278 |
| 127 | 64 | 2.279, 2.280, 2.281 |
| 128 | 65 | 2.282, 2.283, 2.284 |
| 129 | 65 | 2.285, 2.286, 2.287 |
| 130 | 66 | Zadatak 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 |
| 131 | 66 | Realizacija zadatka 6; 2.288 |
| 132 | 67 | 2.289, 2.290, 2.291, 2.292 |
| 133 | 67 | 2.293, 2.294, 2.295, 2.296 |
| 134 | 68 | 2.297, 2.298, 2.299, 2.300, 2.301 |
| 135 | 68 | Zadatak 1, 2, 3, 4, 5, 6, 7, 8, 9 |
| 136 | 69 | Realizacija zadatka 9 |

## Pixel provenance and boundaries

The script contains 67 independently specified rectangles, each with four manually
selected edges. It does not expand margins uniformly, infer crops from OCR, or
automatically segment a page. Coordinate selection uses a 1000-pixel-wide viewing
coordinate system; the manifest records the converted **local original PNG pixel
coordinates**. `rect` means Pillow `[left, top, right, bottom)` (not xywh).
All paths in the manifest are relative to repository root.

Every saved image was checked against a fresh crop of its authoritative source:
**67/67 images have identical dimensions and exact pixel equality**. There is no
resizing of saved score images, artificial border, stitching, repainting, or
retouching. The script refuses to overwrite existing PNGs; do not rerun it over
independently reviewed or corrected files.

Same-page continuation systems remain with their own example: 2.267, 2.277,
2.278, 2.284; page 130 exercise 9; page 135 exercise 4. No assigned slot requires
stitching across printed pages. Composer/work attributions and both realization
identifying titles are retained. Following body paragraphs and footnotes remain
in the source text, outside the score crops.

## Source limitations and cleanup queue

**38 crops carry `cleanup_required` in their manifest review notes.** This is an
extraction warning, not permission to retouch and not a review pass/fail decision.
Most concern pencil analyses, handwritten figures, arrows, or other source marks
near or within the score. Pixels have been preserved rather than removing marks
by clipping notation. Some source pencil marks run out of the score region toward
body text or a neighbouring example; a rectangle cannot make those marks clean.
The independent reviewer must inspect these boundary conflicts explicitly.

Special source-layout conflict: **page 130, exercises 5 and 6**. The lowest figures
of exercise 5 and the top of exercise 6's slur occupy overlapping vertical space.
Their source-only rectangles intentionally overlap slightly to avoid clipping
either exercise's notation. Adjacent ink therefore remains; both are flagged
`cleanup_required`. A strictly score-only rectangular crop cannot resolve this
collision without loss. No cleanup was attempted.

Faint source handwriting and pencil harmonic analyses are not reliably legible;
they have not been interpreted or converted into authoritative notation. No
missing printed musical example was identified. Independent review remains
necessary to establish notation completeness and every crop-edge decision.

## Integration readiness

**Ready for independent visual review, not final integration approval.** All 67
slot identities and assets are supplied. A separate reviewer must compare every
crop with its source, give pass/recrop-required decisions, and resolve flagged
source-mark/layout cases before these can be approved for integration. This
extraction-only worker has not performed or claimed independent review.
