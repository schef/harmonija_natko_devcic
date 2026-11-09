# Independent visual review — M06, printed pages 224–240

## Result

**64/64 records reviewed: 62 PASS, 2 RECROP_REQUIRED. Not ready for integration because page-238 exercises 6/7 still fail.**

**Focused reassessment:** only records 35 (3.130b), 36 (3.130c) and 46 (3.139b) were freshly reassessed, with their paired first parts and source pages. All three now **PASS** under the explicitly clarified source-only multipart workflow. The original number must be retained on the first part; later parts retain their actual printed variant labels and complete content without fabricating a repeated number. The previous number-only rejections and combined-example proposal are withdrawn. The other 61 decisions, including both source-limited page-238 overlap failures, are unchanged; this update does not claim a fresh review of all 64.

Assigned manifest: `review-candidates/book/M06/images-224-240.json`.
Assigned printed pages: **224–240**; PDF spread pages: **113–121**.
All paths below are relative to the repository root. This review changed only:

- `review-candidates/book/M06/visual-review-224-240.json`
- `review-candidates/book/M06/visual-review-224-240.md`

No score images were extracted, edited, cleaned, retouched or approved by their extractor. No manifest, chapter, tracker, commit or push was changed. One independent worker performed the review without delegation or model subprocesses.

## Method and coordinate convention

- Visually compared every crop with its complete source page, then inspected every crop itself at native resolution, including all four edges. Reopened source-context strips for unusually tight/ambiguous boundaries, including the page-238 overlap.
- Checked example/exercise identifiers, variants, realization titles, printed composer/work attributions, staff starts/ends, clefs, key/time signatures, slurs/ties, brackets, figures and lowest stems.
- All **64 images are pixel-for-pixel identical** to their manifest rectangles in their declared source PNGs. Dimensions also match. Thus no artificial margin, resampling, copied ink or retouching was introduced into these crops.
- Checked every record's printed page, source path and PDF page against `sources/index.json`. **64/64 agree.** The index specifies lossless halves of 300-dpi PDF spreads. PDF linkage here is checked through that source index; the PDF was not independently rerendered.
- Rectangles are source-PNG pixels `[left, top, right, bottom]`, with right/bottom **exclusive**, origin at upper left. They are not coordinates in the two-page PDF spread.
- Small isolated scan dust is distinguished from identifiable foreign characters/notation. No partial foreign character, handwriting or neighbouring score fragment was accepted as harmless dust.
- PASS concerns the crop and its source identity. It does not assert that separately edited chapter alt text or links were reviewed: those files were outside this assignment.
- Focused reassessment reopened the three later-part crops at native resolution and sources on printed 232, 236 and 237, and freshly verified the original numbers in the paired first-part crops. Pixel equality with declared source rectangles was rechecked for all five involved crops. No new crop or temporary replacement was produced for this reassessment.
- Multipart identification follows the clarified established workflow: first part carries the original printed example number; subsequent source-only parts carry their actual printed variant labels and complete notation. An absent repeated number that is absent in the source is not a defect in a paired later part.

### Source-index mapping

| Printed page | PDF page | Source |
|---|---:|---|
| 224 | 113 | `sources/pages/page-224.png` |
| 225 | 113 | `sources/pages/page-225.png` |
| 226 | 114 | `sources/pages/page-226.png` |
| 227 | 114 | `sources/pages/page-227.png` |
| 228 | 115 | No records in assigned manifest |
| 229 | 115 | `sources/pages/page-229.png` |
| 230 | 116 | `sources/pages/page-230.png` |
| 231 | 116 | `sources/pages/page-231.png` |
| 232 | 117 | `sources/pages/page-232.png` |
| 233 | 117 | `sources/pages/page-233.png` |
| 234 | 118 | `sources/pages/page-234.png` |
| 235 | 118 | `sources/pages/page-235.png` |
| 236 | 119 | `sources/pages/page-236.png` |
| 237 | 119 | `sources/pages/page-237.png` |
| 238 | 120 | `sources/pages/page-238.png` |
| 239 | 120 | `sources/pages/page-239.png` |
| 240 | 121 | `sources/pages/page-240.png` |

## Focused multipart reassessment and remaining source limitations

### 3.130 b/c — PASS as paired later parts

Freshly compared records **35 and 36** with `sources/pages/page-232.png` (printed 232 / PDF 117), and with approved first-part record **34**, `images/03-kromatika-b/primjer-3-130-a.png`. The first-part crop visibly retains original printed **3.130**, a label, notation and analysis. Source page 232 establishes b and c as variants of that same numbered example, not new examples.

