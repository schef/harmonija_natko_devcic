# M07 — independent review of four corrected crops

**All four corrected crops PASS.** Counts: **4 PASS, 0 RECROP_REQUIRED, 0 source-limited, 0 unreviewed.**

Scope was limited to the four `pending_recrop_review` entries in `review-candidates/book/M07/images-corrected.json`. Reopened every current recrop and authoritative source page, inspecting all four crop edges at native resolution. Independently verified dimensions and exact decoded RGB source pixels for **4/4**, and checked image/printed-page/1-based PDF mappings against `sources/index.json` for **4/4**.

| ID | Image (repository-root relative) | Printed / PDF page | Decision | Result |
| --- | --- | --- | --- | --- |
| M07-06 | `images/03-kromatika-c/recrops/primjer-3-181.png` | 259 / 130 | PASS | Complete number 3.181, a–d, both systems and all figures. Lowest `(D)` fully restored with genuine lower margin. Following prose footnote excluded. |
| M07-27 | `images/03-kromatika-c/recrops/zadatak-3-8-9.png` | 265 / 133 | PASS | Exercise 9, both systems and all notation/slurs retained; lower treble-clef curl restored, with genuine whitespace below. Adjacent exercises excluded. |
| M07-44 | `images/03-kromatika-c/recrops/zadatak-3-9-3.png` | 271 / 136 | PASS | Exercise 3, full clef, signatures, long slur and all notes retained; lower curl and white margin restored. Tight genuine top separation excludes exercise 2 figures. |
| M07-45 | `images/03-kromatika-c/recrops/zadatak-3-9-4.png` | 271 / 136 | PASS | Exercise 4 and both systems complete; lower-system clef curl restored with genuine white margin. Adjacent exercises excluded. |

For each image, top/bottom/left/right edges are clean, staff ends and lowest stems intact, and feasible genuine source-white margins present. No prose, page numbers, neighbouring staff fragments, partial foreign lettering or handwriting is visible. Numbers and all printed labels are present as in the source; no attribution or realization title is printed with these four examples to retain. Manifest captions, filenames and printed-page references agree. No further rectangle is proposed (`proposed_rect: null`); all four records have `source_limited: false`.

## Hand-off

- Reviewed printed pages **259, 265, 271**; PDF pages **130, 133, 136 (1-based)**.
- Created only `review-candidates/book/M07/recrop-review.json` and `review-candidates/book/M07/recrop-review.md`.
- No musical examples extracted or image/manifest/chapter/tracker edits performed. No retouching, delegation, model subprocess/API calls, GUI, commits or pushes.
- No unreadable or ambiguous printed content found in these four crops.
- **These four recrops are ready for integration.** This does not mark M07 complete: the earlier 17 source-limited failures remain outside this bounded re-review. Final Markdown embedding/alt text/MuseScore checks remain integration responsibilities.
