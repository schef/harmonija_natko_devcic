# Whole-book preparation checkpoint

## Resumed with a revised usage guard

The previous preparation phase paused at **51% weekly remaining**, just above
the former 50% cutoff. On **2026-11-22** the user requested continuation with
**one active subagent maximum** and a revised stopping point of **20% weekly
allowance remaining on the active account**. On 2026-11-23 the user lowered the
current cutoff to **3% weekly remaining on the active account** for review-workflow
improvements before the reset. This supersedes 20%; one active subagent maximum
still applies. The initial resumed check reported
69% weekly remaining on Account 1. Check limits between bounded tasks; do not
start nested agents or model subprocesses.

**Preparation coverage is complete through printed page 411; human review is ready.**
Final hand-off and validation: `review-candidates/book/PREPARATION-COMPLETE.md`.
This is **not publication readiness or milestone acceptance**. Do not mark milestones complete
merely because text and image placeholders have been integrated.

## Completed preparation and independent review

Verified text is provisionally integrated from printed page 47 through 411.
The previously approved work through page 46 is preserved.

| Milestone | Printed pages | PDF pages | Prepared parts | Independent pass | Cleanup required |
| --- | --- | --- | ---: | ---: | ---: |
| M02 remainder | 47–63 | 24–32 | 69 | 49 | 20 |
| M03 | 64–136 | 33–69 | 310 | 158 | 152 |
| M04 | 137–174 | 69–88 | 128 | 107 | 21 |
| M05 | 175–206 | 88–104 | 104 | 66 | 38 |
| M06 | 207–256 | 104–129 | 169 | 142 | 27 |
| M07 | 257–276 | 129–139 | 57 | 40 | 17 |
| M08 | 277–308 | 139–155 | 105 | 81 | 22, plus 2 source-damage holds |
| M09 | 309–348 | 155–175 | 134 | 111 | 23 |
| M10 | 349–378 | 175–190 | 86 | 80 | 5, plus 1 source-damage hold |
| M11 | 379–411 | 190–206 | 44 | 36 | 8 |
| **Reviewed total** | **47–411** | **24–206** | **1,206** | **870** | **333, plus 3 source-damage holds** |

Each reviewed image has an independent per-image decision. Feasible boundary
corrections were generated as separate source-only recrops and independently
re-reviewed; originals were not overwritten. Source-limited crops remain
explicitly provisional links, not approved embedded images. No unattended
handwriting removal or generated borders were used.

The 333 cleanup cases include internal pencil annotations, adjacent visual/prose
overlap, and other source-layout constraints. They require a separate cleanup
or source decision and another review—not automatic human acceptance.

Three additional records have **damaged/uncertified original notation**, not
merely unwanted handwriting: the realization continuation on printed page 290
and example 4.31 on page 295 in M08, plus example 4.173 on page 363 in M10.
Their crop boundaries passed, but the affected
notation did not receive certification. They are `source_damage`, explicitly
unapproved and excluded from the default independent-pass confirmation view.

## Earlier resumed batch: M07

M07 printed **257–276 / PDF 129–139** is now provisionally integrated in
`chapters/03-kromatika-c.md`. Independent review classified 36 initial passes,
four correctable clipping failures and 17 source-limited failures. All four
source-only recrops passed a separate re-review, yielding **40 independent
passes and 17 explicit cleanup cases**. The original extraction manifest is
preserved; final paths and statuses are in
`review-candidates/book/M07/images-integrated.json`, with the complete slot
mapping and validation in `review-candidates/book/M07/INTEGRATION.md`.

## M08 preparation

M08 printed **277–308 / PDF 139–155** is provisionally integrated in
`chapters/04-neakordicki-a.md`. All 105 visual slots are accounted for, including
the two inline graphics missing from the earlier 103-record extraction. Its
independent reviews and applied recrop yield **81 approved crops, 22 cleanup
holds and two source-damage holds**. Both inline graphics remain inline in the
prose. Original crops, metadata and verified text shards are preserved.

Full per-slot mapping: `review-candidates/book/M08/INTEGRATION.md`.
Final paths/statuses: `review-candidates/book/M08/images-integrated.json`.

## Current M09 checkpoint

All M09 text for **309–348 / PDF 155–175** is verified in five shards and
provisionally integrated in `chapters/04-neakordicki-b.md`, with **111 approved
image embeds and 23 explicit manual-review/cleanup holds** across both batches.
Example 4.67's footnote/fermata conflict is not
treated as approved; its printed explanation remains transcribed beside it.
The second **66-crop batch for 329–348** contributed 59 passes and seven
source-limited holds. No failed crop was promoted to a pass. Both integration
reports preserve the printed reference discrepancy on page 344.

## Current M10 and M11 checkpoint

All M10 text and **86 visual parts on pages 349–378** are provisionally
integrated in `chapters/04-neakordicki-c.md`: **80 approved embeds, five explicit
cleanup holds and one source-damage hold**. Both 4.178 parts, 4.169, 4.192 and
4.193 remain blocked; no excerpt continuation or final barline was invented.

