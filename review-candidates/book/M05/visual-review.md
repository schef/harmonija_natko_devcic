# M05 — independent visual review

**104/104 reviewed: 64 PASS, 40 RECROP_REQUIRED, 0 unreviewed. Not ready for integration.**

Assigned scope: printed **175–206**, PDF **88–104**; all records in `review-candidates/book/M05/images.json`. One independent reviewer inspected the earlier extractor's images; no delegation, model subprocess, API or GUI was used. Old partial review logs were not treated as authoritative.

## Verification

- Opened every one of the **32 source PNGs** and inspected every complete crop against its source.
- Inspected **all four edges of all 104 crops at native resolution**, using lossless source/context strips with 48 pixels inside and 12 outside each edge. Side strips were rotated, not resampled. These strips supplemented the complete-crop/source comparison, not replaced it.
- Checked numbers, all variants, exercise IDs, composer/work attributions, clefs, signatures, notes/rests, ties/slurs, arrows/brackets, figures/functions, staff ends, lowest stems and realization titles.
- **104/104 exact decoded-pixel matches** to the declared source rectangles, including mode and dimensions. No retouching, resampling or artificial border detected.
- **104/104 source-index mappings agree** with `sources/index.json`, including printed/PDF page and source dimensions. PDF page = `floor(printed_page / 2) + 1` for this range.
- `review-candidates/book/M05/text-175-190.md`: **50 visual slots**. `review-candidates/book/M05/text-191-206.md`: **54 visual slots**. All **104 normalized IDs and pages match in order**; none missing, duplicated or extra.
- Checked both continuation slots (3.28 e/f on 186 and 3.67 e/f on 201), both realization slots and both exercise series explicitly. Continuations do not repeat the example number in the printed source; their lettered variants establish identity with the preceding numbered part.
- Manifest captions agree semantically with example/exercise/realization identity and printed page. The text drafts contain visual slots, **not final image alt-text/caption blocks**; no unbuilt integrated chapter is certified here.

`review-candidates/book/M05/visual-review.json` is the full per-image ledger: each record includes the root-relative image path, printed page, decision, reason, `proposed_rect` and `source_limited` flag. All images are in `images/03-kromatika-a/`; the filename is the ledger ID plus `.png`.

## Tested corrections — not applied

Coordinates are source pixels `[left, top, right, bottom]`, with exclusive right/bottom.

| ID | Page / PDF | Tested safe rectangle | Result |
| --- | --- | --- | --- |
| primjer-3-2 | 175 / 88 | `[215, 1958, 848, 2298]` | Removes marginal/top foreign ink; retains 3.2, a/b, both staves, connecting lines and feasible genuine margins. Complete test crop and all four edges inspected. |
| primjer-3-33 | 188 / 95 | `[157, 1459, 1678, 1802]` | Removes pencil chord names above score; retains the highest complete bracket, stems, number and both staves with genuine margins. Complete test crop and all four edges inspected. |

All testing was confined to temporary files under `/tmp/opencode`. A tighter top for 3.33 clipped notation and was rejected; a lower top for 3.14 clipped its attribution and was rejected. Neither rejected trial is proposed. The two current files above remain **RECROP_REQUIRED**, not retrospectively approved.

## Source-limited conflicts

**38 failures have no safe rectangular correction established.** Most contain pencil chord names/analysis inside the bounds needed by printed labels, attribution, notation or analysis. Do not erase, paint over, generate replacement background, or clip required printed content. Pixel equality proves faithful extraction, not compliance with the no-handwriting rule.

The **page-190 exercises 7 and 8** are a separate geometric conflict. Enlarged source inspection around y=680–755 shows the lowest figured-bass ink of 7 in the same vertical range as the highest slur of 8, around y=720. The current 7 clips low figures; current 8 retains foreign figure fragments. Extending 7 or lowering the top of 8 does not establish a clean complete single rectangle. These are source-limited failures, not approved compromises.

## Per-image results

For each PASS, the complete printed example/exercise was compared to its source and all four edges passed: no clipping, prose, page number, handwriting or foreign partial mark; genuine feasible margins retained. Specific failures and complete paths are recorded in the JSON ledger. `SL` means source-limited; `tested` means the safe proposal above, not an applied correction.

