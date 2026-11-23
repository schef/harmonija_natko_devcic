# M11 independent visual review

## Outcome and scope

**All 44 records reviewed: 35 PASS, 9 RECROP_REQUIRED, 0 unreviewed. Not ready for final integration.**

- Assigned milestone: printed **379–411**, PDF **190–206**, 1-based. This image review covers the 44 declared visual slots on printed **379–387**, PDF **190–194**. Printed 388–411 are outside this crop set (structured text/blank pages); no extra visual IDs or page-image crops were invented.
- Input: `review-candidates/book/M11/images-complete.json`, all 44 current candidate PNGs (including the seven `-recrop-m11.png` candidates), authoritative `sources/pages/page-379.png` through `sources/pages/page-387.png`, and `review-candidates/book/M11/text-379-387.md` for slot/caption/punctuation pairing. The latter is the existing verified-text shard; no separate file named `verifiedtext-379-387.md` exists in this directory.
- One independent reviewer; no delegation, model subprocess, API or GUI. No image, manifest, text, chapter or tracker was changed. No commit/push or human approval.
- Repository files written only: `review-candidates/book/M11/visual-review.json` and `review-candidates/book/M11/visual-review.md`. Paths in both reports are repository-root-relative.

## Method and source identity

Every candidate was decoded and compared pixel-for-pixel with its declared source rectangle: **44/44 exact RGB decoded-pixel matches**, dimensions included. Thus there is no synthesized border, painting, retouching, resampling or hidden stitch in the candidates. Exact pixel matching establishes provenance, not crop approval.

Opened every authoritative source page and each of the 19 score/realization crops. Inspected complete notation and all four edges at native resolution; inspected each of the 25 glyph crops enlarged against separately enlarged surrounding source context, including upper/lower stack levels, slash tips, plus arms and accidental stems. Extra native-pixel enlargement was used for the exercise-6 flat and slashed-7 separation. Genuine isolated scan specks were distinguished from recognizable title letters, slurs, parentheses, an i dot and sentence punctuation.

Rectangles use source PNG coordinates `[left, top, right, bottom]`, with right/bottom exclusive. PDF source indices are 1-based, not printed page numbers or zero-based array positions:

| Printed source page | PDF source page | Record slots | Decoded source size |
| --- | ---: | --- | --- |
| 379 | 190 | 1–2 | 1883 × 2589 |
| 380 | 191 | 3–6 | 1885 × 2598 |
| 381 | 191 | 7–10 | 1886 × 2598 |
| 382 | 192 | 11–14 | 1880 × 2583 |
| 383 | 192 | 15–17 | 1881 × 2583 |
| 384 | 193 | 18 | 1878 × 2575 |
| 385 | 193 | 19 | 1878 × 2575 |
| 386 | 194 | 20–30 | 1878 × 2575 |
| 387 | 194 | 31–44 | 1878 × 2575 |

`visual-review.json` gives every record's ID, exact candidate image path, printed source page, decision and individual reason. `proposed_rect` occurs **only once**, for a fully source-tested replacement. `source_limited: true` marks the eight source-layout/separation conflicts; it does not excuse a failed crop or authorize cleanup. Ordinary crop clipping in exercise 6 is not source-limited. No additional source-abrasion/illegible-notation case was independently established among the passing crops; dense or imperfect original printing was not reconstructed. Any later uncertainty about original notation must remain a separate parent hold rather than being silently repaired.

## Failed crops and correction limits

