# M08 — bounded integration hand-off

## Outcome and assigned scope

Integrated **printed pages 277–308 inclusive (32 pages), PDF pages 139–155 (1-based)**. Work stops at 308. No image files, raw manifests, source pixels, global trackers, commits, or pushes changed. M08 is **not complete / not ready for final approval**: 22 crop-cleanup holds and 2 source-damage notation holds remain. No human approval was requested or implied.

## Files created

- [chapters/04-neakordicki-a.md](../../../chapters/04-neakordicki-a.md)
- [images/04-neakordicki-a/REVIEW.md](../../../images/04-neakordicki-a/REVIEW.md)
- [review-candidates/book/M08/images-integrated.json](images-integrated.json)
- [review-candidates/book/M08/INTEGRATION.md](INTEGRATION.md)

## Verified text and preservation

- [text-277-292.md](text-277-292.md)
- [text-277-292-review.json](text-277-292-review.json)
- [text-293-308.md](text-293-308.md)
- [text-293-308-review.json](text-293-308-review.json)

Both text workers report visual verification against all 32 source PNGs; neither claims a separate independent text review. Integration does not invent such an approval. No unreadable prose was reported. Exact candidate prose, headings, punctuation, footnotes, continuation comments and source-page markers were retained without normalization changes. The single chapter-4 root and existing section/subsection/exercise hierarchy remain intact. Footnote 7, the asterisk note on 286, and both full notes on 304 remain. Cross-page prose on 278/279 and 284/285 and all score continuations remain in order.

The source boundary comment saying page 293 was outside the *first text worker's* range remains unchanged as provenance; it is not the integrated chapter's endpoint. The following candidate explicitly continues at 293. The final boundary is 308/309, with complete realization on 308; 309 was not integrated.

All 105 visual slots retain their original identity, page and source-position comments. The 49 first-candidate slots and 56 second-candidate slots map one-to-one to the complete corrected 105-record inventory, not the obsolete 103-record raw inventory. The unnumbered progression on 277 and figured appoggiatura symbol in note ** on 304 are inline at their original positions. Their captions, source pages and MuseScore placeholders follow their containing paragraphs. The comma immediately following the progression remains intact. No printed example number is invented for either graphic. Every visual, including unapproved links, has its own actual source-page caption and MuseScore placeholder. Continuation labels are editorial identities, not claims of a repeated printed number.

## Independent image decisions

**81 independent_pass, 22 cleanup_required, 2 source_damage.** Approved images alone are embedded. Unapproved images remain visible, explicitly labelled source-crop links, never silently omitted or shown as approved scores. All links in Markdown are relative to the containing Markdown file; chapter image links use ../images/.

visual-review.json has 82 crop PASS decisions including two source-limited damaged sources, leaving 80 unqualified approvals. recrop-review.json independently passes only 4.z307-3 at its corrected path and rectangle [232,355,1742,1071], yielding 81 unqualified approvals. This supersedes the stale pending_recrop_review field only in the integrated manifest, not the raw input. The blocked coverage-recrop for 4.z303-3 remains cleanup_required.

- [Independent visual review](visual-review.json)
- [Independent page-307 recrop review](recrop-review.json)
- [Detailed review and all failure reasons](../../../images/04-neakordicki-a/REVIEW.md)

### Accepted replacement paths (independently passed only)