| ID | Printed / PDF | Decision | Finding |
| --- | --- | --- | --- |
| primjer-3-1 | 175 / 88 | PASS | Complete a–d; clean four edges. |
| primjer-3-2 | 175 / 88 | RECROP_REQUIRED | Marginal/top foreign ink; tested recrop. |
| primjer-3-3 | 175 / 88 | RECROP_REQUIRED | SL: handwriting inside attribution/score bounds. |
| primjer-3-4 | 176 / 89 | RECROP_REQUIRED | SL: pencil traces in bass-staff area. |
| primjer-3-5 | 176 / 89 | RECROP_REQUIRED | SL: pencil traces inside/below score. |
| primjer-3-6 | 177 / 89 | RECROP_REQUIRED | SL: handwriting between staves. |
| primjer-3-7 | 178 / 90 | RECROP_REQUIRED | SL: left handwriting cannot be excluded while retaining number. |
| primjer-3-8 | 178 / 90 | RECROP_REQUIRED | SL: internal/lower handwriting; tight next-example boundary. |
| primjer-3-9 | 178 / 90 | RECROP_REQUIRED | SL: handwritten analysis in required notation band. |
| primjer-3-10 | 178 / 90 | RECROP_REQUIRED | SL: handwriting above/below score. |
| primjer-3-11 | 179 / 90 | RECROP_REQUIRED | SL: writing beside labels and below notes. |
| primjer-3-12 | 179 / 90 | RECROP_REQUIRED | SL: writing shares label/analysis bands. |
| primjer-3-13 | 179 / 90 | RECROP_REQUIRED | SL: top prose fragments plus embedded writing. |
| primjer-3-14 | 179 / 90 | RECROP_REQUIRED | SL: writing shares Wagner attribution band. |
| primjer-3-15 | 180 / 91 | RECROP_REQUIRED | SL: writing in required analysis band. |
| primjer-3-16 | 180 / 91 | RECROP_REQUIRED | SL: writing beside a/b and in analysis area. |
| primjer-3-17 | 180 / 91 | RECROP_REQUIRED | SL: writing at/below Liszt attribution. |
| primjer-3-18 | 181 / 91 | PASS | Complete a/b and lower analysis. |
| primjer-3-19 | 182 / 92 | RECROP_REQUIRED | SL: handwriting above/between systems. |
| primjer-3-20 | 183 / 92 | PASS | Complete a/b and lower analysis. |
| primjer-3-21 | 183 / 92 | RECROP_REQUIRED | SL: writing within score/function bounds. |
| primjer-3-22 | 183 / 92 | RECROP_REQUIRED | SL: writing in upper/inter-system bands. |
| primjer-3-23 | 183 / 92 | RECROP_REQUIRED | SL: writing at a/b height. |
| primjer-3-24 | 184 / 93 | RECROP_REQUIRED | SL: writing in label/function bands. |
| primjer-3-25 | 184 / 93 | RECROP_REQUIRED | SL: writing at labels and beneath staves. |
| primjer-3-26 | 185 / 93 | RECROP_REQUIRED | SL: writing shares labels/functions. |
| primjer-3-27 | 185 / 93 | RECROP_REQUIRED | SL: top previous-function fragment plus handwriting. |
| primjer-3-28 | 185 / 93 | RECROP_REQUIRED | SL: writing throughout a–d systems. |
| primjer-3-28-p186 | 186 / 94 | RECROP_REQUIRED | SL: e/f and Bach attribution retained, but embedded writing. |
| primjer-3-29 | 186 / 94 | RECROP_REQUIRED | SL: handwriting above/between/below systems. |
| primjer-3-30 | 187 / 94 | PASS | Bach attribution, both systems and full analysis. |
| primjer-3-31 | 187 / 94 | PASS | Chopin attribution and full lower analysis. |
| primjer-3-32 | 188 / 95 | RECROP_REQUIRED | SL: top prose fragments plus inter-system writing. |
| primjer-3-33 | 188 / 95 | RECROP_REQUIRED | Pencil names above score; tested recrop. |
| primjer-3-34 | 188 / 95 | RECROP_REQUIRED | SL: handwriting above/within/below score. |
| primjer-3-35 | 189 / 95 | RECROP_REQUIRED | SL: writing shares lowest-stem band. |
| primjer-3-36 | 189 / 95 | RECROP_REQUIRED | SL: writing in label/bracket/inter-system bands. |
| zadatak-3-189-2 | 189 / 95 | PASS | Full figures, accidentals and final barline. |
| zadatak-3-189-3 | 189 / 95 | PASS | Lowest sharp complete with bottom margin. |
| zadatak-3-189-4 | 189 / 95 | PASS | Full figures and staff ends. |
| zadatak-3-190-5 | 190 / 96 | PASS | Full figures and staff ends. |
| zadatak-3-190-6 | 190 / 96 | PASS | Full figures and final barline. |
| zadatak-3-190-7 | 190 / 96 | RECROP_REQUIRED | SL: clipped low figures conflict with next slur. |
| zadatak-3-190-8 | 190 / 96 | RECROP_REQUIRED | SL: foreign figure fragments conflict with highest slur. |
| zadatak-3-190-9 | 190 / 96 | PASS | Highest slur and complete notation. |
| zadatak-3-190-10 | 190 / 96 | PASS | Both complete systems. |
| zadatak-3-190-11 | 190 / 96 | PASS | Full slurs and staff ends. |
| zadatak-3-190-12 | 190 / 96 | PASS | Key signature and high slurs intact. |
| zadatak-3-190-13 | 190 / 96 | PASS | Full slurs, accidentals and final barline. |
| zadatak-3-190-14 | 190 / 96 | PASS | Both systems complete; no page number. |
| zadatak-3-191-8-realizacija | 191 / 96 | PASS | Full realization title and lowest stems. |
| primjer-3-37 | 192 / 97 | RECROP_REQUIRED | SL: writing shares title/analysis bands. |
| primjer-3-38 | 192 / 97 | RECROP_REQUIRED | SL: writing above staves and by lower function. |
| primjer-3-39 | 193 / 97 | RECROP_REQUIRED | SL: writing above score and by D/IV. |
| primjer-3-40 | 193 / 97 | RECROP_REQUIRED | SL: writing shares E-c heading band. |
| primjer-3-41 | 193 / 97 | RECROP_REQUIRED | SL: writing shares H-es heading band. |
| primjer-3-42 | 193 / 97 | RECROP_REQUIRED | SL: embedded chord names/figures. |
| primjer-3-43 | 194 / 98 | PASS | Heading, score and full lower analysis. |
| primjer-3-44 | 194 / 98 | PASS | Heading, staff ends and lower analysis. |
| primjer-3-45 | 194 / 98 | PASS | Long score and lowest stems intact. |
| primjer-3-46 | 194 / 98 | PASS | Full lower IV figures. |
| primjer-3-47 | 194 / 98 | PASS | Continuation ends and lower analysis. |
| primjer-3-48 | 195 / 98 | PASS | Heading and full A:V2. |
| primjer-3-49 | 195 / 98 | PASS | Lowest stems and Des:V7. |
| primjer-3-50 | 195 / 98 | PASS | Both staves and D:V. |
| primjer-3-51 | 195 / 98 | PASS | Time signature and lower function. |
| primjer-3-52 | 195 / 98 | PASS | Continuation sign and g:IV. |
| primjer-3-53 | 195 / 98 | PASS | Lowest stacked IV figures. |
| primjer-3-54 | 196 / 99 | PASS | Full staff ends and Es:I. |
| primjer-3-55 | 196 / 99 | PASS | Ties and H:IV intact. |
| primjer-3-56 | 196 / 99 | PASS | Accidentals and lowest stems intact. |
| primjer-3-57 | 196 / 99 | PASS | Enclosures and cis:V7 intact. |
| primjer-3-58 | 196 / 99 | PASS | Both signatures, enclosure and final barline. |
| primjer-3-59 | 197 / 99 | PASS | Liszt attribution; all four staves and instrument labels. |
| primjer-3-60 | 197 / 99 | PASS | Chopin attribution and full upper/lower slurs. |
| primjer-3-61 | 197 / 99 | PASS | Wagner attribution and lowest bass stems. |
| primjer-3-62 | 198 / 100 | PASS | Grieg attribution; both three-staff systems. |
| primjer-3-63 | 199 / 100 | PASS | All a–d and lowest a:VI function. |
| primjer-3-64 | 199 / 100 | PASS | All a–c and complete functions. |
| primjer-3-65 | 200 / 101 | PASS | a/b, continuation sign and sharp-five analysis. |
| primjer-3-66 | 200 / 101 | PASS | Complete d:VII7; no following prose. |
| primjer-3-67 | 200 / 101 | PASS | All a–d and complete lowest stacked figures. |
| primjer-3-67-p201 | 201 / 101 | PASS | e/f continuation; lowest figure 3 intact. |
| primjer-3-68 | 201 / 101 | PASS | All a–c and complete lower functions. |
| primjer-3-69 | 201 / 101 | PASS | Full Beethoven attribution and lowest bass notes. |
| primjer-3-70 | 202 / 102 | PASS | Optional accidentals and full stacked figures. |
| primjer-3-71 | 202 / 102 | PASS | All a–e, both systems and lowest figures. |
| primjer-3-72 | 202 / 102 | PASS | a/b, optional accidentals and full clef. |
| primjer-3-73 | 203 / 102 | PASS | Full lower V2 and staff ends. |
| primjer-3-74 | 203 / 102 | PASS | Continuation sign and stacked VII figures. |
| primjer-3-75 | 203 / 102 | PASS | Full f:VII7; no ZADACI prose. |
| primjer-3-76 | 204 / 103 | PASS | Boxed title; both systems and lowest stems. |
| primjer-3-77 | 204 / 103 | PASS | All a–f and upper/lower brackets. |
| primjer-3-78 | 205 / 103 | PASS | All a–d, brackets and optional accidentals. |
| zadatak-3-205-2 | 205 / 103 | PASS | All figures including lowest 3. |
| zadatak-3-205-3 | 205 / 103 | PASS | Both systems; lowest sharp intact. |
| zadatak-3-205-4 | 205 / 103 | PASS | Both systems and full signatures. |
| zadatak-3-205-5 | 205 / 103 | PASS | All accidentals and lowest final note. |
| zadatak-3-205-6 | 205 / 103 | PASS | Both systems; no page number. |
| zadatak-3-206-7 | 206 / 104 | PASS | Both high slurs and full signatures. |
| zadatak-3-206-8 | 206 / 104 | PASS | Full high slur; detached mark below excluded. |
| zadatak-3-206-9 | 206 / 104 | PASS | Both systems and full slurs. |
| zadatak-3-206-10 | 206 / 104 | PASS | Full signatures, ornaments and slurs. |
| zadatak-3-206-7-realizacija | 206 / 104 | PASS | Full title, tonal labels, both systems and lowest stems. |

## Hand-off

1. **Assigned pages:** printed 175–206 / PDF 88–104, all 104 existing records.
2. **Files created:** only `review-candidates/book/M05/visual-review.json` and `review-candidates/book/M05/visual-review.md`. No crop, source, manifest, text draft, chapter, global file or milestone status edited; no commit/push.
3. **Examples extracted:** none by this reviewer. The existing set comprises 3.1–3.78, continuations on 186 and 201, exercises on 189–190 and 205–206, and realizations on 191 and 206. Every image's printed page is listed above and in JSON.
4. **Image review:** 64 PASS; 40 RECROP_REQUIRED = 2 tested safe recrops + 38 source-limited conflicts. **0 unreviewed.**
5. **Ambiguities/incompleteness:** faint handwritten analysis is not approved printed notation; no attempt made to decipher/retouch it. Page-190 exercises 7/8 have the explicit source collision described above. No other unreadable/incomplete printed example identified in this set.
6. **Integration readiness:** **NO.** Apply the two tested recrops through the assigned extractor/integrator, then review the resulting image files again. Resolve the 38 source-limited failures without clipping required content or retouching source ink; this review does not authorize an exception to the crop rules.
