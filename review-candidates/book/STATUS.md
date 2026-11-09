# Whole-book preparation checkpoint

## Paused at the usage guard

The latest active-account weekly limit was **51% remaining**. Work was paused
before starting another agent, leaving a buffer above the user's 50%-remaining
cutoff. All work in this sequential phase used at most one subagent at a time,
without nested delegation or model subprocesses.

This is **not a whole-book completion report**. Do not mark milestones complete
merely because text and image placeholders have been integrated.

## Completed preparation and independent review

Verified text is provisionally integrated from printed page 47 through 256.
The previously approved work through page 46 is preserved.

| Milestone | Printed pages | PDF pages | Prepared parts | Independent pass | Cleanup required |
| --- | --- | --- | ---: | ---: | ---: |
| M02 remainder | 47–63 | 24–32 | 69 | 49 | 20 |
| M03 | 64–136 | 33–69 | 310 | 158 | 152 |
| M04 | 137–174 | 69–88 | 128 | 107 | 21 |
| M05 | 175–206 | 88–104 | 104 | 66 | 38 |
| M06 | 207–256 | 104–129 | 169 | 142 | 27 |
| **Reviewed total** | **47–256** | **24–129** | **780** | **522** | **258** |

Each reviewed image has an independent per-image decision. Feasible boundary
corrections were generated as separate source-only recrops and independently
re-reviewed; originals were not overwritten. Source-limited crops remain
explicitly provisional links, not approved embedded images. No unattended
handwriting removal or generated borders were used.

The 258 cleanup cases include internal pencil annotations, adjacent visual/prose
overlap, and other source-layout constraints. They require a separate cleanup
or source decision and another review—not automatic human acceptance.

## Prepared but not independently reviewed

M07 printed **257–276 / PDF 129–139**:

- Verified text: `review-candidates/book/M07/text-257-276.md`.
- Per-page verification: `review-candidates/book/M07/text-257-276-review.json`.
- **57 crops**, all `pending_independent_review`:
  `review-candidates/book/M07/images.json`.
- The extractor flagged 18 examples for potential source-mark cleanup; these
  flags are not independent review decisions.
- M07 has not been promoted to `chapters/03-kromatika-c.md`.

## Next session

1. Check usage limits before resuming; keep **one active subagent maximum**.
2. Independently review all 57 M07 crops, apply feasible source-only recrops and
   re-review replacements, then integrate the verified text and image decisions.
3. Continue M08–M11, printed **277–411 / PDF 139–206**. Earlier partial crop
   manifests for these sections are preserved but must be checked for complete
   coverage and independently reviewed; they are not silently approved.
4. Resolve provisional images and run full-section rendered previews, footnote,
   link, example-number continuity and text integration checks before marking
   any milestone complete.

## Human confirmation interface

```bash
python tools/review_book.py
```

Open the local URL it prints (default `http://127.0.0.1:8765`). The viewer defaults
to **Independently passed — confirm**, showing the crop beside its original
source page. It also has separate **Cleanup required**, **Independent review
pending**, and **All prepared images** views. Decisions are stored in
`review-candidates/book/human-review-state.json`; this file is separate from
source crops and independent review records.

The current consolidated queue has **837 records**: 522 independent passes,
258 cleanup cases and 57 pending independent review. It intentionally excludes
the earlier approved material through printed page 46.

Rebuild the same queue after updating reviewed hand-offs:

```bash
python tools/build_book_review_queue.py --milestone M02 --milestone M03 --milestone M04 --milestone M05 --milestone M06 --milestone M07
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
- Final integration audit verified **837/837 queue crops** against original
  source pixels and authoritative page mappings, and **1,038 chapter links**.
  It corrected 849 generated links that had incorrectly been relative to the
  repository root rather than their containing chapter; no prose or image
  pixels were changed by that correction. The correction is reproducible with
  `python tools/fix_markdown_links.py --apply` and is idempotent.
- The user explicitly requested committing and pushing this checkpoint after
  preparation paused. The commit includes chapter content, source/recrop images,
  selected review manifests and reports, and the review tools. Raw OCR output,
  temporary inspection files, logs, GIMP working backups and unrelated catalog/
  cache changes remain local and are excluded. Working files are preserved.
