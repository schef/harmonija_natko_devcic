# Harmonija — Natko Devčić

Work-in-progress Markdown edition of *Harmonija* by Natko Devčić (Školska knjiga, Zagreb, 1975).

The project converts the scanned source PDF into clean, readable Croatian Markdown. It preserves the book's structure and will include only meaningful visual material, such as musical examples, diagrams, and illustrations. Library stamps, barcodes, and full-page scans are not part of the Markdown edition.

## Repository layout

```text
pdfcoffee.com_natko-devi-harmonija-pdf-free.pdf  # scanned source PDF
sample/
  harmonija-sample.md                            # verified opening-page sample
```

As the conversion grows, chapters will be stored as Markdown files and visual material will be placed in an `images/` directory using relative links. MuseScore source files (`.mscz`) may later be added beside their corresponding musical examples.

## Conversion status and next steps

The section-based queue and its acceptance criteria are in [MILESTONES.md](MILESTONES.md).

Instructions for text conversion, score-only image extraction, and independent visual review are in [AGENTS.md](AGENTS.md). Every musical example must be checked by a reviewer other than the extracting agent before its milestone is complete.

- [x] Add the scanned source PDF to the repository.
- [x] Create and manually verify a Markdown sample of the opening pages.
- [x] Extract and embed one cropped musical example (`Primjer 2.33`).
- [ ] Decide the final folder and file layout for chapters, images, and MuseScore files.
- [ ] Convert the remaining text into clean Markdown, preserving headings, paragraphs, lists, and example numbers.
- [ ] Compare every converted section with the source scan and correct OCR errors before committing it.
- [ ] Extract musical examples, diagrams, and illustrations as individual cropped images; do not include page scans, library stamps, or barcodes.
- [ ] Add meaningful captions and source-page references for every extracted image.
- [ ] Create MuseScore (`.mscz`) transcriptions where wanted and link each one next to its corresponding score image.
- [ ] Review rendered Markdown locally before committing; push completed, reviewed batches to GitHub.

## Preview Markdown locally

No push is needed to review changes locally.

- **VS Code / VSCodium:** open a Markdown file and press `Ctrl+Shift+V` for its preview.
- **GitHub-style browser preview:** install and run [Grip](https://github.com/joeyespo/grip):

  ```bash
  pip install grip
  grip sample/harmonija-sample.md
  ```

  Open the local URL that Grip prints in the terminal.

GitHub will render the same Markdown automatically after the repository is pushed.