| Record | Printed/PDF page | Finding | Safe tested replacement |
| --- | --- | --- | --- |
| `M11-primjer-5-6` | 380 / 191 | Top clips the high flat in system 1, final measure. This is an additional defect, not one of the eight extractor flags. | **`[164,1810,1694,2393]`** |
| `M11-primjer-5-9` | 381 / 191 | Bottom contains partial **Andantino** from task 10; task 9's complete low slurs prevent a straight horizontal separation. | None certified |
| `M11-primjer-5-10-part-1` | 381 / 191 | Top contains task 9's cut-off low slurs/accidental. Keep task 10's genuine **Andantino**. | None certified |
| `M11-primjer-5-11` | 382 / 192 | Contains task 12's **Risoluto**; task 11's low ending reduction/beams/chord must not be clipped. | None certified |
| `M11-primjer-5-12` | 382 / 192 | Top-right contains task 11's reduction; task 12's **Risoluto** must not be removed. | None certified |
| `M11-slika-386-1` | 386 / 194 | Next-line prose survives below the 4; complete sharp descender overlaps its vertical range. | None certified |
| `M11-slika-386-2` | 386 / 194 | Right-edge parenthesis fragments survive; they are coherent punctuation, not specks. Narrowing clips the slashed 4. | None certified |
| `M11-slika-386-5` | 386 / 194 | Bottom-left ink is next-line **i dot**. At top, a slash-tip pixel at y=1724 is lost by top=1725; extending upward admits preceding-line descender ink. | None certified |
| `M11-slika-387-14` | 387 / 194 | Sentence period remains, already supplied by prose; retaining full overbar prevents a clean glyph-only rectangular crop. | None certified |

The exercise-6 proposal was actually cropped to `/tmp/opencode/m11-independent/proposal6.png` and visually inspected as a complete crop on all four edges. It restores the full flat and original blank margin without admitting exercise 5; every staff end, low final beam and final barline remains, with no page number. **The current exercise-6 candidate remains RECROP_REQUIRED** until extraction applies and integration checks the replacement.

For slika-386-5, temporary trials were rejected, not promoted to proposals. Source pixels show preceding-line coherent ink at y=1724 alongside the first upper slash-tip pixel; current top=1725 avoids the former by losing the latter. At bottom the slash reaches y=1773 and next-line i-dot ink begins y=1774. The new bottom=1778 retains part of that dot. A bottom-only adjustment does not resolve the upper overlap. No safe rectangle is asserted.

The other seven source-layout flags were independently confirmed rather than automatically accepted from the extractor notes. Where a single rectangle cannot separate interleaved material, a new source-only multipart representation would require extraction and independent re-review. No erasure, artificial whitespace, stitching, clipped notation, or invented repeated number is authorized by this report.

## Complete decision register

| Slot | Record | Printed page | Decision |
| ---: | --- | ---: | --- |
| 1 | `M11-primjer-5-1` | 379 | PASS |
| 2 | `M11-primjer-5-2` | 379 | PASS |
| 3 | `M11-primjer-5-3` | 380 | PASS |
| 4 | `M11-primjer-5-4` | 380 | PASS |
| 5 | `M11-primjer-5-5` | 380 | PASS |
| 6 | `M11-primjer-5-6` | 380 | RECROP_REQUIRED |
| 7 | `M11-primjer-5-7` | 381 | PASS |
| 8 | `M11-primjer-5-8` | 381 | PASS |
| 9 | `M11-primjer-5-9` | 381 | RECROP_REQUIRED |
| 10 | `M11-primjer-5-10-part-1` | 381 | RECROP_REQUIRED |
| 11 | `M11-primjer-5-10-part-2` | 382 | PASS |
| 12 | `M11-primjer-5-11` | 382 | RECROP_REQUIRED |
| 13 | `M11-primjer-5-12` | 382 | RECROP_REQUIRED |
| 14 | `M11-primjer-5-13-part-1` | 382 | PASS |
| 15 | `M11-primjer-5-13-part-2` | 383 | PASS |
| 16 | `M11-primjer-5-14` | 383 | PASS |
| 17 | `M11-primjer-5-15` | 383 | PASS |
| 18 | `M11-slika-384-1` | 384 | PASS |
| 19 | `M11-slika-385-1` | 385 | PASS |
| 20 | `M11-slika-386-1` | 386 | RECROP_REQUIRED |
| 21 | `M11-slika-386-2` | 386 | RECROP_REQUIRED |
| 22 | `M11-slika-386-3` | 386 | PASS |
| 23 | `M11-slika-386-4` | 386 | PASS |
| 24 | `M11-slika-386-5` | 386 | RECROP_REQUIRED |
| 25 | `M11-slika-386-6` | 386 | PASS |
| 26 | `M11-slika-386-7` | 386 | PASS |
| 27 | `M11-slika-386-8` | 386 | PASS |
| 28 | `M11-slika-386-9` | 386 | PASS |
| 29 | `M11-slika-386-10` | 386 | PASS |
| 30 | `M11-slika-386-11` | 386 | PASS |
| 31 | `M11-slika-387-1` | 387 | PASS |
| 32 | `M11-slika-387-2` | 387 | PASS |
| 33 | `M11-slika-387-3` | 387 | PASS |
| 34 | `M11-slika-387-4` | 387 | PASS |
| 35 | `M11-slika-387-5` | 387 | PASS |
| 36 | `M11-slika-387-6` | 387 | PASS |
| 37 | `M11-slika-387-7` | 387 | PASS |
| 38 | `M11-slika-387-8` | 387 | PASS |
| 39 | `M11-slika-387-9` | 387 | PASS |
| 40 | `M11-slika-387-10` | 387 | PASS |
| 41 | `M11-slika-387-11` | 387 | PASS |
| 42 | `M11-slika-387-12` | 387 | PASS |
| 43 | `M11-slika-387-13` | 387 | PASS |
| 44 | `M11-slika-387-14` | 387 | RECROP_REQUIRED |

