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
