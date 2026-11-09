# M05 — integration report

## Scope and disposition

- Printed pages **175–206** (32 pages); PDF pages **88–104** (17 spread pages, only assigned halves).
- Chapter: `chapters/03-kromatika-a.md`; root heading: `# 3. Kromatika i enharmonija`.
- **104/104 exact slot identities and printed pages matched in source order:** first text draft 50, second 54.
- **66 independent_pass**: 64 original independent passes plus independently approved applied recrops 3.2 (175) and 3.33 (188). These alone are embedded.
- **38 cleanup_required**: source-limited, visibly PROVISIONAL, linked only as unapproved source crops. No images were extracted or edited.
- Text review: **32/32 verified pages**; no unreadable prose reported.
- Ready for provisional integration, **not final acceptance or milestone completion**. The 38 image failures remain unresolved. No human approval requested or recorded.

## Inputs and authority

- `review-candidates/book/M05/text-175-190.md`
- `review-candidates/book/M05/text-191-206.md`
- `review-candidates/book/M05/text-175-190-review.json`
- `review-candidates/book/M05/text-191-206-review.json`
- `review-candidates/book/M05/images-corrected.json`
- `review-candidates/book/M05/visual-review.json`
- `review-candidates/book/M05/recrop-review.json`
- `sources/index.json` and `sources/pages/page-175.png` through `sources/pages/page-206.png`.

Independent approvals were inherited, not self-issued. The follow-up recrop review overrides only the two pending_recrop_review records in the new integrated manifest. Raw manifests and review evidence remain unchanged.

## Text preservation and boundaries

Only heading case and section-number spacing were normalized: the requested root heading, numbered subheadings 3.4 and 3.4.1–3.4.4, and ZADACI headings to Zadaci. Body text, bold run-in subheadings, quotations, attributions, diacritics, literal starred notes, footnote 5, Markdown footnote 6, printed typos and all source/continuation comments remain exactly as verified. Printed odosu, uobičajnom, and the page-194 reference to 3.45 before example 3.46 were not silently corrected.

Page 174 was opened directly and is blank: there is no initial prose continuation to import. At **190–191 no prose sentence exists to join**: page 190 ends the exercise sequence; page 191 is the separate realization of exercise 8. The verified boundary comment remains intact. Other prose continuations are preserved with their markers at 178–179, 184–185, 186–187, 195–196, 198–199 (dehyphenated promjene), and 202–203. Visual continuations 3.28 (186) and 3.67 (201) remain separate page-qualified slots with explicit e/f continuation captions. Both exercise series and both realizations retain distinct identities. Scope ends with the last realization on page 206.

## Validation performed

- 104 unique manifest IDs and 104 slots: exact identity + printed page + order, not just counts.
- **104/104 source-pixel matches** against source_image.crop(rect): identical mode, dimensions and complete decoded pixel bytes. No resampling, retouch, generated image or artificial border. Decoded-pixel SHA-256 recorded per image.
- Source image, printed page and PDF page match `sources/index.json` for all 104 records; dimensions match for all 32 sources. PDF = floor(printed_page/2)+1.
- All 32 source-page markers appear once in ascending order with correct PDF pages; 32 text-review records verified and cover exactly 175–206.
- Exactly **66 embeds, 38 PROVISIONAL link-only blocks, 104 captions and 104 MuseScore placeholders**. Every block retains its exact visual-slot comment, matching identity, alt/link text and printed page.
- Every image/crop link exists. All file references use complete repository-root-relative paths.
- Link resolution deliberately follows the repository's root-relative path convention, not the chapter directory. The 38 unapproved crops are ordinary links, never Markdown image embeds.
- Round-trip removal of only the 104 generated blocks recovers the two joined text drafts exactly after the documented heading-only normalization. Prose, footnotes and source/continuation comments survive losslessly.
- No image, raw manifest, shared tracker or unrelated work edited. No commit, push, delegation, model subprocess, API or GUI.

## Full 104-slot map and per-image results

Status independent_pass inherits independent PASS. Status cleanup_required retains independent RECROP_REQUIRED and is never embedded.

