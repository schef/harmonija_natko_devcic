# M09 extraction hand-off: printed 309–328

## Scope and output

- Assigned printed pages: **309–328**, all 20 pages opened visually.
- Assigned 1-based PDF pages: **155–165**. Correct mapping for these two-up scans is `printed_page // 2 + 1`, including even printed pages.
- Read verified text candidates `review-candidates/book/M09/text-309-312.md`, `review-candidates/book/M09/text-313-316.md`, `review-candidates/book/M09/text-317-318.md`, and only the through-328 portion of `review-candidates/book/M09/text-319-333.md`.
- Created **68 separate PNG crops** in `images/04-neakordicki-b/`.
- Created `review-candidates/book/M09/images-309-328.json`, with one record for each visual slot, root-relative source/output paths, original local source-pixel rectangles, correct PDF index, caption, source caveats, and review status.
- Created reproducible guarded extractor `review-candidates/book/M09/extract-309-328.py` and this hand-off file.
- No pre-existing PNGs were present in the output directory at initial inspection. No existing image or shared text/manifests/tracker was overwritten. The old `review-candidates/book/M09/extract.py` was read only as a partial hint; never imported or executed.
- No delegation, model subprocess, API, GUI, commit, or push was used.

## Slot mapping and independent-review results

**Every listed image is `pending_independent_review`; there are no pass approvals.** The manifest records that result individually for all 68 images. Extractor edge inspection is not independent approval.

Example filenames use `images/04-neakordicki-b/primjer-4-<number>.png`. Exercise filenames use `images/04-neakordicki-b/zadatak-4-<printed-page>-<number>.png`; realization filenames append `-realizacija` to the exercise number.

| Printed page | PDF page | Visual slots / images | Count | Image-review result for each listed image |
| --- | --- | --- | ---: | --- |
| 309 | 155 | 4.53, 4.54 | 2 | pending independent review |
| 310 | 156 | 4.55, 4.56, 4.57, 4.58 | 4 | pending independent review |
| 311 | 156 | 4.59, 4.60 | 2 | pending independent review |
| 312 | 157 | 4.61, 4.62, 4.63, 4.64 | 4 | pending independent review |
| 313 | 157 | 4.65, 4.66, 4.67, 4.68 | 4 | pending independent review |
| 314 | 158 | 4.69, 4.70, 4.71 | 3 | pending independent review |
| 315 | 158 | Zadaci 1, 2, 3, 4, 5 | 5 | pending independent review |
| 316 | 159 | Zadaci 6, 7, 8 | 3 | pending independent review |
| 317 | 159 | Zadatak 9; Realizacija zadatka 3 | 2 | pending independent review |
| 318 | 160 | 4.72, 4.73, 4.74, 4.75 | 4 | pending independent review |
| 319 | 160 | 4.76, 4.77, 4.78, 4.79, 4.80 | 5 | pending independent review |
| 320 | 161 | 4.81, 4.82 | 2 | pending independent review |
| 321 | 161 | Zadaci 1, 2, 3, 4, 5 | 5 | pending independent review |
| 322 | 162 | Realizacija zadatka 4; 4.83, 4.84 | 3 | pending independent review |
| 323 | 162 | 4.85, 4.86, 4.87, 4.88 | 4 | pending independent review |
| 324 | 163 | 4.89, 4.90, 4.91 | 3 | pending independent review |
| 325 | 163 | 4.92, 4.93, 4.94 | 3 | pending independent review |
| 326 | 164 | 4.95, 4.96, 4.97; 4.98 a–c (`primjer-4-98-a.png`) | 4 | pending independent review |
| 327 | 164 | 4.98 d–e (`primjer-4-98-b.png`), 4.99, 4.100 | 3 | pending independent review |
| 328 | 165 | 4.101, 4.102, 4.103 | 3 | pending independent review |
| **Total** | | **68 text slots → 68 images** | **68** | **all pending** |

There is no count discrepancy: verified text already provides two visual slots for 4.98. The second image preserves only the actual continuation and labels d–e; its source does **not** repeat the example number. No fake number, joining, or stitching was added.

## Source constraints and required reviewer attention

- **4.67 / printed 313 — `footnote_overlap`:** Full-resolution source inspection showed the lowest fermata reaching into the same vertical band as the first ink of the separately transcribed footnote. A single rectangle spanning the complete example cannot exclude that footnote without clipping the fermata or retaining a partial prose fragment. The crop therefore retains the **complete printed footnote**, with the printed score asterisk also intact. This is an explicit exception requiring independent reviewer/integrator disposition, not a clean-score pass.
- **4.60 / printed 311 — cleanup:** marginal handwriting touches the right staff ending. Notation and original pixels were preserved rather than clipped or painted. Handwriting also remains elsewhere in the example.
- **4.53–4.58, 4.61, 4.63–4.68, 4.71 — cleanup:** pencil circles, labels, and/or harmonic analysis remain in original source pixels. Per-image notes describe their placement. Source marks are not silently retouched.
- **4.68 / printed 313:** unusually tight upper separation from the preceding paragraph underline. The crop excludes that paragraph and preserves the clef and upper stems; pencil interference remains flagged.
- **4.74 / printed 318 — source_layout/source_damage:** irregular open staff endpoints in variant c are visible in the source itself. No repair was generated.
- **4.70, 4.87, 4.94–4.96, 4.100:** open staff endings are printed/source layout, not newly truncated or reconstructed endings.
- **Realizations / printed 317 and 322:** both printed realization titles are included in their images, not omitted under the assumption that text transcription substitutes for the title.
- **4.101–4.103 / printed 328:** composer/work attributions and lowest fermatas are retained. The left edge of 4.103 avoids the printed page number while keeping the entire lower notation and genuine source whitespace.
- No unreadable source was reconstructed or guessed; original scan quality, handwriting, and damage remain visible and flagged where relevant.

## Checks performed and integration readiness

- All four edges of each initial crop were inspected in full-resolution, unresized edge strips. Additional complete-crop and source-detail views were used for 4.66–4.68; those selections were corrected to preserve complete attribution/fermata and handle the footnote overlap explicitly.
- Programmatic checks confirmed 68 visual comments in the assigned verified text range, 68 manifest records, 68 distinct existing output paths, PDF indices 155–165, and byte-for-byte decoded pixel equality between **every PNG** and its stated original source rectangle.
- No artificial border, padding, painting, resizing of final crops, stitching, or generated content was used. Original four-edge rectangles were selected per example, not expanded using a fixed batch margin.
- **Ready for independent visual review: yes. Ready for final integration/completion: no.** All 68 images still require a separate reviewer's pass/recrop-required decision; 4.67 additionally requires disposition of its documented inseparable footnote overlap. No chapter text, shared manifest, or milestone tracker was edited.
