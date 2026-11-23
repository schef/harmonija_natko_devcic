# M08 extraction and coverage hand-off

## Scope and outcome

- Assigned printed pages **277–308**, PDF pages **139–155 (1-based)**.
- Opened all **32** source PNGs individually, including the prose-only page 279, and reconciled their visual contents against both verified text shards and the existing crop inventory.
- **105 visual slots → 105 manifest records → 105 candidate images**: 49 slots in `review-candidates/book/M08/text-277-292.md`, 56 in `review-candidates/book/M08/text-293-308.md`.
- Inventory: **54 numbered-example page parts**, **42 exercise page parts**, **7 realization page parts**, **2 unnumbered inline graphics**. The 54 example parts cover printed examples 4.1–4.52, with separate continuations of 4.1 and 4.21. Continuations and multi-system examples are not missing examples or duplicated slots.
- All **105** candidates remain `pending_independent_review`. No crop is self-approved. This is a coverage/extraction hand-off, **not integration approval**.

## Outputs and preservation

- Complete candidate manifest: `review-candidates/book/M08/images-complete.json`.
- Reproducible source-only reconciliation: `review-candidates/book/M08/reconcile.py`.
- This hand-off: `review-candidates/book/M08/extraction-complete.md`.
- Newly extracted inline figure: `images/04-neakordicki-a/sifra-appoggiature-304.png`.
- Nine separate corrective crops listed below; no original crop was overwritten.
- Preserved unchanged: raw `review-candidates/book/M08/images.json` (103 records), all its 103 image files, `review-candidates/book/M08/inline-progression.json`, the already-created `images/04-neakordicki-a/progresija-277.png`, both verified text shards, and their text-review files.
- No chapter, global tracker, commit, push, delegation, model subprocess, API or GUI work.

Manifest paths are relative to the repository root. Rectangles are local source-PNG pixel coordinates `[left, top, right, bottom]`, with right/bottom exclusive. `pdf_page` is the original PDF's 1-based index, not the printed page number. Every record carries the verified shard's exact `slot_label`, `slot_source`, `slot_line`, and global `slot_index`; this disambiguates repeated exercise numbers and unnumbered inline slots without inventing printed IDs. Captions include printed source pages, and `musescore_hint` explicitly distinguishes unnumbered graphics.

## Added inline graphic

| Printed / PDF page | Manifest ID (descriptive, not printed) | Image | Source rectangle |
| --- | --- | --- | --- |
| 277 / 139 | `progresija-277` | `images/04-neakordicki-a/progresija-277.png` (existing supplement reused) | `[968,1556,1329,1632]` |
| 304 / 153 | `sifra-appoggiature-304` | `images/04-neakordicki-a/sifra-appoggiature-304.png` | `[1278,958,1373,1048]` |

The second image is the stacked **9/7/4 > 8/3** symbol in note ** after the continuation of realization 3 in section 4.1.6. It is separate from both the realization and example 4.46. Retain it at its inline text slot. Both inline figures still require independent review and later MuseScore reconstruction; neither has a printed example number.

## Separate recrops

The manifest retains `original_image` and `original_rect` for every corrected record. All source content is copied as-is: no retouching, stitching, rescaling, generated borders or painted margins.

| ID | Printed page | New candidate under `images/04-neakordicki-a/` | Correction |
| --- | --- | --- | --- |
| 4.13 | 283 | `primjer-4-13-coverage-recrop.png` | Restore the lowest bass stem and genuine lower whitespace; bottom changed from 2382 to 2400. |
| 4.z289-9-realizacija | 289 | `zadatak-4-289-9-realizacija-naslov-recrop.png` | Include printed realization title; top 1989 → 1925. |
| 4.z294-5-realizacija | 294 | `zadatak-4-294-5-realizacija-naslov-recrop.png` | Include printed realization title; top 942 → 780. |
| 4.z297-3-realizacija | 297 | `zadatak-4-297-3-realizacija-naslov-recrop.png` | Include printed realization title; top 1069 → 965. |
| 4.z303-3 | 303 | `zadatak-4-303-3-coverage-recrop.png` | Restore upper slur; top 550 → 543. Adjacent figured-bass fragments are inseparable by rectangular cropping: cleanup flag, not a pass. |
| 4.z303-3-realizacija | 303 | `zadatak-4-303-3-realizacija-naslov-recrop.png` | Include printed realization title; top 1944 → 1880. |
| 4.z306-1 | 306 | `zadatak-4-306-1-coverage-recrop.png` | Exclude the next exercise's highest note; bottom 1918 → 1913, retaining all own final figures. |
| 4.z306-2 | 306 | `zadatak-4-306-2-coverage-recrop.png` | Restore highest note with the available small source gap; top 1917 → 1913. |
| 4.z308-3-realizacija | 308 | `zadatak-4-308-3-realizacija-naslov-recrop.png` | Include printed realization title; top 188 → 110. |

## Page-by-page coverage

