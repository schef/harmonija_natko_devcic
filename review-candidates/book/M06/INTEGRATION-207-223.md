# M06 integration hand-off — printed pages 207–223

## Outcome and scope

Integrated the verified shard into `chapters/03-kromatika-b.md`: **52 exact visual slots, 30 independently passing embedded crops, 22 PROVISIONAL / cleanup_required unapproved source-crop links**. Printed **207–223**, PDF **104–112** only. No delegation, model subprocess, API or GUI was used.

This is a bounded partial integration, **not M06 completion and not human approval**. Stop at printed **223**; next page is **224**. References to 3.117–3.120 are retained as printed prose, but those later examples are not integrated here.

## Files created

- `chapters/03-kromatika-b.md`
- `images/03-kromatika-b/REVIEW.md`
- `review-candidates/book/M06/images-integrated.json`
- `review-candidates/book/M06/INTEGRATION-207-223.md`

All four paths were absent at preflight. There was no prior chapter content to overwrite. Every pre-existing repository file was SHA-256 snapshotted before integration and checked unchanged afterward, including source PNGs, raw text/review shards, extraction manifests, shared trackers and other workers' material.

## Text preservation and metadata corrections

Text authority is `review-candidates/book/M06/text-207-223.md`, with 17 verified page records in `review-candidates/book/M06/text-207-223-review.json`. Preserve these raw shards unchanged, including their original mistaken even-page PDF metadata.

No prose was changed. All paragraphs, original slot comments, attributions, exercise instruction 1, ZADACI heading, realization title, two asterisk footnotes on 220, source comments and continuation comments are retained. Heading-only normalization: `## 3. 5.` → `## 3.5.` and `## 3. 6.` → `## 3.6.`. The new root heading is `# 3. Kromatika i enharmonija — nastavak`.

The eight even-page source comments were corrected only in the integrated chapter using `sources/index.json`. Odd-page references were already correct. The raw text-review JSON shares these eight errors and was intentionally not modified; integrated metadata and the following table are authoritative.

| Printed page | Raw text/review PDF reference | Correct integrated PDF reference | Indexed source half |
| --- | --- | --- | --- |
| 208 | 104 | 105 | left |
| 210 | 105 | 106 | left |
| 212 | 106 | 107 | left |
| 214 | 107 | 108 | left |
| 216 | 108 | 109 | left |
| 218 | 109 | 110 | left |
| 220 | 110 | 111 | left |
| 222 | 111 | 112 | left |

## All 52 exact slot identities and source pages

Rows are in original text order; exercises and the realization retain distinct stable IDs. Example 3.101 a–c / d–f is not merged.