M11 is provisionally integrated in `chapters/05-rekapitulacija.md` (379–385)
and `chapters/dodaci.md` (386–411). All 33 pages, all 730 table lines, footnote 8,
blank-page metadata and 44 visual slots are preserved. Independent review and
the exercise-6 recrop re-review yield **36 passing crops and eight layout holds**:
exercises 9, 10 first part, 11, 12; glyphs `slika-386-1`, `slika-386-2`,
`slika-386-5`, `slika-387-14`. These eight remain unapproved links.
Full source-page/decision mapping: `review-candidates/book/M11/INTEGRATION.md`.

## Next session

1. Check usage limits before resuming; keep **one active subagent maximum**.
2. **Do not restart book extraction: preparation is finished.** Confirm passing
   images in the viewer; handle cleanup/layout and source-damage cases separately.
   Preserve originals and edit separate GIMP copies. Closing GIMP signals the
   edited copy is ready for independent review, not automatic approval.
3. Resolve provisional images and run full-section rendered previews, footnote,
   link, example-number continuity and text integration checks before marking
   any milestone complete.

## Human confirmation interface

The upgraded workspace adds keyboard shortcuts, chapter/page/issue filters,
progress/resume, draft-note protection, undo, source-region highlighting and
per-page chapter context. Full instructions: `tools/BOOK-REVIEW.md`.
GIMP edits use separate copies and are snapshotted/queued on editor exit; the
viewer does not launch AI reviewers or approve/integrate edits automatically.
Use the generated `CLEANUP-REVIEW-READY.md` bundle for the separate review step.
The workflow upgrade passed **28 isolated tests**, including a real Chromium
session using a fake GIMP process; a real desktop GIMP edit/export/close cycle
still needs a user smoke test. A separate read-only run checked all 1,206 real
records for findings and chapter context without creating decisions or jobs.
Structural results: `review-candidates/book/REVIEW-WORKFLOW-AUDIT.md`.

```bash
python tools/review_book.py
```

Open the local URL it prints (default `http://127.0.0.1:8765`). The viewer defaults
to **Independently passed — confirm**, showing the crop beside its original
source page. It also has separate **Cleanup required**, **Damaged or uncertain source notation**, **Independent review
pending**, and **All prepared images** views. Decisions are stored in
`review-candidates/book/human-review-state.json`; this file is separate from
source crops and independent review records.

The current consolidated queue has **1,206 records**: 870 independent passes,
333 cleanup cases, three source-damage holds and no pending independent review.
M11 is included; human decisions do not overwrite independent-review metadata.
It intentionally excludes
the earlier approved material through printed page 46.

Rebuild the same queue after updating reviewed hand-offs:

```bash
python tools/build_book_review_queue.py --milestone M02 --milestone M03 --milestone M04 --milestone M05 --milestone M06 --milestone M07 --milestone M08 --milestone M09 --milestone M10 --milestone M11
```

## Provenance and outstanding checks

- Every integrated crop is checked against its source PNG and rectangle.
- Original extraction manifests are preserved; integrated manifests carry the
  final paths, review statuses, and corrected PDF mappings.
- M03's final shard had **35 even-page PDF reference corrections**; M06's first
  text shard had **eight corrected PDF source comments**. Corrections use
  `sources/index.json`, not page-number arithmetic.
- All remaining-page OCR drafts (47–411) are available under
  `review-candidates/book/ocr/`, explicitly **not visually verified**. They are
  drafts, never substitutes for scan comparison.
- No unresolved unreadable printed prose was reported in the verified shards;
  printed irregularities and cross-page continuations are documented in the
  per-page text reviews. This does not replace final full-section proofreading.
- Final parent audit verified **1,206/1,206 queue crops** against original source
  pixels and authoritative page mappings. After M11 integration, all **1,551
  chapter links** resolve and all **365 source-page markers for pages 47–411**
  are present exactly once with correct PDF references.
  It corrected 849 generated links that had incorrectly been relative to the
  repository root rather than their containing chapter; no prose or image
  pixels were changed by that correction. The correction is reproducible with
  `python tools/fix_markdown_links.py --apply` and is idempotent.
- All 12 chapter files render with `python tools/preview_book.py`. Representative
  recap, terminology, index, inline-glyph and source-damage/cleanup label previews
  were visually inspected. This is a spot check, not full-book visual acceptance.
  Chromium fragment-navigation screenshots were blank; standalone page excerpts
  rendered correctly. Local output: `/tmp/opencode/harmonija-book-preview/`.
- Book preparation through page 411 was committed/pushed as **`0a28718`** after
  `62be9a5`. The subsequent review-workflow upgrade is included in its own
  user-authorized commit/push checkpoint on 2026-11-23. Unrelated catalog/cache edits, raw OCR,
  temporary previews/logs and GIMP working backups are preserved.
