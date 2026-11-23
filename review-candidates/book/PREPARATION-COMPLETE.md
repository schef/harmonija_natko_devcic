# Preparation complete — human image review hand-off

Date: 2026-11-22. This reports completed preparation, **not publication readiness,
human acceptance, or completed milestones**.

## Assigned coverage and outputs

- Remaining printed pages **47–411**, authoritative PDF pages **24–206**.
  Printed/PDF mappings come from `sources/index.json`, not arithmetic.
- Previously approved material through printed page 46 was preserved.
- Verified text is provisionally integrated in `chapters/`; resumed outputs are
  `chapters/03-kromatika-c.md`, `chapters/04-neakordicki-a.md`,
  `chapters/04-neakordicki-b.md`, `chapters/04-neakordicki-c.md`,
  `chapters/05-rekapitulacija.md` and `chapters/dodaci.md`.
- Recap occupies printed **379–385**; appendices occupy **386–411**.
  Terminology/index/name-index/contents entries are structured text, not page images.
- Image outputs and separate recrops are under the matching `images/` section
  directories. Originals and raw extraction manifests remain preserved.
- Verified text shards, per-page checks, extraction/independent-review reports,
  final manifests and exact slot/source-page maps are under
  `review-candidates/book/M02/` through `review-candidates/book/M11/`.
- Global outputs updated: `MILESTONES.md`, `review-candidates/book/STATUS.md`,
  `review-candidates/book/review-queue.json`, `review-candidates/book/REVIEW-QUEUE.md`.
  Review/recrop tooling was updated; `tools/preview_book.py` was added.

## Every image has a recorded decision

The consolidated queue contains **1,206 unique visual parts**:

| Milestone | Printed source pages | Parts | Independent pass | Cleanup/layout | Source damage |
| --- | --- | ---: | ---: | ---: | ---: |
| M02 remainder | 47–63 | 69 | 49 | 20 | 0 |
| M03 | 64–136 | 310 | 158 | 152 | 0 |
| M04 | 137–174 | 128 | 107 | 21 | 0 |
| M05 | 175–206 | 104 | 66 | 38 | 0 |
| M06 | 207–256 | 169 | 142 | 27 | 0 |
| M07 | 257–276 | 57 | 40 | 17 | 0 |
| M08 | 277–308 | 105 | 81 | 22 | 2 |
| M09 | 309–348 | 134 | 111 | 23 | 0 |
| M10 | 349–378 | 86 | 80 | 5 | 1 |
| M11 | 379–411; visuals 379–387 | 44 | 36 | 8 | 0 |
| **Total** | **47–411** | **1,206** | **870** | **333** | **3** |

For **each individual example/part**, the canonical queue and each milestone's
`images-integrated.json` provide its identity, image path, printed/PDF source
page, source rectangle and final review status. Independent review reasons and
per-slot captions are retained in milestone review/integration reports and
section `REVIEW.md` files. Multipart continuations and unnumbered inline glyphs
retain their actual source identities; no printed numbers were invented.

Passing crops are embedded. Failed crops remain explicitly unapproved links.
There are **zero pending independent-review records**, but human confirmation
and all 336 holds remain outstanding.

## Ambiguous or incomplete source material

No unresolved unreadable printed prose was reported in the verified text shards.
Printed anomalies and reference discrepancies were retained and documented.
This does not certify every damaged note or replace final proofreading.

Three original-source notation-damage holds are explicitly unapproved:

- M08 realization continuation, printed **290**, PDF **146**.
- M08 example **4.31**, printed **295**, PDF **148**.
- M10 example **4.173**, printed **363**, PDF **182**.

Their crop boundaries passed, but missing/worn notation was not certified.
The 333 other holds include handwriting, adjacent-content overlap and source
layout conflicts. No unattended painting, notation invention, source stitching
or generated white borders were used to make these appear approved.

## Final checks

- **1,206/1,206** crops match their recorded original source rectangles in decoded
  pixel mode, dimensions and bytes; all authoritative printed/PDF mappings agree.
- **1,551** local chapter links resolve.
- All **365** printed source-page markers for **47–411** occur exactly once and
  carry correct PDF references.
- M11 integration round-trip preserves all **730 table lines**, footnote 8,
  printed anomalies, cross-page continuations and blank-page metadata.
- All **12** chapter Markdown files render via `python tools/preview_book.py`.
  Representative recap, terminology, index, inline-glyph and hold-label previews
  were visually inspected. This is a spot check, not exhaustive visual acceptance.
  Chromium screenshots using fragment navigation were blank; rendering standalone
  excerpts from the generated HTML produced inspectable previews.
- `git diff --check` passes. The user authorized a scoped commit and push on
  2026-11-23 after receiving this preparation hand-off.

## Ready for the user's next review session

Preparation is finished; **do not restart extraction**. Start confirmation with:

```bash
python tools/review_book.py
```

Open `http://127.0.0.1:8765` (or the URL printed by the tool). The default view
contains independently passing images. Cleanup and source damage have separate
views; decisions are stored separately in `human-review-state.json`.

Preserve originals and manually edit separate GIMP copies where needed. Closing
GIMP signals that a copy is ready for independent review, not automatic acceptance.
Source-damage cases require an explicit notation/source decision, not merely a
crop-boundary confirmation. Milestones remain unchecked until required final
text/image acceptance and assembled-section checks pass.

Local previews: `/tmp/opencode/harmonija-book-preview/index.html`.
The preceding committed/pushed checkpoint is `62be9a5`; this hand-off accompanies
the user-authorized resumed-preparation commit.
Unrelated catalog/cache changes, temporary files and GIMP backups are preserved.