| Slot | Exact text slot | ID | Printed | PDF | Status | Image | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 3.1 | `primjer-3-1` | 175 | 88 | independent_pass | `images/03-kromatika-a/primjer-3-1.png` | `review-candidates/book/M05/visual-review.json` |
| 2 | 3.2 | `primjer-3-2` | 175 | 88 | independent_pass | `images/03-kromatika-a/recrops/primjer-3-2.png` | `review-candidates/book/M05/recrop-review.json` |
| 3 | 3.3 | `primjer-3-3` | 175 | 88 | cleanup_required | `images/03-kromatika-a/primjer-3-3.png` | `review-candidates/book/M05/visual-review.json` |
| 4 | 3.4 | `primjer-3-4` | 176 | 89 | cleanup_required | `images/03-kromatika-a/primjer-3-4.png` | `review-candidates/book/M05/visual-review.json` |
| 5 | 3.5 | `primjer-3-5` | 176 | 89 | cleanup_required | `images/03-kromatika-a/primjer-3-5.png` | `review-candidates/book/M05/visual-review.json` |
| 6 | 3.6 | `primjer-3-6` | 177 | 89 | cleanup_required | `images/03-kromatika-a/primjer-3-6.png` | `review-candidates/book/M05/visual-review.json` |
| 7 | 3.7 | `primjer-3-7` | 178 | 90 | cleanup_required | `images/03-kromatika-a/primjer-3-7.png` | `review-candidates/book/M05/visual-review.json` |
| 8 | 3.8 | `primjer-3-8` | 178 | 90 | cleanup_required | `images/03-kromatika-a/primjer-3-8.png` | `review-candidates/book/M05/visual-review.json` |
| 9 | 3.9 | `primjer-3-9` | 178 | 90 | cleanup_required | `images/03-kromatika-a/primjer-3-9.png` | `review-candidates/book/M05/visual-review.json` |
| 10 | 3.10 | `primjer-3-10` | 178 | 90 | cleanup_required | `images/03-kromatika-a/primjer-3-10.png` | `review-candidates/book/M05/visual-review.json` |
| 11 | 3.11 | `primjer-3-11` | 179 | 90 | cleanup_required | `images/03-kromatika-a/primjer-3-11.png` | `review-candidates/book/M05/visual-review.json` |
| 12 | 3.12 | `primjer-3-12` | 179 | 90 | cleanup_required | `images/03-kromatika-a/primjer-3-12.png` | `review-candidates/book/M05/visual-review.json` |
| 13 | 3.13 | `primjer-3-13` | 179 | 90 | cleanup_required | `images/03-kromatika-a/primjer-3-13.png` | `review-candidates/book/M05/visual-review.json` |
| 14 | 3.14 | `primjer-3-14` | 179 | 90 | cleanup_required | `images/03-kromatika-a/primjer-3-14.png` | `review-candidates/book/M05/visual-review.json` |
| 15 | 3.15 | `primjer-3-15` | 180 | 91 | cleanup_required | `images/03-kromatika-a/primjer-3-15.png` | `review-candidates/book/M05/visual-review.json` |
| 16 | 3.16 | `primjer-3-16` | 180 | 91 | cleanup_required | `images/03-kromatika-a/primjer-3-16.png` | `review-candidates/book/M05/visual-review.json` |
| 17 | 3.17 | `primjer-3-17` | 180 | 91 | cleanup_required | `images/03-kromatika-a/primjer-3-17.png` | `review-candidates/book/M05/visual-review.json` |
| 18 | 3.18 | `primjer-3-18` | 181 | 91 | independent_pass | `images/03-kromatika-a/primjer-3-18.png` | `review-candidates/book/M05/visual-review.json` |
| 19 | 3.19 | `primjer-3-19` | 182 | 92 | cleanup_required | `images/03-kromatika-a/primjer-3-19.png` | `review-candidates/book/M05/visual-review.json` |
| 20 | 3.20 | `primjer-3-20` | 183 | 92 | independent_pass | `images/03-kromatika-a/primjer-3-20.png` | `review-candidates/book/M05/visual-review.json` |
| 21 | 3.21 | `primjer-3-21` | 183 | 92 | cleanup_required | `images/03-kromatika-a/primjer-3-21.png` | `review-candidates/book/M05/visual-review.json` |
| 22 | 3.22 | `primjer-3-22` | 183 | 92 | cleanup_required | `images/03-kromatika-a/primjer-3-22.png` | `review-candidates/book/M05/visual-review.json` |
| 23 | 3.23 | `primjer-3-23` | 183 | 92 | cleanup_required | `images/03-kromatika-a/primjer-3-23.png` | `review-candidates/book/M05/visual-review.json` |
| 24 | 3.24 | `primjer-3-24` | 184 | 93 | cleanup_required | `images/03-kromatika-a/primjer-3-24.png` | `review-candidates/book/M05/visual-review.json` |
| 25 | 3.25 | `primjer-3-25` | 184 | 93 | cleanup_required | `images/03-kromatika-a/primjer-3-25.png` | `review-candidates/book/M05/visual-review.json` |
| 26 | 3.26 | `primjer-3-26` | 185 | 93 | cleanup_required | `images/03-kromatika-a/primjer-3-26.png` | `review-candidates/book/M05/visual-review.json` |
| 27 | 3.27 | `primjer-3-27` | 185 | 93 | cleanup_required | `images/03-kromatika-a/primjer-3-27.png` | `review-candidates/book/M05/visual-review.json` |
| 28 | 3.28 | `primjer-3-28` | 185 | 93 | cleanup_required | `images/03-kromatika-a/primjer-3-28.png` | `review-candidates/book/M05/visual-review.json` |
| 29 | 3.28 (nastavak: e, f) | `primjer-3-28-p186` | 186 | 94 | cleanup_required | `images/03-kromatika-a/primjer-3-28-p186.png` | `review-candidates/book/M05/visual-review.json` |
| 30 | 3.29 | `primjer-3-29` | 186 | 94 | cleanup_required | `images/03-kromatika-a/primjer-3-29.png` | `review-candidates/book/M05/visual-review.json` |
| 31 | 3.30 | `primjer-3-30` | 187 | 94 | independent_pass | `images/03-kromatika-a/primjer-3-30.png` | `review-candidates/book/M05/visual-review.json` |
| 32 | 3.31 | `primjer-3-31` | 187 | 94 | independent_pass | `images/03-kromatika-a/primjer-3-31.png` | `review-candidates/book/M05/visual-review.json` |
| 33 | 3.32 | `primjer-3-32` | 188 | 95 | cleanup_required | `images/03-kromatika-a/primjer-3-32.png` | `review-candidates/book/M05/visual-review.json` |
| 34 | 3.33 | `primjer-3-33` | 188 | 95 | independent_pass | `images/03-kromatika-a/recrops/primjer-3-33.png` | `review-candidates/book/M05/recrop-review.json` |
| 35 | 3.34 | `primjer-3-34` | 188 | 95 | cleanup_required | `images/03-kromatika-a/primjer-3-34.png` | `review-candidates/book/M05/visual-review.json` |
| 36 | 3.35 | `primjer-3-35` | 189 | 95 | cleanup_required | `images/03-kromatika-a/primjer-3-35.png` | `review-candidates/book/M05/visual-review.json` |
| 37 | 3.36 | `primjer-3-36` | 189 | 95 | cleanup_required | `images/03-kromatika-a/primjer-3-36.png` | `review-candidates/book/M05/visual-review.json` |
| 38 | ZADACI 2 | `zadatak-3-189-2` | 189 | 95 | independent_pass | `images/03-kromatika-a/zadatak-3-189-2.png` | `review-candidates/book/M05/visual-review.json` |
| 39 | ZADACI 3 | `zadatak-3-189-3` | 189 | 95 | independent_pass | `images/03-kromatika-a/zadatak-3-189-3.png` | `review-candidates/book/M05/visual-review.json` |
| 40 | ZADACI 4 | `zadatak-3-189-4` | 189 | 95 | independent_pass | `images/03-kromatika-a/zadatak-3-189-4.png` | `review-candidates/book/M05/visual-review.json` |
| 41 | ZADACI 5 | `zadatak-3-190-5` | 190 | 96 | independent_pass | `images/03-kromatika-a/zadatak-3-190-5.png` | `review-candidates/book/M05/visual-review.json` |
| 42 | ZADACI 6 | `zadatak-3-190-6` | 190 | 96 | independent_pass | `images/03-kromatika-a/zadatak-3-190-6.png` | `review-candidates/book/M05/visual-review.json` |
| 43 | ZADACI 7 | `zadatak-3-190-7` | 190 | 96 | cleanup_required | `images/03-kromatika-a/zadatak-3-190-7.png` | `review-candidates/book/M05/visual-review.json` |
| 44 | ZADACI 8 | `zadatak-3-190-8` | 190 | 96 | cleanup_required | `images/03-kromatika-a/zadatak-3-190-8.png` | `review-candidates/book/M05/visual-review.json` |
| 45 | ZADACI 9 | `zadatak-3-190-9` | 190 | 96 | independent_pass | `images/03-kromatika-a/zadatak-3-190-9.png` | `review-candidates/book/M05/visual-review.json` |
| 46 | ZADACI 10 | `zadatak-3-190-10` | 190 | 96 | independent_pass | `images/03-kromatika-a/zadatak-3-190-10.png` | `review-candidates/book/M05/visual-review.json` |
| 47 | ZADACI 11 | `zadatak-3-190-11` | 190 | 96 | independent_pass | `images/03-kromatika-a/zadatak-3-190-11.png` | `review-candidates/book/M05/visual-review.json` |
| 48 | ZADACI 12 | `zadatak-3-190-12` | 190 | 96 | independent_pass | `images/03-kromatika-a/zadatak-3-190-12.png` | `review-candidates/book/M05/visual-review.json` |
| 49 | ZADACI 13 | `zadatak-3-190-13` | 190 | 96 | independent_pass | `images/03-kromatika-a/zadatak-3-190-13.png` | `review-candidates/book/M05/visual-review.json` |
| 50 | ZADACI 14 | `zadatak-3-190-14` | 190 | 96 | independent_pass | `images/03-kromatika-a/zadatak-3-190-14.png` | `review-candidates/book/M05/visual-review.json` |
| 51 | Realizacija zadatka 8. | `zadatak-3-191-8-realizacija` | 191 | 96 | independent_pass | `images/03-kromatika-a/zadatak-3-191-8-realizacija.png` | `review-candidates/book/M05/visual-review.json` |
| 52 | 3.37 | `primjer-3-37` | 192 | 97 | cleanup_required | `images/03-kromatika-a/primjer-3-37.png` | `review-candidates/book/M05/visual-review.json` |
| 53 | 3.38 | `primjer-3-38` | 192 | 97 | cleanup_required | `images/03-kromatika-a/primjer-3-38.png` | `review-candidates/book/M05/visual-review.json` |
| 54 | 3.39 | `primjer-3-39` | 193 | 97 | cleanup_required | `images/03-kromatika-a/primjer-3-39.png` | `review-candidates/book/M05/visual-review.json` |
| 55 | 3.40 | `primjer-3-40` | 193 | 97 | cleanup_required | `images/03-kromatika-a/primjer-3-40.png` | `review-candidates/book/M05/visual-review.json` |
| 56 | 3.41 | `primjer-3-41` | 193 | 97 | cleanup_required | `images/03-kromatika-a/primjer-3-41.png` | `review-candidates/book/M05/visual-review.json` |
| 57 | 3.42 | `primjer-3-42` | 193 | 97 | cleanup_required | `images/03-kromatika-a/primjer-3-42.png` | `review-candidates/book/M05/visual-review.json` |
| 58 | 3.43 | `primjer-3-43` | 194 | 98 | independent_pass | `images/03-kromatika-a/primjer-3-43.png` | `review-candidates/book/M05/visual-review.json` |
| 59 | 3.44 | `primjer-3-44` | 194 | 98 | independent_pass | `images/03-kromatika-a/primjer-3-44.png` | `review-candidates/book/M05/visual-review.json` |
| 60 | 3.45 | `primjer-3-45` | 194 | 98 | independent_pass | `images/03-kromatika-a/primjer-3-45.png` | `review-candidates/book/M05/visual-review.json` |
| 61 | 3.46 | `primjer-3-46` | 194 | 98 | independent_pass | `images/03-kromatika-a/primjer-3-46.png` | `review-candidates/book/M05/visual-review.json` |
| 62 | 3.47 | `primjer-3-47` | 194 | 98 | independent_pass | `images/03-kromatika-a/primjer-3-47.png` | `review-candidates/book/M05/visual-review.json` |
| 63 | 3.48 | `primjer-3-48` | 195 | 98 | independent_pass | `images/03-kromatika-a/primjer-3-48.png` | `review-candidates/book/M05/visual-review.json` |
| 64 | 3.49 | `primjer-3-49` | 195 | 98 | independent_pass | `images/03-kromatika-a/primjer-3-49.png` | `review-candidates/book/M05/visual-review.json` |
| 65 | 3.50 | `primjer-3-50` | 195 | 98 | independent_pass | `images/03-kromatika-a/primjer-3-50.png` | `review-candidates/book/M05/visual-review.json` |
| 66 | 3.51 | `primjer-3-51` | 195 | 98 | independent_pass | `images/03-kromatika-a/primjer-3-51.png` | `review-candidates/book/M05/visual-review.json` |
| 67 | 3.52 | `primjer-3-52` | 195 | 98 | independent_pass | `images/03-kromatika-a/primjer-3-52.png` | `review-candidates/book/M05/visual-review.json` |
| 68 | 3.53 | `primjer-3-53` | 195 | 98 | independent_pass | `images/03-kromatika-a/primjer-3-53.png` | `review-candidates/book/M05/visual-review.json` |
| 69 | 3.54 | `primjer-3-54` | 196 | 99 | independent_pass | `images/03-kromatika-a/primjer-3-54.png` | `review-candidates/book/M05/visual-review.json` |
| 70 | 3.55 | `primjer-3-55` | 196 | 99 | independent_pass | `images/03-kromatika-a/primjer-3-55.png` | `review-candidates/book/M05/visual-review.json` |
| 71 | 3.56 | `primjer-3-56` | 196 | 99 | independent_pass | `images/03-kromatika-a/primjer-3-56.png` | `review-candidates/book/M05/visual-review.json` |
| 72 | 3.57 | `primjer-3-57` | 196 | 99 | independent_pass | `images/03-kromatika-a/primjer-3-57.png` | `review-candidates/book/M05/visual-review.json` |
| 73 | 3.58 | `primjer-3-58` | 196 | 99 | independent_pass | `images/03-kromatika-a/primjer-3-58.png` | `review-candidates/book/M05/visual-review.json` |
| 74 | 3.59 | `primjer-3-59` | 197 | 99 | independent_pass | `images/03-kromatika-a/primjer-3-59.png` | `review-candidates/book/M05/visual-review.json` |
| 75 | 3.60 | `primjer-3-60` | 197 | 99 | independent_pass | `images/03-kromatika-a/primjer-3-60.png` | `review-candidates/book/M05/visual-review.json` |
| 76 | 3.61 | `primjer-3-61` | 197 | 99 | independent_pass | `images/03-kromatika-a/primjer-3-61.png` | `review-candidates/book/M05/visual-review.json` |
| 77 | 3.62 | `primjer-3-62` | 198 | 100 | independent_pass | `images/03-kromatika-a/primjer-3-62.png` | `review-candidates/book/M05/visual-review.json` |
| 78 | 3.63 a–d | `primjer-3-63` | 199 | 100 | independent_pass | `images/03-kromatika-a/primjer-3-63.png` | `review-candidates/book/M05/visual-review.json` |
| 79 | 3.64 a–c | `primjer-3-64` | 199 | 100 | independent_pass | `images/03-kromatika-a/primjer-3-64.png` | `review-candidates/book/M05/visual-review.json` |
| 80 | 3.65 a–b | `primjer-3-65` | 200 | 101 | independent_pass | `images/03-kromatika-a/primjer-3-65.png` | `review-candidates/book/M05/visual-review.json` |
| 81 | 3.66 | `primjer-3-66` | 200 | 101 | independent_pass | `images/03-kromatika-a/primjer-3-66.png` | `review-candidates/book/M05/visual-review.json` |
| 82 | 3.67 a–d | `primjer-3-67` | 200 | 101 | independent_pass | `images/03-kromatika-a/primjer-3-67.png` | `review-candidates/book/M05/visual-review.json` |
| 83 | 3.67 e–f (nastavak) | `primjer-3-67-p201` | 201 | 101 | independent_pass | `images/03-kromatika-a/primjer-3-67-p201.png` | `review-candidates/book/M05/visual-review.json` |
| 84 | 3.68 a–c | `primjer-3-68` | 201 | 101 | independent_pass | `images/03-kromatika-a/primjer-3-68.png` | `review-candidates/book/M05/visual-review.json` |
| 85 | 3.69 | `primjer-3-69` | 201 | 101 | independent_pass | `images/03-kromatika-a/primjer-3-69.png` | `review-candidates/book/M05/visual-review.json` |
| 86 | 3.70 | `primjer-3-70` | 202 | 102 | independent_pass | `images/03-kromatika-a/primjer-3-70.png` | `review-candidates/book/M05/visual-review.json` |
| 87 | 3.71 a–e | `primjer-3-71` | 202 | 102 | independent_pass | `images/03-kromatika-a/primjer-3-71.png` | `review-candidates/book/M05/visual-review.json` |
| 88 | 3.72 a–b | `primjer-3-72` | 202 | 102 | independent_pass | `images/03-kromatika-a/primjer-3-72.png` | `review-candidates/book/M05/visual-review.json` |
| 89 | 3.73 | `primjer-3-73` | 203 | 102 | independent_pass | `images/03-kromatika-a/primjer-3-73.png` | `review-candidates/book/M05/visual-review.json` |
| 90 | 3.74 | `primjer-3-74` | 203 | 102 | independent_pass | `images/03-kromatika-a/primjer-3-74.png` | `review-candidates/book/M05/visual-review.json` |
| 91 | 3.75 | `primjer-3-75` | 203 | 102 | independent_pass | `images/03-kromatika-a/primjer-3-75.png` | `review-candidates/book/M05/visual-review.json` |
| 92 | 3.76 | `primjer-3-76` | 204 | 103 | independent_pass | `images/03-kromatika-a/primjer-3-76.png` | `review-candidates/book/M05/visual-review.json` |
| 93 | 3.77 a–f | `primjer-3-77` | 204 | 103 | independent_pass | `images/03-kromatika-a/primjer-3-77.png` | `review-candidates/book/M05/visual-review.json` |
| 94 | 3.78 a–d | `primjer-3-78` | 205 | 103 | independent_pass | `images/03-kromatika-a/primjer-3-78.png` | `review-candidates/book/M05/visual-review.json` |
| 95 | ZADACI 2 | `zadatak-3-205-2` | 205 | 103 | independent_pass | `images/03-kromatika-a/zadatak-3-205-2.png` | `review-candidates/book/M05/visual-review.json` |
| 96 | ZADACI 3 | `zadatak-3-205-3` | 205 | 103 | independent_pass | `images/03-kromatika-a/zadatak-3-205-3.png` | `review-candidates/book/M05/visual-review.json` |
| 97 | ZADACI 4 | `zadatak-3-205-4` | 205 | 103 | independent_pass | `images/03-kromatika-a/zadatak-3-205-4.png` | `review-candidates/book/M05/visual-review.json` |
| 98 | ZADACI 5 | `zadatak-3-205-5` | 205 | 103 | independent_pass | `images/03-kromatika-a/zadatak-3-205-5.png` | `review-candidates/book/M05/visual-review.json` |
| 99 | ZADACI 6 | `zadatak-3-205-6` | 205 | 103 | independent_pass | `images/03-kromatika-a/zadatak-3-205-6.png` | `review-candidates/book/M05/visual-review.json` |
| 100 | ZADACI 7 | `zadatak-3-206-7` | 206 | 104 | independent_pass | `images/03-kromatika-a/zadatak-3-206-7.png` | `review-candidates/book/M05/visual-review.json` |
| 101 | ZADACI 8 | `zadatak-3-206-8` | 206 | 104 | independent_pass | `images/03-kromatika-a/zadatak-3-206-8.png` | `review-candidates/book/M05/visual-review.json` |
| 102 | ZADACI 9 | `zadatak-3-206-9` | 206 | 104 | independent_pass | `images/03-kromatika-a/zadatak-3-206-9.png` | `review-candidates/book/M05/visual-review.json` |
| 103 | ZADACI 10 | `zadatak-3-206-10` | 206 | 104 | independent_pass | `images/03-kromatika-a/zadatak-3-206-10.png` | `review-candidates/book/M05/visual-review.json` |
| 104 | Realizacija zadatka 7. | `zadatak-3-206-7-realizacija` | 206 | 104 | independent_pass | `images/03-kromatika-a/zadatak-3-206-7-realizacija.png` | `review-candidates/book/M05/visual-review.json` |