Score/realization subtotal: **14 PASS / 5 RECROP_REQUIRED**. Inline-glyph subtotal: **21 PASS / 4 RECROP_REQUIRED**. Of seven extractor replacement candidates, **three PASS** (386-3, 386-4, 387-13) and **four RECROP_REQUIRED** (386-1, 386-2, 386-5, 387-14).

## Numbering, titles and punctuation pairing

- Exercise 10 spans 381/382 and exercise 13 spans 382/383. The continued parts correctly have **no repeated printed number**; their first-part numbers and continuation captions establish identity. No number should be added to a continuation.
- The realization images retain the full printed titles **Realizacija zadatka 4.** and **Realizacija zadatka 9.** Their captions match the source; they are not additional numbered exercises. Other notation excerpts have no assigned printed exercise number; none was invented.
- `text-379-387.md` has 44 visual slots matching the 44 records in order. This is slot/caption/punctuation review, not approval of a final assembled Markdown rendering: final image alt text and embedding are not yet available in this shard and require integration checks.
- For 386-2/3/4/5, the surrounding parentheses already exist in prose. The passing crops 386-3 and 386-4 exclude both parentheses. The rejected 386-2 retains fragments, and 386-5 has separate source-ink overlap. Do not add another pair of parentheses or accept foreign punctuation to hide a crop defect.
- The unusual `.(slot).` punctuation on text line 71 is visible in the supplied scan; this report does not silently normalize it. Parent integration must preserve source intent and avoid duplicating punctuation when replacing that slot.
- The parentheses **inside** slika-387-4 belong to its alternative ninth-chord figure and are required notation, not redundant prose punctuation.
- Full stacked/slashed figures, sharps/natural/flat and plus signs are retained in passing glyphs. Suspension slots 387-10 → 387-11 and 387-12 → 387-13 correctly pair each initial figure with its resolution; both resolution levels are present.
- Slika-387-11 excludes its following semicolon, and recropped 387-13 excludes its following period: prose supplies each once. Rejected 387-14 still contains its period, so current image-plus-prose would duplicate it. Do not solve this by clipping the overbar or deleting printed notation.

## Handoff

Review complete, no records left unreviewed. No new musical examples were extracted and no production image was modified. The 35 passing crops are suitable for parent integration subject to final embedding/link checks. **M11 overall remains on hold** for nine failed candidates: apply the one tested ordinary recrop, resolve the eight source-layout conflicts without retouching or notation loss, and obtain independent re-review of changed images. No milestone-complete approval is given.