- `4.13` (printed 283): [images/04-neakordicki-a/primjer-4-13-coverage-recrop.png](../../../images/04-neakordicki-a/primjer-4-13-coverage-recrop.png).
- `4.z289-9-realizacija` (printed 289): [images/04-neakordicki-a/zadatak-4-289-9-realizacija-naslov-recrop.png](../../../images/04-neakordicki-a/zadatak-4-289-9-realizacija-naslov-recrop.png).
- `4.z294-5-realizacija` (printed 294): [images/04-neakordicki-a/zadatak-4-294-5-realizacija-naslov-recrop.png](../../../images/04-neakordicki-a/zadatak-4-294-5-realizacija-naslov-recrop.png).
- `4.z297-3-realizacija` (printed 297): [images/04-neakordicki-a/zadatak-4-297-3-realizacija-naslov-recrop.png](../../../images/04-neakordicki-a/zadatak-4-297-3-realizacija-naslov-recrop.png).
- `4.z303-3-realizacija` (printed 303): [images/04-neakordicki-a/zadatak-4-303-3-realizacija-naslov-recrop.png](../../../images/04-neakordicki-a/zadatak-4-303-3-realizacija-naslov-recrop.png).
- `4.z306-1` (printed 306): [images/04-neakordicki-a/zadatak-4-306-1-coverage-recrop.png](../../../images/04-neakordicki-a/zadatak-4-306-1-coverage-recrop.png).
- `4.z306-2` (printed 306): [images/04-neakordicki-a/zadatak-4-306-2-coverage-recrop.png](../../../images/04-neakordicki-a/zadatak-4-306-2-coverage-recrop.png).
- `4.z307-3` (printed 307): [images/04-neakordicki-a/recrops/zadatak-4-307-3.png](../../../images/04-neakordicki-a/recrops/zadatak-4-307-3.png).
- `4.z308-3-realizacija` (printed 308): [images/04-neakordicki-a/zadatak-4-308-3-realizacija-naslov-recrop.png](../../../images/04-neakordicki-a/zadatak-4-308-3-realizacija-naslov-recrop.png).

### Distinct source-damage holds — NOT approved notation

1. **4.z290-9-realizacija-cont**, printed 290 / PDF 146: white abrasion in the lower staff of the first system near its second measure; additional worn ink by the next system's left side. Exact affected notation is uncertified.
2. **4.31**, printed 295 / PDF 148: white abrasion in variant c's upper staff. Missing/worn notation is uncertified.

Both retain `status: source_damage`, `approved: false`, and `crop_review_status: independent_pass`. Boundary approval is not notation approval. Chapter warnings read **SOURCE DAMAGE / NOTATION UNCERTAIN — NEODOBRENO** and link to untouched source crops. Independent notation interpretation or an undamaged source is needed; no reconstruction is asserted.

### Cleanup holds

22 entries remain **PROVISIONAL — NEODOBRENO**. Most have source handwriting within the intended score rectangle; on page 303 the exercise-2 figures and exercise-3 slur overlap vertically. The reviewer proposed no safe rectangular replacement for these. Cleanup_required is an unresolved workflow status, not permission to erase, paint, synthesize margins or retouch original pixels.

## Validation results

- 105/105 slots match corrected-inventory identity, printed page, slot-source file and exact original slot line; 49 + 56 slots preserved.
- Exact byte-for-byte text round-trip after removing only integration insertions: PASS. No verified prose, punctuation, headings, footnotes, continuation comments or source markers lost.
- Exactly 32 source-page markers: printed 277–308, each matching sources/index.json; PDF mapping 139–155 (1-based).
- 105/105 crop files decode pixel-identically in RGB to their exact authoritative source rectangles; no border generation, resampling or retouching. Pixel identity alone does not remove source damage or constitute crop approval.
- 81 image embeds, 24 explicitly unapproved source-crop links, 105 slot-status markers, 105 captions and 105 MuseScore placeholders.
- Two inline graphics remain inside their containing paragraphs; captions/placeholders follow those paragraphs. No added printed numbers.
- All local Markdown links resolve relative to the containing file. Existing source and image files were read only.
- SHA-256 of each integrated image recorded in images-integrated.json for provenance; the authoritative rectangles remain in that manifest.

## Full 105-slot map (including actual printed source pages)

