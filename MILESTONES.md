# Conversion milestones

This is the work queue for section-based conversion agents. Each checkbox is one self-contained job. The printed-page ranges come from the book's table of contents; the PDF consists of page spreads, so a source scan page normally contains two printed pages.

## Standard job requirements

Every conversion job must:

1. Work only in its assigned printed-page and PDF-page range.
2. Create or update its assigned Markdown file under `chapters/`.
3. Correct OCR by comparing the Markdown against the source image; never copy raw OCR output directly.
4. Extract each musical example, diagram, or illustration into the assigned `images/` subdirectory. Do not include complete scans, stamps, barcodes, or marginal markings.
5. Add a caption and printed source-page reference below every image.
6. Add a placeholder for an eventual MuseScore transcription when the image is a notated musical example.
7. Preview the Markdown locally and report the files changed, examples extracted, and any unreadable passages. Do not commit or push unless explicitly asked.

## Jobs

| Status | Job | Scope | Printed pages | PDF pages | Output |
| --- | --- | --- | --- | --- | --- |
| [x] | Demo | Verified opening sample and one cropped score example | cover–5, 23 | 1–3, 12 | `sample/` |
| [x] | M01 | Introduction | 7–10 | 4–6 | `chapters/01-uvod.md`, `images/01-uvod/` |
| [ ] | M02 | Diatonika: kvintakordi and sekstakordi (§§2.1–2.2) | 11–63 | 6–32 | `chapters/02-dijatonika-a.md`, `images/02-dijatonika-a/` |
| [ ] | M03 | Diatonika: kvartsekstakordi through nonakordi (§§2.3–2.8) | 64–136 | 33–69 | `chapters/02-dijatonika-b.md`, `images/02-dijatonika-b/` |
| [ ] | M04 | Diatonika: modulacije and stari načini (§§2.9–2.10) | 137–174 | 69–88 | `chapters/02-dijatonika-c.md`, `images/02-dijatonika-c/` |
| [ ] | M05 | Kromatika i enharmonija: kromatski pomak through kromatske modulacije (§§3.1–3.4) | 175–206 | 88–104 | `chapters/03-kromatika-a.md`, `images/03-kromatika-a/` |
| [ ] | M06 | Kromatika i enharmonija: Napuljski and enharmonijske modulacije (§§3.5–3.7) | 207–256 | 104–129 | `chapters/03-kromatika-b.md`, `images/03-kromatika-b/` |
| [ ] | M07 | Kromatika i enharmonija: remaining altered chords (§§3.8–3.10) | 257–276 | 129–139 | `chapters/03-kromatika-c.md`, `images/03-kromatika-c/` |
| [ ] | M08 | Neakordički tonovi: zaostajalice (§4.1) | 277–308 | 139–155 | `chapters/04-neakordicki-a.md`, `images/04-neakordicki-a/` |
| [ ] | M09 | Neakordički tonovi: prohodni and izmjenični tonovi (§4.2) | 309–348 | 155–175 | `chapters/04-neakordicki-b.md`, `images/04-neakordicki-b/` |
| [ ] | M10 | Neakordički tonovi: appoggiature through special aspects (§§4.3–4.6) | 349–378 | 175–190 | `chapters/04-neakordicki-c.md`, `images/04-neakordicki-c/` |
| [ ] | M11 | Rekapitulacija and reference material | 379–411 | 190–206 | `chapters/05-rekapitulacija.md`, `chapters/dodaci.md` |

## Milestone completion

- **Milestone 1 — structure:** M01 is complete and its Markdown, image paths, and local preview have been reviewed.
- **Milestone 2 — dijatonika:** M02–M04 are complete and cross-checked for continuous example numbering.
- **Milestone 3 — kromatika i enharmonija:** M05–M07 are complete and cross-checked.
- **Milestone 4 — neakordički tonovi:** M08–M10 are complete and cross-checked.
- **Milestone 5 — publication review:** M11 is complete; all links, images, source references, and MuseScore placeholders have been checked.
