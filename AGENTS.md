# Agent guide: book conversion and score-image review

This repository converts *Harmonija* by Natko Devčić from a scanned PDF into clean Croatian Markdown. Accuracy matters more than speed. Do not treat the PDF's embedded OCR as authoritative.

## Scope rules

- Work only on the milestone, printed-page range, and output paths assigned to you in [MILESTONES.md](MILESTONES.md).
- Do not edit another agent's section without being explicitly assigned to review it.
- Do not commit or push unless the user explicitly asks.
- Keep all Markdown, image paths, and captions relative to the repository root.

## Text-conversion procedure

1. Render the assigned PDF pages at a readable resolution.
2. Use OCR only as a draft.
3. Compare every Markdown paragraph, heading, example number, footnote, and quotation against the scan.
4. Correct OCR errors manually, including Croatian diacritics, hyphenated words, punctuation, and musical terminology.
5. Preserve the printed hierarchy with Markdown headings.
6. Add a source-page reference to every extracted visual example.

## Musical-example extraction procedure

Every musical example requires a separate image. A page scan is **not** a musical-example image.

1. Open the rendered source page and identify the exact bounds of the example.
2. Crop from the original source scan only. Exclude body text, headings, adjacent examples, marginal notes, page numbers, library marks, and barcodes, but retain a small, content-free white margin on every edge whenever that blank source area exists. Do not add, generate, extend, or paint a border after cropping.
   - Do not expand a crop by a fixed amount or process a page's examples in a batch. Adjacent examples often have different safe boundaries.
   - Determine the four crop edges separately for each example from the source scan. Where a neighbouring example or prose leaves no clean gap, stop at the natural separation; preserving unrelated content merely to create a margin is a failure.
   - If a page number or other unrelated mark threatens one edge, adjust a different edge first when possible. For example, shift the crop sideways to exclude a bottom-corner page number, then retain the complete lower annotation and its genuine white margin. Never solve this by clipping part of the example.
   - Inspect each crop edge at full resolution before approval. A crop fails if even a partial letter, punctuation mark, staff fragment, page number, or other non-example ink is visible at an edge. Move the relevant edge to the nearest clean source whitespace; do not merely make the foreign mark less visible.
3. Retain all content belonging to that one example:
   - example number;
   - lettered variants such as `a)`, `b)`, and `c)`;
   - composer/work attribution where printed with the example;
   - every staff, clef, key signature, time signature, note, rest, slur, tie, dynamic, arrow, bracket, figured-bass mark, and Roman-numeral annotation;
   - the final barline and any continuation or reduction that is part of the example.
4. Name it predictably: `images/<section>/primjer-<chapter>-<number>.png`.
5. Embed it immediately after its textual reference, followed by a caption, printed source page, and MuseScore placeholder.

## Mandatory visual review

The extractor may not approve their own crop. A separate review agent must inspect each image against the rendered source page.

The reviewer must mark every image as either **pass** or **recrop required** using this checklist:

- [ ] The image contains only the intended example; no surrounding prose or unrelated example is visible.
- [ ] The example number is present.
- [ ] All labels and variants are present.
- [ ] The left and right edges of every staff are intact.
- [ ] No notation, annotation, or attribution is clipped at the top, bottom, left, or right edge.
- [ ] A small content-free margin from the original scan is visible on every feasible edge; no artificial border has been added.
- [ ] The crop contains no printed page number, running header, body paragraph, stamp, barcode, or marginal handwriting.
- [ ] Each of the four edges has been inspected at full resolution; no partial non-example character or mark is visible.
- [ ] The image path, Markdown alt text, caption, and printed source-page reference agree with the source.

An image that fails any item must be recropped and reviewed again. Do not accept a crop merely because its main notes are visible.

## Parallel-agent roles

Use these independent roles when processing a milestone:

| Role | Responsibility | May edit |
| --- | --- | --- |
| Text agent | Transcribe and verify prose, headings, and footnotes. | Assigned Markdown file only. |
| Extraction agent | Produce score-only crops and add image references. | Assigned image directory and Markdown image blocks. |
| Visual-review agent | Compare every crop with the source and report pass/recrop-required decisions. | No files; report findings only. |
| Integration agent | Apply reviewed corrections, run link checks, and update milestone status. | Assigned section and `MILESTONES.md`. |

The integration agent may mark a milestone complete only after text review and image review both pass.

## Required hand-off report

At the end of each job, report:

1. assigned printed and PDF pages;
2. files created or changed;
3. musical examples extracted and their printed source pages;
4. image-review result for each example;
5. unreadable, ambiguous, or incomplete source material;
6. whether the job is ready for integration.