| Slot | Identitet / izvorna oznaka | Tiskana / PDF str. | Status | Izrez |
| --- | --- | --- | --- | --- |
| 001 | `progresija-277` — nenumerirana harmonijska progresija u odlomku o zaostajalicama | 277 / 139 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/progresija-277.png) |
| 002 | `4.1` — 4.1 a–b | 277 / 139 | `cleanup_required` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-1.png) |
| 003 | `4.1-c` — 4.1 c (nastavak) | 278 / 140 | `cleanup_required` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-1-c.png) |
| 004 | `4.2` — 4.2 | 278 / 140 | `cleanup_required` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-2.png) |
| 005 | `4.3` — 4.3 | 280 / 141 | `cleanup_required` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-3.png) |
| 006 | `4.4` — 4.4 | 281 / 141 | `cleanup_required` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-4.png) |
| 007 | `4.5` — 4.5 | 281 / 141 | `cleanup_required` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-5.png) |
| 008 | `4.6` — 4.6 | 282 / 142 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-6.png) |
| 009 | `4.7` — 4.7 | 282 / 142 | `cleanup_required` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-7.png) |
| 010 | `4.8` — 4.8 | 282 / 142 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-8.png) |
| 011 | `4.9` — 4.9 | 282 / 142 | `cleanup_required` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-9.png) |
| 012 | `4.10` — 4.10 | 283 / 142 | `cleanup_required` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-10.png) |
| 013 | `4.11` — 4.11 | 283 / 142 | `cleanup_required` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-11.png) |
| 014 | `4.12` — 4.12 | 283 / 142 | `cleanup_required` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-12.png) |
| 015 | `4.13` — 4.13 | 283 / 142 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-13-coverage-recrop.png) |
| 016 | `4.14` — 4.14 | 284 / 143 | `cleanup_required` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-14.png) |
| 017 | `4.15` — 4.15 | 284 / 143 | `cleanup_required` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-15.png) |
| 018 | `4.16` — 4.16 | 284 / 143 | `cleanup_required` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-16.png) |
| 019 | `4.17` — 4.17 | 285 / 143 | `cleanup_required` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-17.png) |
| 020 | `4.18` — 4.18 | 285 / 143 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-18.png) |
| 021 | `4.19` — 4.19 | 286 / 144 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-19.png) |
| 022 | `4.20` — 4.20 | 286 / 144 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-20.png) |
| 023 | `4.21` — 4.21 a–c | 286 / 144 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-21.png) |
| 024 | `4.21-cont` — 4.21 d–f (nastavak) | 287 / 144 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-21-cont.png) |
| 025 | `4.z287-1` — zadatak 1 | 287 / 144 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-287-1.png) |
| 026 | `4.z287-2` — zadatak 2 | 287 / 144 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-287-2.png) |
| 027 | `4.z287-3` — zadatak 3 (početak) | 287 / 144 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-287-3.png) |
| 028 | `4.z288-3-cont` — zadatak 3 (nastavak) | 288 / 145 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-288-3-cont.png) |
| 029 | `4.z288-4` — zadatak 4 | 288 / 145 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-288-4.png) |
| 030 | `4.z288-5` — zadatak 5 | 288 / 145 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-288-5.png) |
| 031 | `4.z288-6` — zadatak 6 | 288 / 145 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-288-6.png) |
| 032 | `4.z288-7` — zadatak 7 | 288 / 145 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-288-7.png) |
| 033 | `4.z288-8` — zadatak 8 | 288 / 145 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-288-8.png) |
| 034 | `4.z289-9` — zadatak 9 | 289 / 145 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-289-9.png) |
| 035 | `4.z289-10` — zadatak 10 | 289 / 145 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-289-10.png) |
| 036 | `4.z289-11` — zadatak 11 | 289 / 145 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-289-11.png) |
| 037 | `4.z289-12` — zadatak 12 | 289 / 145 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-289-12.png) |
| 038 | `4.z289-13` — zadatak 13 | 289 / 145 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-289-13.png) |
| 039 | `4.z289-9-realizacija` — Realizacija zadatka 9 (početak) | 289 / 145 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-289-9-realizacija-naslov-recrop.png) |
| 040 | `4.z290-9-realizacija-cont` — Realizacija zadatka 9 (nastavak) | 290 / 146 | `source_damage` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-290-9-realizacija-cont.png) |
| 041 | `4.22` — 4.22 | 290 / 146 | `cleanup_required` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-22.png) |
| 042 | `4.23` — 4.23 | 291 / 146 | `cleanup_required` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-23.png) |
| 043 | `4.24` — 4.24 | 291 / 146 | `cleanup_required` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-24.png) |
| 044 | `4.25` — 4.25 | 291 / 146 | `cleanup_required` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-25.png) |
| 045 | `4.26` — 4.26 | 291 / 146 | `cleanup_required` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-26.png) |
| 046 | `4.27` — 4.27 | 292 / 147 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-27.png) |
| 047 | `4.28` — 4.28 | 292 / 147 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-28.png) |
| 048 | `4.29` — 4.29 | 292 / 147 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-29.png) |
| 049 | `4.30` — 4.30 | 292 / 147 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-30.png) |
| 050 | `4.z293-1` — 4.1.3 — zadatak 1 | 293 / 147 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-293-1.png) |
| 051 | `4.z293-2` — 4.1.3 — zadatak 2 | 293 / 147 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-293-2.png) |
| 052 | `4.z293-3` — 4.1.3 — zadatak 3 | 293 / 147 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-293-3.png) |
| 053 | `4.z293-4` — 4.1.3 — zadatak 4 | 293 / 147 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-293-4.png) |
| 054 | `4.z293-5` — 4.1.3 — zadatak 5 | 293 / 147 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-293-5.png) |
| 055 | `4.z293-6` — 4.1.3 — zadatak 6 (početak) | 293 / 147 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-293-6.png) |
| 056 | `4.z294-6-cont` — 4.1.3 — zadatak 6 (nastavak) | 294 / 148 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-294-6-cont.png) |
| 057 | `4.z294-7` — 4.1.3 — zadatak 7 | 294 / 148 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-294-7.png) |
| 058 | `4.z294-5-realizacija` — 4.1.3 — Realizacija zadatka 5 | 294 / 148 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-294-5-realizacija-naslov-recrop.png) |
| 059 | `4.31` — 4.31 a–d | 295 / 148 | `source_damage` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-31.png) |
| 060 | `4.32` — 4.32 a–c | 295 / 148 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-32.png) |
| 061 | `4.33` — 4.33 a–c | 295 / 148 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-33.png) |
| 062 | `4.34` — 4.34 a–c | 295 / 148 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-34.png) |
| 063 | `4.35` — 4.35 a–e | 296 / 149 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-35.png) |
| 064 | `4.z296-1` — 4.1.4 — zadatak 1 | 296 / 149 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-296-1.png) |
| 065 | `4.z296-2` — 4.1.4 — zadatak 2 | 296 / 149 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-296-2.png) |
| 066 | `4.z297-3` — 4.1.4 — zadatak 3 | 297 / 149 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-297-3.png) |
| 067 | `4.z297-4` — 4.1.4 — zadatak 4 | 297 / 149 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-297-4.png) |
| 068 | `4.z297-3-realizacija` — 4.1.4 — Realizacija zadatka 3 | 297 / 149 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-297-3-realizacija-naslov-recrop.png) |
| 069 | `4.36` — 4.36 a–d | 298 / 150 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-36.png) |
| 070 | `4.37` — 4.37 a–b | 298 / 150 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-37.png) |
| 071 | `4.z298-1` — 4.1.5 — zadatak 1 (početak) | 298 / 150 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-298-1.png) |
| 072 | `4.z299-1-cont` — 4.1.5 — zadatak 1 (nastavak) | 299 / 150 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-299-1-cont.png) |
| 073 | `4.z299-2` — 4.1.5 — zadatak 2 | 299 / 150 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-299-2.png) |
| 074 | `4.38` — 4.38 a–f | 299 / 150 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-38.png) |
| 075 | `4.39` — 4.39 a–c | 300 / 151 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-39.png) |
| 076 | `4.40` — 4.40 a–b | 300 / 151 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-40.png) |
| 077 | `4.41` — 4.41 a–e | 300 / 151 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-41.png) |
| 078 | `4.42` — 4.42 a–d | 301 / 151 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-42.png) |
| 079 | `4.43` — 4.43 a–d | 301 / 151 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-43.png) |
| 080 | `4.44` — 4.44 a–d | 301 / 151 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-44.png) |
| 081 | `4.45` — 4.45 a–d | 302 / 152 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-45.png) |
| 082 | `4.z302-1` — 4.1.6 — zadatak 1 | 302 / 152 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-302-1.png) |
| 083 | `4.z302-2` — 4.1.6 — zadatak 2 (početak) | 302 / 152 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-302-2.png) |
| 084 | `4.z303-2-cont` — 4.1.6 — zadatak 2 (nastavak) | 303 / 152 | `cleanup_required` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-303-2-cont.png) |
| 085 | `4.z303-3` — 4.1.6 — zadatak 3 | 303 / 152 | `cleanup_required` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-303-3-coverage-recrop.png) |
| 086 | `4.z303-4` — 4.1.6 — zadatak 4 | 303 / 152 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-303-4.png) |
| 087 | `4.z303-5` — 4.1.6 — zadatak 5 | 303 / 152 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-303-5.png) |
| 088 | `4.z303-6` — 4.1.6 — zadatak 6 | 303 / 152 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-303-6.png) |
| 089 | `4.z303-3-realizacija` — 4.1.6 — Realizacija zadatka 3 (početak) | 303 / 152 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-303-3-realizacija-naslov-recrop.png) |
| 090 | `4.z304-3-realizacija-cont` — 4.1.6 — Realizacija zadatka 3 (nastavak; oznake * i **) | 304 / 153 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-304-3-realizacija-cont.png) |
| 091 | `sifra-appoggiature-304` — 4.1.6 — šifra trostruke appoggiature u bilješci ** (9/7/4 > 8/3) | 304 / 153 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/sifra-appoggiature-304.png) |
| 092 | `4.46` — 4.46 a–h, itd. | 304 / 153 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-46.png) |
| 093 | `4.47` — 4.47 a–b | 305 / 153 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-47.png) |
| 094 | `4.48` — 4.48 a–b | 305 / 153 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-48.png) |
| 095 | `4.49` — 4.49 a–b | 305 / 153 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-49.png) |
| 096 | `4.50` — 4.50 a–b | 305 / 153 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-50.png) |
| 097 | `4.51` — 4.51 a–b | 306 / 154 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-51.png) |
| 098 | `4.52` — 4.52 — (Chopin: Mazurka op. 63 br. 1) | 306 / 154 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/primjer-4-52.png) |
| 099 | `4.z306-1` — 4.1.7 — zadatak 1 | 306 / 154 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-306-1-coverage-recrop.png) |
| 100 | `4.z306-2` — 4.1.7 — zadatak 2 (početak) | 306 / 154 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-306-2-coverage-recrop.png) |
| 101 | `4.z307-2-cont` — 4.1.7 — zadatak 2 (nastavak) | 307 / 154 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-307-2-cont.png) |
| 102 | `4.z307-3` — 4.1.7 — zadatak 3 | 307 / 154 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/recrops/zadatak-4-307-3.png) |
| 103 | `4.z307-4` — 4.1.7 — zadatak 4 | 307 / 154 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-307-4.png) |
| 104 | `4.z307-5` — 4.1.7 — zadatak 5 | 307 / 154 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-307-5.png) |
| 105 | `4.z308-3-realizacija` — 4.1.7 — Realizacija zadatka 3 | 308 / 155 | `independent_pass` | [izvorni izrez](../../../images/04-neakordicki-a/zadatak-4-308-3-realizacija-naslov-recrop.png) |

## Execution boundary

Completed by one integration worker using local file operations and validation only. No delegation, model subprocess, external API, GUI, image modification, raw-manifest update, global-tracker update, commit or push was performed. Existing unrelated working-tree changes were left untouched.

## Ready for integration?

The bounded integration artifacts and link/pixel/text validations are ready for hand-off. **Not ready for milestone completion or final publication approval.** Resolve all 22 cleanup holds and 2 source-damage notation holds, and obtain any additionally required independent text review before claiming completion.
