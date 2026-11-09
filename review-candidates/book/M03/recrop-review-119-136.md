# Independent recrop review — corrected example 2.265

**PASS — 1 image re-reviewed; 0 recrop failures.**

| ID | Image | Printed page | PDF page | Rectangle | Decision | source_limited | proposed_rect |
| --- | --- | ---: | ---: | --- | --- | --- | --- |
| primjer-2-265 | images/02-dijatonika-b/recrops/primjer-2-265.png | 121 | 61 | [209, 2010, 1738, 2381] | PASS | false | null |

Authoritative image: `sources/pages/page-121.png`. Corrected manifest: `review-candidates/book/M03/images-corrected-119-136.json`. Rectangles use source pixels `[left, top, right, bottom]`, right/bottom exclusive.

## Visual and pixel checks

The complete recrop was compared with the authoritative source page, and **all four edges were separately inspected at native resolution**.

- **Top — PASS:** the preceding example's partial handwritten **3** is gone. All sequence brackets survive, including the highest/rightmost bracket, whose ink begins at source y=2014. The crop starts at y=2010, retaining four genuine source rows above it.
- **Bottom — PASS:** lowest bass beams and the final flagged note are intact, with original white margin; no page number or foreign lettering.
- **Left — PASS:** complete **2.265**, braces, clefs, key/time signatures and staff beginnings are retained, with genuine clean margin.
- **Right — PASS:** complete printed open staff ends, final notes/flags and rightmost bracket are intact, with genuine clean margin. No final barline is printed at these open ends.
- **Complete notation — PASS:** both staves, all notes/rests/stems/beams and sequence brackets agree with the source. No composer attribution or lettered variants are printed for this example. No surrounding prose, adjacent example, handwriting or partial foreign character remains. The small disconnected cluster under the first bracket is scan flecking, not lettering.
- **Exact decoded pixels — PASS:** candidate and source rectangle both decode as **RGB, 1529 × 371**, with identical raw decoded bytes. No retouching, resampling or artificial border was found. Decoded RGB SHA-256: `0c501f5ff463d62ae39129ca2f2fad2ae902239c563d291cce858a3922fa69e3`.

No further rectangle is proposed. This separate corrected image is ready for image integration; this is not whole-milestone approval.

## Authoritative PDF mapping correction — verified

`sources/index.json`, not the raw review manifest, is authoritative. I checked the corrected manifest's **67 records** against that index:

- **67/67** corrected `pdf_page` values and source-image paths agree with the index.
- **35** PDF-page corrections were verified against the original manifest, and all 35 retain the former value in `original_pdf_page`.
- The affected raw records are on even printed pages **120–136**, previously assigned to the preceding PDF page.
- Printed **121 → PDF 61**; printed **136 → PDF 69**. The corrected records cover PDF **60–69**.

**Correction to my earlier report:** the earlier claim that the raw manifest's PDF 60–68 mapping was correct, including printed 136 → PDF 68, was wrong. That mapping note is superseded by this source-index verification. The earlier review files were left unchanged as instructed.

## Hand-off

1. Follow-up visual scope: **example 2.265 only, printed 121 / PDF 61**; mapping verification covers the assigned printed 119–136 / PDF 60–69 range.
2. Files created only: `review-candidates/book/M03/recrop-review-119-136.json` and `review-candidates/book/M03/recrop-review-119-136.md`.
3. No examples extracted or modified by this reviewer; one parent-produced recrop inspected.
4. Result: **1 PASS, 0 RECROP_REQUIRED**, exact source-pixel match; all four edges and complete notation pass.
5. No unreadable or incomplete printed notation identified in this recrop. Other images were not visually re-reviewed in this follow-up; their source-limited failures are not waived.
6. **Corrected 2.265 ready for image integration.** No source pixels, production images, manifests, source index, prior reports, chapter or tracker were edited; no retouching, commit or push performed.