| Slot | Exact text slot | Stable ID | Printed page | PDF / half | Source crop (root-relative) | Final disposition |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 3.79 | `primjer-3-79` | 207 | 104 right | [images/03-kromatika-b/primjer-3-79.png](images/03-kromatika-b/primjer-3-79.png) | PASS / embedded |
| 2 | 3.80 | `primjer-3-80` | 207 | 104 right | [images/03-kromatika-b/primjer-3-80.png](images/03-kromatika-b/primjer-3-80.png) | PASS / embedded |
| 3 | 3.81 | `primjer-3-81` | 208 | 105 left | [images/03-kromatika-b/primjer-3-81.png](images/03-kromatika-b/primjer-3-81.png) | PASS / embedded |
| 4 | 3.82 | `primjer-3-82` | 208 | 105 left | [images/03-kromatika-b/primjer-3-82.png](images/03-kromatika-b/primjer-3-82.png) | PASS / embedded |
| 5 | 3.83 | `primjer-3-83` | 208 | 105 left | [images/03-kromatika-b/primjer-3-83.png](images/03-kromatika-b/primjer-3-83.png) | cleanup_required / unapproved link |
| 6 | 3.84 | `primjer-3-84` | 209 | 105 right | [images/03-kromatika-b/primjer-3-84.png](images/03-kromatika-b/primjer-3-84.png) | PASS / embedded |
| 7 | 3.85 | `primjer-3-85` | 209 | 105 right | [images/03-kromatika-b/primjer-3-85.png](images/03-kromatika-b/primjer-3-85.png) | PASS / embedded |
| 8 | 3.86 | `primjer-3-86` | 210 | 106 left | [images/03-kromatika-b/primjer-3-86.png](images/03-kromatika-b/primjer-3-86.png) | PASS / embedded |
| 9 | 3.87 | `primjer-3-87` | 210 | 106 left | [images/03-kromatika-b/primjer-3-87.png](images/03-kromatika-b/primjer-3-87.png) | PASS / embedded |
| 10 | 3.88 | `primjer-3-88` | 211 | 106 right | [images/03-kromatika-b/primjer-3-88.png](images/03-kromatika-b/primjer-3-88.png) | PASS / embedded |
| 11 | 3.89 | `primjer-3-89` | 211 | 106 right | [images/03-kromatika-b/primjer-3-89.png](images/03-kromatika-b/primjer-3-89.png) | PASS / embedded |
| 12 | 3.90 | `primjer-3-90` | 211 | 106 right | [images/03-kromatika-b/primjer-3-90.png](images/03-kromatika-b/primjer-3-90.png) | PASS / embedded |
| 13 | 3.91 | `primjer-3-91` | 212 | 107 left | [images/03-kromatika-b/primjer-3-91.png](images/03-kromatika-b/primjer-3-91.png) | PASS / embedded |
| 14 | 3.92 | `primjer-3-92` | 212 | 107 left | [images/03-kromatika-b/primjer-3-92.png](images/03-kromatika-b/primjer-3-92.png) | PASS / embedded |
| 15 | ZADACI 2 | `zadatak-3-212-2` | 212 | 107 left | [images/03-kromatika-b/zadatak-3-212-2.png](images/03-kromatika-b/zadatak-3-212-2.png) | PASS / embedded |
| 16 | ZADACI 3 | `zadatak-3-212-3` | 212 | 107 left | [images/03-kromatika-b/zadatak-3-212-3.png](images/03-kromatika-b/zadatak-3-212-3.png) | PASS / embedded |
| 17 | ZADACI 4 | `zadatak-3-212-4` | 212 | 107 left | [images/03-kromatika-b/zadatak-3-212-4.png](images/03-kromatika-b/zadatak-3-212-4.png) | cleanup_required / unapproved link |
| 18 | ZADACI 5 | `zadatak-3-212-5` | 212 | 107 left | [images/03-kromatika-b/zadatak-3-212-5.png](images/03-kromatika-b/zadatak-3-212-5.png) | cleanup_required / unapproved link |
| 19 | ZADACI 6 | `zadatak-3-213-6` | 213 | 107 right | [images/03-kromatika-b/zadatak-3-213-6.png](images/03-kromatika-b/zadatak-3-213-6.png) | PASS / embedded |
| 20 | ZADACI 7 | `zadatak-3-213-7` | 213 | 107 right | [images/03-kromatika-b/zadatak-3-213-7.png](images/03-kromatika-b/zadatak-3-213-7.png) | PASS / embedded |
| 21 | ZADACI 8 | `zadatak-3-213-8` | 213 | 107 right | [images/03-kromatika-b/zadatak-3-213-8.png](images/03-kromatika-b/zadatak-3-213-8.png) | PASS / embedded |
| 22 | ZADACI 9 | `zadatak-3-213-9` | 213 | 107 right | [images/03-kromatika-b/zadatak-3-213-9.png](images/03-kromatika-b/zadatak-3-213-9.png) | PASS / embedded |
| 23 | ZADACI 10 | `zadatak-3-213-10` | 213 | 107 right | [images/03-kromatika-b/zadatak-3-213-10.png](images/03-kromatika-b/zadatak-3-213-10.png) | PASS / embedded |
| 24 | ZADACI 11 | `zadatak-3-213-11` | 213 | 107 right | [images/03-kromatika-b/zadatak-3-213-11.png](images/03-kromatika-b/zadatak-3-213-11.png) | PASS / embedded |
| 25 | ZADACI 12 | `zadatak-3-213-12` | 213 | 107 right | [images/03-kromatika-b/zadatak-3-213-12.png](images/03-kromatika-b/zadatak-3-213-12.png) | PASS / embedded |
| 26 | ZADACI 13 | `zadatak-3-213-13` | 213 | 107 right | [images/03-kromatika-b/zadatak-3-213-13.png](images/03-kromatika-b/zadatak-3-213-13.png) | PASS / embedded |
| 27 | Realizacija zadatka 7. | `realizacija-3-213-zadatak-7` | 213 | 107 right | [images/03-kromatika-b/realizacija-3-213-zadatak-7.png](images/03-kromatika-b/realizacija-3-213-zadatak-7.png) | PASS / embedded |
| 28 | 3.93 | `primjer-3-93` | 214 | 108 left | [images/03-kromatika-b/primjer-3-93.png](images/03-kromatika-b/primjer-3-93.png) | cleanup_required / unapproved link |
| 29 | 3.94 | `primjer-3-94` | 214 | 108 left | [images/03-kromatika-b/primjer-3-94.png](images/03-kromatika-b/primjer-3-94.png) | PASS / embedded |
| 30 | 3.95 | `primjer-3-95` | 215 | 108 right | [images/03-kromatika-b/primjer-3-95.png](images/03-kromatika-b/primjer-3-95.png) | cleanup_required / unapproved link |
| 31 | 3.96 | `primjer-3-96` | 215 | 108 right | [images/03-kromatika-b/primjer-3-96.png](images/03-kromatika-b/primjer-3-96.png) | cleanup_required / unapproved link |
| 32 | 3.97 | `primjer-3-97` | 215 | 108 right | [images/03-kromatika-b/primjer-3-97.png](images/03-kromatika-b/primjer-3-97.png) | PASS / embedded |
| 33 | 3.98 | `primjer-3-98` | 216 | 109 left | [images/03-kromatika-b/primjer-3-98.png](images/03-kromatika-b/primjer-3-98.png) | cleanup_required / unapproved link |
| 34 | 3.99 | `primjer-3-99` | 216 | 109 left | [images/03-kromatika-b/primjer-3-99.png](images/03-kromatika-b/primjer-3-99.png) | cleanup_required / unapproved link |
| 35 | 3.100 | `primjer-3-100` | 216 | 109 left | [images/03-kromatika-b/primjer-3-100.png](images/03-kromatika-b/primjer-3-100.png) | cleanup_required / unapproved link |
| 36 | 3.101 a–c | `primjer-3-101-a-c` | 216 | 109 left | [images/03-kromatika-b/primjer-3-101-a-c.png](images/03-kromatika-b/primjer-3-101-a-c.png) | cleanup_required / unapproved link |
| 37 | 3.101 d–f | `primjer-3-101-d-f` | 217 | 109 right | [images/03-kromatika-b/primjer-3-101-d-f.png](images/03-kromatika-b/primjer-3-101-d-f.png) | cleanup_required / unapproved link |
| 38 | 3.102 | `primjer-3-102` | 217 | 109 right | [images/03-kromatika-b/primjer-3-102.png](images/03-kromatika-b/primjer-3-102.png) | cleanup_required / unapproved link |
| 39 | 3.103 | `primjer-3-103` | 217 | 109 right | [images/03-kromatika-b/primjer-3-103.png](images/03-kromatika-b/primjer-3-103.png) | cleanup_required / unapproved link |
| 40 | 3.104 | `primjer-3-104` | 218 | 110 left | [images/03-kromatika-b/primjer-3-104.png](images/03-kromatika-b/primjer-3-104.png) | cleanup_required / unapproved link |
| 41 | 3.105 | `primjer-3-105` | 218 | 110 left | [images/03-kromatika-b/primjer-3-105.png](images/03-kromatika-b/primjer-3-105.png) | PASS / embedded |
| 42 | 3.106 | `primjer-3-106` | 219 | 110 right | [images/03-kromatika-b/primjer-3-106.png](images/03-kromatika-b/primjer-3-106.png) | cleanup_required / unapproved link |
| 43 | 3.107 | `primjer-3-107` | 220 | 111 left | [images/03-kromatika-b/primjer-3-107.png](images/03-kromatika-b/primjer-3-107.png) | cleanup_required / unapproved link |
| 44 | 3.108 | `primjer-3-108` | 220 | 111 left | [images/03-kromatika-b/primjer-3-108.png](images/03-kromatika-b/primjer-3-108.png) | cleanup_required / unapproved link |
| 45 | 3.109 | `primjer-3-109` | 221 | 111 right | [images/03-kromatika-b/primjer-3-109.png](images/03-kromatika-b/primjer-3-109.png) | cleanup_required / unapproved link |
| 46 | 3.110 | `primjer-3-110` | 221 | 111 right | [images/03-kromatika-b/primjer-3-110.png](images/03-kromatika-b/primjer-3-110.png) | cleanup_required / unapproved link |
| 47 | 3.111 | `primjer-3-111` | 221 | 111 right | [images/03-kromatika-b/primjer-3-111.png](images/03-kromatika-b/primjer-3-111.png) | cleanup_required / unapproved link |
| 48 | 3.112 | `primjer-3-112` | 222 | 112 left | [images/03-kromatika-b/primjer-3-112.png](images/03-kromatika-b/primjer-3-112.png) | cleanup_required / unapproved link |
| 49 | 3.113 | `primjer-3-113` | 222 | 112 left | [images/03-kromatika-b/primjer-3-113.png](images/03-kromatika-b/primjer-3-113.png) | cleanup_required / unapproved link |
| 50 | 3.114 | `primjer-3-114` | 222 | 112 left | [images/03-kromatika-b/primjer-3-114.png](images/03-kromatika-b/primjer-3-114.png) | PASS / embedded |
| 51 | 3.115 | `primjer-3-115` | 223 | 112 right | [images/03-kromatika-b/primjer-3-115.png](images/03-kromatika-b/primjer-3-115.png) | PASS / embedded |
| 52 | 3.116 | `primjer-3-116` | 223 | 112 right | [images/03-kromatika-b/primjer-3-116.png](images/03-kromatika-b/primjer-3-116.png) | PASS / embedded |