- **35 — `images/03-kromatika-b/primjer-3-130-b.png`: PASS.** Actual printed b) label and complete Mozart attribution are present. Both staves, clefs, accidentals, beams, rests, analytical figures, staff ends and lowest notes/stems match the source. All four edges are clean with genuine white margins; adjacent material is excluded. Rectangle `[150,630,1694,1089]` remains pixel-identical to source.
- **36 — `images/03-kromatika-b/primjer-3-130-c.png`: PASS.** Actual printed c) label and complete Schubert attribution are present. All notation, asterisks, slurs/ties, staff ends, lowest analytical accidental and final bass stem match source. All four edges are clean, including the narrow but intact bottom margin; the prose footnote is excluded. Rectangle `[154,1098,1695,1611]` remains pixel-identical to source.

The only previous rejection was lack of an artificially repeated number. Under the clarified multipart workflow, original 3.130 correctly remains on a. **No joining, replacement rectangle or added number is required or proposed.** The previous combined-example proposal has been removed from the JSON and is not an integration requirement. These are current-crop approvals, not approvals of a hypothetical replacement.

### Cross-page 3.139 b — PASS as paired cross-page part

Freshly compared record **46**, `images/03-kromatika-b/primjer-3-139-b.png`, with `sources/pages/page-237.png` (printed 237 / PDF 119), and paired first-part record **45**, `images/03-kromatika-b/primjer-3-139-a.png`, with `sources/pages/page-236.png` (printed 236 / PDF 119). First part visibly retains **3.139**, a), and the printed reference to b. The page-237 b) block is the actual cross-page reduction of measures 3/4 belonging to that same example.

**46 — PASS.** Actual b) and measure labels 3/4, all chord tones and accidentals, parenthetical spellings, both staff ends, analytical rows, lowest figures and bass stems are complete. All four native-resolution edges are clean with original whitespace and no body prose. Rectangle `[514,163,1469,747]` remains pixel-identical to source. Original 3.139 correctly remains on the paired a part; no repeated number, joining or transplantation is required. The previous number-only rejection is withdrawn. `source_limited=false`: normal cross-page numbering is not a source defect.

Record **45**, the a part on printed 236, passes: it includes number 3.139, both systems/measures 1–9, the bracket and printed reference to b, all figures and lowest bass stems. Chopin/Fantazija op.49 is named in the separate body paragraph above, not as a score-block attribution; importing that prose into the image would be inappropriate.

### Printed 238, exercises 6/7 — genuinely impossible clean single rectangles

Records **51 and 52** both fail for visible foreign notation at the shared edge, not merely for insufficient whitespace.

- Exercise 6's current rectangle is `[167,597,1688,1043]`. Its bottom includes the clipped top of exercise 7's upper accidental.
- Exercise 7's current rectangle is `[181,1016,1691,1169]`. Its top includes portions of exercise 6's lowest x/flat/natural figure rows.
- A low natural belonging to 6 occupies the source box **`[528,1004,541,1036]`**; intended 6 ink therefore extends through **y=1035**. Another low x sign is at `[349,1018,367,1035]`.
- The high parenthetical accidental belonging to 7 starts at **y=1025**. These are different horizontal positions, but both are within the staff widths that a complete rectangle must retain.
- A complete 6 rectangle needs exclusive bottom **at least 1036**; one excluding all 7 ink needs bottom **at most 1025**. A complete 7 rectangle needs top **at most 1025**; one excluding all 6 ink needs top **at least 1036**. Neither pair is satisfiable.

Both are **RECROP_REQUIRED, source_limited=true**. No `proposed_rect` is supplied because no complete, clean, single-source rectangle was found or can satisfy these bounds. Tightening an edge would clip intended content; shifting horizontally would lose staff content. Combining the two exercises would not meet the one-intended-example criterion. No retouching, masking, added border or partial-notation workaround is authorized here.

### Other source/tight-edge observations

- Record 24: the white interruptions within realization 12's lower staff are already present in the source scan. They are not crop damage; all outer boundaries pass. `source_limited=true` records this existing source defect, not a failed crop.
- Record 14: the lowest sharp ends at y=822, with two genuine white rows before exclusive bottom 825. It is tight but complete; no ink is clipped or foreign. PASS does not imply a large standardized margin.
- Records 13/20: isolated scan specks near a boundary were checked in context and are not partial characters or adjacent notation.
- Records 34/36/47/48/56: unusually close lowest figures/clef tails were specifically rechecked against source context in the original review. Intended content is complete. Record 36's native crop and paired first part were freshly reassessed for this update; record 36 now passes, including its narrow but intact bottom margin.
- Printed 238's right-margin handwriting is outside the passing exercise 8 and 12 crops.
- No intended notation was unreadable in a way that prevented the boundary decisions. No musical content was reconstructed or inferred to replace source ink.

## Complete record inventory