## All 38 unresolved source-limited issues

A clean rectangular solution preserving all required content was not established by the independent reviewer. Do not paint out handwriting, clip required notation, or add borders. A suitable unmarked source and renewed extraction/review are needed where embedded foreign ink cannot be excluded by cropping. These are image-cleanliness failures, not unreadable prose. Specific reasons are retained unchanged below.

- `primjer-3-3` — printed 175, PDF 88: Pencil harmonic annotations remain between the Brahms attribution and score and within the example bounds; excluding them rectangularly would lose required attribution or notation.
- `primjer-3-4` — printed 176, PDF 89: Faint pencil traces overlap and extend below the bass-staff area of the a-d example. A clean rectangle cannot exclude embedded writing while retaining the complete staves.
- `primjer-3-5` — printed 176, PDF 89: Faint source pencil marks occur inside and below the score, including bass-staff regions; complete a-d notation cannot be retained in a handwriting-free rectangle.
- `primjer-3-6` — printed 177, PDF 89: Handwritten harmonic marks between the staves remain inside the a-g example. They cannot be removed by adjusting outer crop edges.
- `primjer-3-7` — printed 178, PDF 90: Partial handwritten marks at the left of the lower system remain inside the horizontal bounds needed for number 3.7. Moving left edge past the writing would clip the number; all a-h variants must remain.
- `primjer-3-8` — printed 178, PDF 90: Source handwriting remains within and below the two systems. The very tight lower boundary also requires care against the following example's labels; no clean complete rectangular solution established.
- `primjer-3-9` — printed 178, PDF 90: Handwritten analysis above/below the a-e score is retained; lower handwritten marks occupy the same vertical range needed by the lowest printed notes. No clean rectangular solution.
- `primjer-3-10` — printed 178, PDF 90: Pencil analysis is visible above and beneath the a-d score, inside the necessary printed-content bounds. Removing it by crop would discard required labels/notation.
- `primjer-3-11` — printed 179, PDF 90: Handwritten chord names sit alongside the a-c labels and additional pencil figures remain below the notes; required labels/lowest notation prevent a clean rectangular crop.
- `primjer-3-12` — printed 179, PDF 90: Pencil chord names share the a-e label band and handwritten analysis remains below the score. Embedded foreign source ink cannot be removed by rectangular cropping.
- `primjer-3-13` — printed 179, PDF 90: Top edge includes fragments of preceding prose as well as handwritten chord names at the variant-label height. Trimming prose alone does not remove the embedded handwriting without losing labels.
- `primjer-3-14` — printed 179, PDF 90: Pencil C and other analysis occupy the upper band also required by the Wagner: Parsifal attribution. A trial lower top edge clipped the attribution and was rejected; no safe rectangle proposed.
- `primjer-3-15` — printed 180, PDF 91: Pencil harmonic annotations remain within the two-variant example, including the lower printed-analysis band. A handwriting-free rectangle would lose required analysis/notation.
- `primjer-3-16` — printed 180, PDF 91: Handwritten chord names occur beside the a/b labels and pencil analysis remains in the lower score area. Required labels and notation enclose the writing.
- `primjer-3-17` — printed 180, PDF 91: Handwritten analysis is retained at attribution height and between the Liszt attribution and staves; preserving the printed title and full score encloses the foreign ink.
- `primjer-3-19` — printed 182, PDF 92: Pencil chord names/analysis occur above and between the three systems containing a-f; the intermediate writing cannot be excluded with an outer rectangle.
- `primjer-3-21` — printed 183, PDF 92: Handwritten analysis is visible within the two-staff example and alongside the lower printed functions. It lies inside the bounds needed for complete a/b notation.
- `primjer-3-22` — printed 183, PDF 92: Pencil chord names and harmonic figures occupy the upper and inter-system bands of the multi-system example. Rectangular cropping cannot separate them from the complete intended example.
- `primjer-3-23` — printed 183, PDF 92: Handwritten chord names share the a/b label band; foreign marks are retained near the tightly adjacent preceding analysis. No complete handwriting-free rectangle established.
- `primjer-3-24` — printed 184, PDF 93: Pencil chord names and lower annotations remain inside the complete a/b score's bounds; adjusting outer edges cannot remove all writing while retaining labels and functions.
- `primjer-3-25` — printed 184, PDF 93: Handwritten chord analysis appears at the a/b label height and beneath the staves, within the necessary printed-content rectangle.
- `primjer-3-26` — printed 185, PDF 93: Pencil analysis occupies the a/b label band and the lower printed-function area. The close 3.26/3.27 boundary cannot solve embedded handwriting by trimming.
- `primjer-3-27` — printed 185, PDF 93: Top contains handwritten analysis and a fragment of the preceding example's lowest printed function. Embedded pencil marks remain even if that foreign printed fragment is trimmed.
- `primjer-3-28` — printed 185, PDF 93: Pencil chord names and analysis remain in upper, inter-system and lower bands of variants a-d; a complete clean rectangle is impossible without losing printed material.
- `primjer-3-28-p186` — printed 186, PDF 94: Continuation e/f and Bach chorale attribution are present, but extensive pencil analysis occupies the label/title band and areas between/below the staves. No clean rectangle.
- `primjer-3-29` — printed 186, PDF 94: Handwritten analysis remains above, between and below the two systems containing a-c; intermediate marks cannot be removed by changing outside bounds.
- `primjer-3-32` — printed 188, PDF 95: Top includes preceding prose fragments; handwritten chord names/analysis also remain in the upper and inter-system bands. Removing prose alone cannot create a handwriting-free complete crop.
- `primjer-3-34` — printed 188, PDF 95: Pencil chord names and analysis remain above and within/below the score. Embedded marks in the staff region prevent a safe handwriting-free rectangle.
- `primjer-3-35` — printed 189, PDF 95: Handwritten analysis below the bass shares the vertical band required by the lowest down-stems. Trimming that band to remove writing would truncate required notation.
- `primjer-3-36` — printed 189, PDF 95: Handwritten chord names share the a/b label/bracket band and further pencil analysis remains between and below systems; no clean complete rectangular crop.
- `zadatak-3-190-7` — printed 190, PDF 96: Bottom edge truncates the lowest figured-bass marks. Enlarged source strip y=680..755 shows the lowest figures interleaving vertically with the highest slur of exercise 8 around y=720; extending the rectangle includes the neighbouring slur. No safe complete single rectangle established.
- `zadatak-3-190-8` — printed 190, PDF 96: Top retains partial lowest figures from exercise 7. Those figures extend into the vertical band needed to retain exercise 8's complete highest slur; moving the top far enough down removes required slur ink. Source-tested conflict, not a retouch/clipping solution.
- `primjer-3-37` — printed 192, PDF 97: Pencil chord names occupy the upper score band and handwritten figures remain beside the printed lower function; complete number/staves/function enclose the writing.
- `primjer-3-38` — printed 192, PDF 97: Pencil chord names are retained above the staves and handwritten analysis shares the lower printed-function band. No clean complete rectangle.
- `primjer-3-39` — printed 193, PDF 97: Handwritten chord names above the score and pencil marks beside the lower D/IV analysis remain within the required printed-content bounds.
- `primjer-3-40` — printed 193, PDF 97: Handwriting shares the printed E-c title band and remains near the lower analysis; removing it rectangularly would lose required printed content.
- `primjer-3-41` — printed 193, PDF 97: Handwritten chord names share the H-es heading band, with further pencil marks in the analysis area; the complete intended score cannot fit a clean rectangle.
- `primjer-3-42` — printed 193, PDF 97: Extensive handwritten chord names/figures remain above and beneath the staves, including the required heading/analysis bands. No safe rectangular removal.

## Files created and hand-off

- `chapters/03-kromatika-a.md`
- `images/03-kromatika-a/REVIEW.md`
- `review-candidates/book/M05/images-integrated.json`
- `review-candidates/book/M05/INTEGRATION.md`

Ready for provisional integration: **yes**. Ready for final image acceptance or milestone completion: **no**, pending 38 cleanup-required crops and independent re-review. No content beyond printed page 206 was integrated.