## Validation

- Post-write verification confirmed exactly the four assigned new files and unchanged SHA-256 values for every pre-existing repository file (excluding Git internals).
- 52 raw slot comments = 52 manifest records = 52 independent review records = 52 final records; stable ID, page, image and exact slot identity checked for each.
- 30 PASS records embedded; 22 RECROP_REQUIRED/source-limited records linked only as unapproved source crops. All 52 have captions, printed page references and MuseScore placeholders.
- All 52 chapter image/source-crop links resolve from the repository root. No blocked crop is rendered as an approved image.
- All 52 PNG sizes and decoded RGB pixels exactly equal their original source rectangle; the final manifest records each pixel SHA-256. Original pixels and rectangles were not changed.
- All 17 integrated source-page comments, and all 52 final records' PDF references and source paths, checked against `sources/index.json`; correct range 104–112.
- Removing precisely the added root heading and image blocks reconstructs the raw text exactly after only the two heading normalizations and eight PDF-comment fixes. No prose, footnote, instruction, attribution or continuation loss.
- No printed-page source block beyond 223 was added. No raw manifest, image, tracker, other worker output, commit or push was changed.

## Source limitations and readiness

No unreadable printed prose was reported in the verified text review. The 22 failed crops are source-limited: handwriting embedded in notation, overlapping adjacent material, or overlapping page-footer content prevents a clean intact single rectangular crop. Reasons are retained verbatim for each failed image in the final manifest and chapter; passing pixel provenance does not clear these failures. The 3.101 d–f source continuation lacks a repeated printed example number; this is documented rather than silently repaired.

This range is provisionally integrated and ready for parent hand-off, **not final publication approval**. Source-limited cleanup, fresh independent review after any authorized cleanup, human confirmation and remaining M06 pages are outstanding. No human approval was requested or claimed.

## Unmodified input SHA-256 values

- `review-candidates/book/M06/text-207-223.md`: `a1c6d1d659687cdbd998f8ed718cce4cb808509111d36f7d9fbf95e62fab4e48`
- `review-candidates/book/M06/text-207-223-review.json`: `6b2c7fb80331dd7f170d3c7a526f1adeda2610d65d0d96c8fe4981a47b732c93`
- `review-candidates/book/M06/images-207-223.json`: `ca6666c3a2247b1b2d0ac56ae7ba4b65ae3e5d2a88279a899867fdd6b2ba6939`
- `review-candidates/book/M06/visual-review-207-223.json`: `a24ae088bef5cbf3c107a9a0e5618cc880d2996843b7fcfc62408e054f4a1d9f`
- `sources/index.json`: `f8fd737535d4a9cb3469ecccb447bea4e94f7466a62c98fc3f09e58efe97594a`