The JSON report gives each record's root-relative image path, decision, individual reason and source-limitation flag. No replacement rectangle is currently proposed. In the table below, **slot is the final two digits of the full record ID**; the full ID is also shown. Every listed rectangle was verified against the actual image pixels in the original review; five involved crops were rechecked for pixel equality in the focused reassessment. Only decisions 35, 36 and 46 changed.

| ID | Printed / PDF | Example or exercise | Source rectangle | Decision |
|---|---|---|---|---|
| M06-p224-slot-01 | 224 / 113 | 3.117 | `[154,118,1699,1030]` | PASS |
| M06-p224-slot-02 | 224 / 113 | 3.118 | `[167,1175,1699,1653]` | PASS |
| M06-p224-slot-03 | 224 / 113 | 3.119 | `[167,1777,1699,2341]` | PASS |
| M06-p225-slot-04 | 225 / 113 | 3.120 | `[212,143,1733,673]` | PASS |
| M06-p225-slot-05 | 225 / 113 | ZADACI 2 | `[225,950,1731,1163]` | PASS |
| M06-p225-slot-06 | 225 / 113 | ZADACI 3 | `[224,1192,1731,1383]` | PASS |
| M06-p225-slot-07 | 225 / 113 | ZADACI 4 | `[225,1416,1731,1630]` | PASS |
| M06-p225-slot-08 | 225 / 113 | ZADACI 5 | `[227,1657,1731,1878]` | PASS |
| M06-p225-slot-09 | 225 / 113 | ZADACI 6 | `[228,1898,1733,2108]` | PASS |
| M06-p225-slot-10 | 225 / 113 | ZADACI 7 | `[227,2135,1733,2254]` | PASS |
| M06-p226-slot-11 | 226 / 114 | ZADACI 8 | `[179,138,1691,264]` | PASS |
| M06-p226-slot-12 | 226 / 114 | ZADACI 9 | `[179,322,1691,440]` | PASS |
| M06-p226-slot-13 | 226 / 114 | ZADACI 10 | `[169,492,1691,631]` | PASS |
| M06-p226-slot-14 | 226 / 114 | ZADACI 11 | `[174,694,1691,825]` | PASS |
| M06-p226-slot-15 | 226 / 114 | ZADACI 12 | `[172,856,1691,1020]` | PASS |
| M06-p226-slot-16 | 226 / 114 | ZADACI 13 | `[172,1047,1691,1206]` | PASS |
| M06-p226-slot-17 | 226 / 114 | ZADACI 14 | `[170,1236,1691,1403]` | PASS |
| M06-p226-slot-18 | 226 / 114 | ZADACI 15 | `[167,1425,1691,1596]` | PASS |
| M06-p226-slot-19 | 226 / 114 | ZADACI 16 | `[170,1616,1691,1774]` | PASS |
| M06-p226-slot-20 | 226 / 114 | ZADACI 17 | `[170,1800,1691,1963]` | PASS |
| M06-p226-slot-21 | 226 / 114 | ZADACI 18 | `[170,1990,1691,2157]` | PASS |
| M06-p226-slot-22 | 226 / 114 | ZADACI 19 | `[163,2176,1691,2339]` | PASS |
| M06-p227-slot-23 | 227 / 114 | Realizacija zadatka 7 | `[211,107,1758,1016]` | PASS |
| M06-p227-slot-24 | 227 / 114 | Realizacija zadatka 12 | `[219,1302,1763,1804]` | PASS; existing source defect |
| M06-p229-slot-25 | 229 / 115 | 3.121 a/b | `[232,90,1738,381]` | PASS |
| M06-p229-slot-26 | 229 / 115 | 3.122 a/b | `[223,1057,1734,1553]` | PASS |
| M06-p229-slot-27 | 229 / 115 | 3.123 | `[515,1563,1430,2066]` | PASS |
| M06-p230-slot-28 | 230 / 116 | 3.124 | `[297,182,1516,627]` | PASS |
| M06-p230-slot-29 | 230 / 116 | 3.125 a/b/c | `[144,662,1682,1621]` | PASS |
| M06-p230-slot-30 | 230 / 116 | 3.126 | `[174,1969,944,2414]` | PASS |
| M06-p230-slot-31 | 230 / 116 | 3.127 a/b | `[958,1943,1685,2379]` | PASS |
| M06-p231-slot-32 | 231 / 116 | 3.128 a/b | `[255,787,1751,1067]` | PASS |
| M06-p231-slot-33 | 231 / 116 | 3.129 | `[420,1535,1570,2039]` | PASS |
| M06-p232-slot-34 | 232 / 117 | 3.130 a | `[558,168,1302,624]` | PASS |
| M06-p232-slot-35 | 232 / 117 | 3.130 b | `[150,630,1694,1089]` | PASS; paired with 34 |
| M06-p232-slot-36 | 232 / 117 | 3.130 c | `[154,1098,1695,1611]` | PASS; paired with 34 |
| M06-p232-slot-37 | 232 / 117 | 3.131 | `[580,1755,1262,2219]` | PASS |
| M06-p233-slot-38 | 233 / 117 | 3.132 a/b | `[223,391,1745,916]` | PASS |
| M06-p233-slot-39 | 233 / 117 | 3.133 | `[203,953,1747,1977]` | PASS |
| M06-p234-slot-40 | 234 / 118 | 3.134 a/b/c | `[163,169,1680,628]` | PASS |
| M06-p234-slot-41 | 234 / 118 | 3.135 a/b | `[124,887,1689,1868]` | PASS |
| M06-p235-slot-42 | 235 / 118 | 3.136 a-f | `[234,916,1749,1143]` | PASS |
| M06-p235-slot-43 | 235 / 118 | 3.137 a/b | `[223,1521,1745,2026]` | PASS |
| M06-p236-slot-44 | 236 / 119 | 3.138 a/b | `[160,280,1684,814]` | PASS |
| M06-p236-slot-45 | 236 / 119 | 3.139 a | `[133,1276,1676,2265]` | PASS |
| M06-p237-slot-46 | 237 / 119 | 3.139 b | `[514,163,1469,747]` | PASS; paired with 45 |
| M06-p237-slot-47 | 237 / 119 | ZADACI 2 | `[214,1976,1732,2217]` | PASS |
| M06-p237-slot-48 | 237 / 119 | ZADACI 3 | `[214,2219,1729,2435]` | PASS |
| M06-p238-slot-49 | 238 / 120 | ZADACI 4 | `[163,151,1679,366]` | PASS |
| M06-p238-slot-50 | 238 / 120 | ZADACI 5 | `[168,369,1681,589]` | PASS |
| M06-p238-slot-51 | 238 / 120 | ZADACI 6 | `[167,597,1688,1043]` | RECROP_REQUIRED: foreign 7 ink |
| M06-p238-slot-52 | 238 / 120 | ZADACI 7 | `[181,1016,1691,1169]` | RECROP_REQUIRED: foreign 6 ink |
| M06-p238-slot-53 | 238 / 120 | ZADACI 8 | `[186,1226,1694,1364]` | PASS |
| M06-p238-slot-54 | 238 / 120 | ZADACI 9 | `[186,1421,1694,1560]` | PASS |
| M06-p238-slot-55 | 238 / 120 | ZADACI 10 | `[180,1605,1699,1736]` | PASS |
| M06-p238-slot-56 | 238 / 120 | ZADACI 11 | `[185,1766,1703,2128]` | PASS |
| M06-p238-slot-57 | 238 / 120 | ZADACI 12 | `[184,2154,1708,2338]` | PASS |
| M06-p239-slot-58 | 239 / 120 | ZADACI 13 | `[206,128,1729,298]` | PASS |
| M06-p239-slot-59 | 239 / 120 | ZADACI 14 | `[206,324,1726,483]` | PASS |
| M06-p239-slot-60 | 239 / 120 | ZADACI 15 | `[206,506,1726,671]` | PASS |
| M06-p239-slot-61 | 239 / 120 | ZADACI 16 | `[206,693,1729,858]` | PASS |
| M06-p239-slot-62 | 239 / 120 | ZADACI 17 | `[201,889,1732,1253]` | PASS |
| M06-p239-slot-63 | 239 / 120 | Realizacija zadatka 7 | `[182,1450,1732,2357]` | PASS |
| M06-p240-slot-64 | 240 / 121 | Realizacija zadatka 11 | `[171,120,1713,1537]` | PASS |

## Hand-off

- Scope completed: all **64** assigned records on printed 224–240 / PDF 113–121; no records assigned on printed 228.
- Results after focused reassessment: **62 PASS / 2 RECROP_REQUIRED**, with no unreviewed records from the original 64-record assignment.
- Reassessed only records **35/36/46**, printed **232/237**, PDF **117/119**, against original source pages and paired first parts **34/45** on printed **232/236**. All three now pass as complete, clean source-only later parts; original numbers verified on first parts.
- No replacement crop is proposed for these passing parts. The earlier joining proposal is withdrawn; no number is to be added or transplanted.
- Remaining source-limited failures, unchanged: **51/52**, page-238 exercises 6/7's overlapping ink. No complete clean single rectangle resolves them.
- Existing source defect: realization 12 on printed 227; crop passes, source limitation documented.
- Ready for integration: **No**, pending resolution/review of the two remaining page-238 failures. This update applies the clarified multipart workflow, does not waive actual content/edge requirements, and does not request human approval. Only the existing two review reports were edited; no crops, manifests, chapters, trackers, commits or pushes were changed.