Every row is pending independent image review. Numbered variants, full multi-system examples, composer attributions, exercise figures, titles and continuation endings were reconciled against the source page, rather than inferred from prose references alone.

| Printed | PDF | Slots | Visual contents |
| --- | --- | --- | --- |
| 277 | 139 | 2 | Inline progression; 4.1 a–b. |
| 278 | 140 | 2 | 4.1 c continuation; 4.2. |
| 279 | 140 | 0 | Prose only; no omitted figure. |
| 280 | 141 | 1 | 4.3. |
| 281 | 141 | 2 | 4.4–4.5. |
| 282 | 142 | 4 | 4.6–4.9. |
| 283 | 142 | 4 | 4.10–4.13. |
| 284 | 143 | 3 | 4.14–4.16, including all three Bach attributions. |
| 285 | 143 | 2 | 4.17 a–i and 4.18 a–g, each retaining both systems. |
| 286 | 144 | 3 | 4.19; complete two-system 4.20; 4.21 a–c. |
| 287 | 144 | 4 | 4.21 d–f; section 4.1.2 exercises 1–2 and start of 3. |
| 288 | 145 | 6 | Exercise 3 continuation; exercises 4–8. |
| 289 | 145 | 6 | Exercises 9–13; realization 9 start with title. |
| 290 | 146 | 2 | Realization 9 continuation and final ending; 4.22. |
| 291 | 146 | 4 | 4.23–4.26. |
| 292 | 147 | 4 | 4.27–4.30. |
| 293 | 147 | 6 | Section 4.1.3 exercises 1–5 and start of 6. |
| 294 | 148 | 3 | Exercise 6 continuation; exercise 7; realization 5 with title. |
| 295 | 148 | 4 | 4.31–4.34. |
| 296 | 149 | 3 | 4.35 a–e; section 4.1.4 exercises 1–2. |
| 297 | 149 | 3 | Exercises 3–4; complete three-system realization 3 with title. |
| 298 | 150 | 3 | 4.36–4.37; section 4.1.5 exercise 1 start. |
| 299 | 150 | 3 | Exercise 1 continuation; exercise 2; complete two-system 4.38 a–f. |
| 300 | 151 | 3 | 4.39–4.40; complete two-system 4.41 a–e. |
| 301 | 151 | 3 | 4.42–4.44. |
| 302 | 152 | 3 | Complete two-system 4.45 a–d; section 4.1.6 exercise 1; exercise 2 start. |
| 303 | 152 | 6 | Exercise 2 continuation; exercises 3–6; realization 3 start with title. |
| 304 | 153 | 3 | Realization 3 continuation and * / ** markers; inline figured symbol in **; full two-system 4.46 a–h and printed “itd.” |
| 305 | 153 | 4 | 4.47–4.50. |
| 306 | 154 | 4 | 4.51; 4.52 with Chopin attribution; section 4.1.7 exercise 1; exercise 2 start. |
| 307 | 154 | 4 | Exercise 2 continuation; exercises 3–5. |
| 308 | 155 | 1 | Complete five-system realization 3 with title, lowest final bass note and final double barline. |

## Verification and unresolved source issues

- `python review-candidates/book/M08/reconcile.py` verifies **all 105 candidate images** against the exact decoded pixels of their source rectangles and separately verifies **all 103 original images**. All match, including dimensions. It asserts the 49/56 slot totals, 105-record count, slot-page correspondence and original 1-based PDF mapping.
- Native-resolution four-edge strips of all 103 originals were inspected, followed by direct inspection of the new inline crop and all nine recrops. This extractor inspection is not independent review and confers no approval.
- **22 records have `cleanup_required: true`**. Source handwriting remains in/touching examples 4.1 (both page parts), 4.2–4.5, 4.7, 4.9–4.12, 4.14–4.17 and 4.22–4.26. These are deliberately not retouched; some handwritten marks cross crop boundaries or sit between adjacent examples.
- The other two cleanup flags are the page-303 exercise-2 continuation / exercise-3 boundary. The low figures and high slur overlap vertically. A rectangular source crop cannot remove all foreign ink while retaining all intended notation. Exercise 3 now retains the previously clipped upper slur, but both candidates require the independent reviewer/integrator's explicit decision. They are **not clean/pass crops**.
- Existing scan abrasion/loss intersects notation on page 290 (first system, lower staff near second measure, realization 9 continuation) and page 295 (4.31 c, upper staff). Each affected record carries a `source_condition_note`. Source pixels are retained; interpreting lost notation for MuseScore is outside extraction and cannot be solved by expanding a crop.
- No other missing visual slot was found in the assigned 32-page range. No unreadable prose was transcribed or changed in this role.

## Integration readiness

Coverage and source-only extraction are ready for **independent review of all 105 candidates** using `review-candidates/book/M08/images-complete.json`. They are **not ready for final integration approval** until that review resolves or explicitly handles all cleanup/source-condition flags and returns per-image pass/recrop-required decisions. The original 103-record manifest must remain preserved as provenance, not mistaken for the complete coverage inventory.
