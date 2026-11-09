# Integration: printed 101–118 / PDF 51–60

Appended only this assigned batch to `chapters/02-dijatonika-b.md`. The full pre-existing chapter through page 100, including historical stopping notes, is byte-for-byte unchanged. The new introduction supersedes the prior working boundary without altering it.

## Inputs and text preservation

- text: `review-candidates/book/M03/text-101-118.md`
- text_review: `review-candidates/book/M03/text-101-118-review.json`
- images: `review-candidates/book/M03/images-corrected-101-118.json`
- visual_review: `review-candidates/book/M03/visual-review-101-118.json`
- recrop_review: `review-candidates/book/M03/recrop-review-101-118.json`

All 18 text pages have verified=true. All prose, heading hierarchy, both asterisk footnotes, source-page markers, the paragraph continuing from page 104 to 105, prose interrupted by example 2.244, and the incomplete final paragraph continuing on page 119 are retained. Only numbered-heading spacing is normalized. No unreadable prose is reported; the printed reference “pr. 233.a” is preserved, not silently corrected.

## Results and validation

- Exactly 95 unique slots matched one-to-one by (printed_page, exact visual identity), never by list position alone.
- 61 approved images embedded: 56 original PASS + all five independently reviewed recrops. The final recrop review supersedes pending_recrop_review, and every recrop uses its approved `recrops/` path.
- 34 source-blocked images are not embedded or approved. Each has a visible PROVISIONAL / needs cleanup/review / cleanup_required / source_limited notice, original unapproved crop link, source-page link and independent reason.
- Every slot has its exact extraction caption, printed source-page reference and MuseScore placeholder.
- All chapter links resolve from the repository root; all crop rectangles are in source bounds; 95/95 decoded RGB crop images exactly equal their source rectangles. Per-image dimensions and decoded-pixel SHA-256 are recorded in `review-candidates/book/M03/images-integrated.json`. No image pixels were edited.
- Original 148 records preserved exactly; 95 appended as slots 149–243. Totals: 243 records, 128 independent_pass, 115 cleanup_required.
- Post-write validation also rechecked all 243 integrated crop rectangles, dimensions, decoded RGB pixels and stored SHA-256 hashes against their source pages: all pass. All links resolve in the chapter (325), appended review table (95) and this mapping report (95). Protected source manifests, source pages, crop files and `MILESTONES.md` retain their pre-write hashes.
- Pre-append chapter: 96201 bytes, SHA-256 `965200f865a937606f8b0d95b78a89134899e7316a060cdbb8a47b709f2b25b2`. Preserved prefix checked byte-for-byte. The prior REVIEW.md prefix is also byte-for-byte unchanged.

## Exact per-slot mapping

| Global slot | Batch slot | Exact visual identity | Printed / PDF | Integrated source crop | Final status |
| --- | --- | --- | --- | --- | --- |
| 149 | 1 | `p101:zadatak 4` | 101 / 51 | [zadatak-2-101-4.png](images/02-dijatonika-b/zadatak-2-101-4.png) | PASS / independent_pass |
| 150 | 2 | `p101:zadatak 5` | 101 / 51 | [zadatak-2-101-5.png](images/02-dijatonika-b/zadatak-2-101-5.png) | PASS / independent_pass |
| 151 | 3 | `p101:zadatak 6` | 101 / 51 | [zadatak-2-101-6.png](images/02-dijatonika-b/zadatak-2-101-6.png) | PASS / independent_pass |
| 152 | 4 | `p101:zadatak 7` | 101 / 51 | [zadatak-2-101-7.png](images/02-dijatonika-b/zadatak-2-101-7.png) | PASS / independent_pass |
| 153 | 5 | `p101:zadatak 8` | 101 / 51 | [zadatak-2-101-8.png](images/02-dijatonika-b/zadatak-2-101-8.png) | PASS / independent_pass |
| 154 | 6 | `p101:zadatak 9` | 101 / 51 | [zadatak-2-101-9.png](images/02-dijatonika-b/zadatak-2-101-9.png) | PASS / independent_pass |
| 155 | 7 | `p101:zadatak 10` | 101 / 51 | [zadatak-2-101-10.png](images/02-dijatonika-b/zadatak-2-101-10.png) | PASS / independent_pass |
| 156 | 8 | `p101:zadatak 11` | 101 / 51 | [zadatak-2-101-11.png](images/02-dijatonika-b/zadatak-2-101-11.png) | PASS / independent_pass |
| 157 | 9 | `p101:zadatak 12` | 101 / 51 | [zadatak-2-101-12.png](images/02-dijatonika-b/zadatak-2-101-12.png) | PASS / independent_pass |
| 158 | 10 | `p101:zadatak 13` | 101 / 51 | [zadatak-2-101-13.png](images/02-dijatonika-b/zadatak-2-101-13.png) | PASS / independent_pass |
| 159 | 11 | `p101:zadatak 14` | 101 / 51 | [zadatak-2-101-14.png](images/02-dijatonika-b/zadatak-2-101-14.png) | PASS / independent_pass |
| 160 | 12 | `p101:zadatak 15` | 101 / 51 | [zadatak-2-101-15.png](images/02-dijatonika-b/zadatak-2-101-15.png) | PASS / independent_pass |
| 161 | 13 | `p102:zadatak 16` | 102 / 52 | [zadatak-2-102-16.png](images/02-dijatonika-b/zadatak-2-102-16.png) | PASS / independent_pass |
| 162 | 14 | `p102:zadatak 17` | 102 / 52 | [zadatak-2-102-17.png](images/02-dijatonika-b/zadatak-2-102-17.png) | PASS / independent_pass |
| 163 | 15 | `p102:zadatak 18` | 102 / 52 | [zadatak-2-102-18.png](images/02-dijatonika-b/zadatak-2-102-18.png) | PASS / independent_pass |
| 164 | 16 | `p102:zadatak 19` | 102 / 52 | [zadatak-2-102-19.png](images/02-dijatonika-b/zadatak-2-102-19.png) | PASS / independent_pass |
| 165 | 17 | `p102:zadatak 20` | 102 / 52 | [zadatak-2-102-20.png](images/02-dijatonika-b/zadatak-2-102-20.png) | PASS / independent_pass |
| 166 | 18 | `p102:zadatak 21` | 102 / 52 | [zadatak-2-102-21.png](images/02-dijatonika-b/zadatak-2-102-21.png) | PASS / independent_pass |
| 167 | 19 | `p102:zadatak 22` | 102 / 52 | [zadatak-2-102-22.png](images/02-dijatonika-b/zadatak-2-102-22.png) | PASS / independent_pass |
| 168 | 20 | `p102:zadatak 23` | 102 / 52 | [zadatak-2-102-23.png](images/02-dijatonika-b/zadatak-2-102-23.png) | PASS / independent_pass |
| 169 | 21 | `p102:Realizacija zadatka 17 (početak)` | 102 / 52 | [zadatak-2-102-17-realizacija.png](images/02-dijatonika-b/zadatak-2-102-17-realizacija.png) | PASS / independent_pass |
| 170 | 22 | `p103:Realizacija zadatka 17 (nastavak)` | 103 / 52 | [zadatak-2-103-17-realizacija.png](images/02-dijatonika-b/zadatak-2-103-17-realizacija.png) | PASS / independent_pass |
| 171 | 23 | `p103:2.222` | 103 / 52 | [primjer-2-222.png](images/02-dijatonika-b/primjer-2-222.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 172 | 24 | `p103:2.223` | 103 / 52 | [primjer-2-223.png](images/02-dijatonika-b/primjer-2-223.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 173 | 25 | `p104:2.224` | 104 / 53 | [primjer-2-224.png](images/02-dijatonika-b/recrops/primjer-2-224.png) | PASS / independent_pass |
| 174 | 26 | `p104:2.225` | 104 / 53 | [primjer-2-225.png](images/02-dijatonika-b/primjer-2-225.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 175 | 27 | `p105:2.226` | 105 / 53 | [primjer-2-226.png](images/02-dijatonika-b/primjer-2-226.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 176 | 28 | `p105:2.227` | 105 / 53 | [primjer-2-227.png](images/02-dijatonika-b/primjer-2-227.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 177 | 29 | `p105:2.228` | 105 / 53 | [primjer-2-228.png](images/02-dijatonika-b/primjer-2-228.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 178 | 30 | `p106:2.229` | 106 / 54 | [primjer-2-229.png](images/02-dijatonika-b/recrops/primjer-2-229.png) | PASS / independent_pass |
| 179 | 31 | `p106:2.230` | 106 / 54 | [primjer-2-230.png](images/02-dijatonika-b/primjer-2-230.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 180 | 32 | `p106:2.231` | 106 / 54 | [primjer-2-231.png](images/02-dijatonika-b/primjer-2-231.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 181 | 33 | `p107:2.232` | 107 / 54 | [primjer-2-232.png](images/02-dijatonika-b/primjer-2-232.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 182 | 34 | `p107:2.233` | 107 / 54 | [primjer-2-233.png](images/02-dijatonika-b/primjer-2-233.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 183 | 35 | `p108:2.234` | 108 / 55 | [primjer-2-234.png](images/02-dijatonika-b/primjer-2-234.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 184 | 36 | `p108:2.235` | 108 / 55 | [primjer-2-235.png](images/02-dijatonika-b/primjer-2-235.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 185 | 37 | `p108:2.236` | 108 / 55 | [primjer-2-236.png](images/02-dijatonika-b/primjer-2-236.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 186 | 38 | `p108:2.237` | 108 / 55 | [primjer-2-237.png](images/02-dijatonika-b/primjer-2-237.png) | PASS / independent_pass |
| 187 | 39 | `p109:zadatak 1` | 109 / 55 | [zadatak-2-109-1.png](images/02-dijatonika-b/zadatak-2-109-1.png) | PASS / independent_pass |
| 188 | 40 | `p109:zadatak 2` | 109 / 55 | [zadatak-2-109-2.png](images/02-dijatonika-b/zadatak-2-109-2.png) | PASS / independent_pass |
| 189 | 41 | `p109:zadatak 3` | 109 / 55 | [zadatak-2-109-3.png](images/02-dijatonika-b/zadatak-2-109-3.png) | PASS / independent_pass |
| 190 | 42 | `p109:zadatak 4` | 109 / 55 | [zadatak-2-109-4.png](images/02-dijatonika-b/zadatak-2-109-4.png) | PASS / independent_pass |
| 191 | 43 | `p109:zadatak 5` | 109 / 55 | [zadatak-2-109-5.png](images/02-dijatonika-b/zadatak-2-109-5.png) | PASS / independent_pass |
| 192 | 44 | `p109:zadatak 6` | 109 / 55 | [zadatak-2-109-6.png](images/02-dijatonika-b/zadatak-2-109-6.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 193 | 45 | `p109:zadatak 7` | 109 / 55 | [zadatak-2-109-7.png](images/02-dijatonika-b/zadatak-2-109-7.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 194 | 46 | `p109:zadatak 8` | 109 / 55 | [zadatak-2-109-8.png](images/02-dijatonika-b/zadatak-2-109-8.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 195 | 47 | `p109:zadatak 9` | 109 / 55 | [zadatak-2-109-9.png](images/02-dijatonika-b/zadatak-2-109-9.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 196 | 48 | `p109:zadatak 10` | 109 / 55 | [zadatak-2-109-10.png](images/02-dijatonika-b/zadatak-2-109-10.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 197 | 49 | `p110:zadatak 11` | 110 / 56 | [zadatak-2-110-11.png](images/02-dijatonika-b/zadatak-2-110-11.png) | PASS / independent_pass |
| 198 | 50 | `p110:zadatak 12` | 110 / 56 | [zadatak-2-110-12.png](images/02-dijatonika-b/zadatak-2-110-12.png) | PASS / independent_pass |
| 199 | 51 | `p110:zadatak 13` | 110 / 56 | [zadatak-2-110-13.png](images/02-dijatonika-b/zadatak-2-110-13.png) | PASS / independent_pass |
| 200 | 52 | `p110:zadatak 14` | 110 / 56 | [zadatak-2-110-14.png](images/02-dijatonika-b/zadatak-2-110-14.png) | PASS / independent_pass |
| 201 | 53 | `p110:zadatak 15` | 110 / 56 | [zadatak-2-110-15.png](images/02-dijatonika-b/zadatak-2-110-15.png) | PASS / independent_pass |
| 202 | 54 | `p110:zadatak 16` | 110 / 56 | [zadatak-2-110-16.png](images/02-dijatonika-b/zadatak-2-110-16.png) | PASS / independent_pass |
| 203 | 55 | `p110:zadatak 17` | 110 / 56 | [zadatak-2-110-17.png](images/02-dijatonika-b/zadatak-2-110-17.png) | PASS / independent_pass |
| 204 | 56 | `p110:zadatak 18` | 110 / 56 | [zadatak-2-110-18.png](images/02-dijatonika-b/zadatak-2-110-18.png) | PASS / independent_pass |
| 205 | 57 | `p110:zadatak 19` | 110 / 56 | [zadatak-2-110-19.png](images/02-dijatonika-b/zadatak-2-110-19.png) | PASS / independent_pass |
| 206 | 58 | `p110:zadatak 20` | 110 / 56 | [zadatak-2-110-20.png](images/02-dijatonika-b/zadatak-2-110-20.png) | PASS / independent_pass |
| 207 | 59 | `p110:zadatak 21` | 110 / 56 | [zadatak-2-110-21.png](images/02-dijatonika-b/zadatak-2-110-21.png) | PASS / independent_pass |
| 208 | 60 | `p110:zadatak 22` | 110 / 56 | [zadatak-2-110-22.png](images/02-dijatonika-b/zadatak-2-110-22.png) | PASS / independent_pass |
| 209 | 61 | `p111:zadatak 23` | 111 / 56 | [zadatak-2-111-23.png](images/02-dijatonika-b/zadatak-2-111-23.png) | PASS / independent_pass |
| 210 | 62 | `p111:Realizacija zadatka 16` | 111 / 56 | [zadatak-2-111-16-realizacija.png](images/02-dijatonika-b/zadatak-2-111-16-realizacija.png) | PASS / independent_pass |
| 211 | 63 | `p111:2.238` | 111 / 56 | [primjer-2-238.png](images/02-dijatonika-b/primjer-2-238.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 212 | 64 | `p111:2.239` | 111 / 56 | [primjer-2-239.png](images/02-dijatonika-b/primjer-2-239.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 213 | 65 | `p112:2.240` | 112 / 57 | [primjer-2-240.png](images/02-dijatonika-b/primjer-2-240.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 214 | 66 | `p112:2.241` | 112 / 57 | [primjer-2-241.png](images/02-dijatonika-b/primjer-2-241.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 215 | 67 | `p112:2.242` | 112 / 57 | [primjer-2-242.png](images/02-dijatonika-b/primjer-2-242.png) | PASS / independent_pass |
| 216 | 68 | `p113:2.243` | 113 / 57 | [primjer-2-243.png](images/02-dijatonika-b/primjer-2-243.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 217 | 69 | `p113:zadatak 1` | 113 / 57 | [zadatak-2-113-1.png](images/02-dijatonika-b/zadatak-2-113-1.png) | PASS / independent_pass |
| 218 | 70 | `p113:zadatak 2` | 113 / 57 | [zadatak-2-113-2.png](images/02-dijatonika-b/zadatak-2-113-2.png) | PASS / independent_pass |
| 219 | 71 | `p113:zadatak 3` | 113 / 57 | [zadatak-2-113-3.png](images/02-dijatonika-b/zadatak-2-113-3.png) | PASS / independent_pass |
| 220 | 72 | `p113:zadatak 4` | 113 / 57 | [zadatak-2-113-4.png](images/02-dijatonika-b/zadatak-2-113-4.png) | PASS / independent_pass |
| 221 | 73 | `p113:zadatak 5` | 113 / 57 | [zadatak-2-113-5.png](images/02-dijatonika-b/zadatak-2-113-5.png) | PASS / independent_pass |
| 222 | 74 | `p113:zadatak 6` | 113 / 57 | [zadatak-2-113-6.png](images/02-dijatonika-b/zadatak-2-113-6.png) | PASS / independent_pass |
| 223 | 75 | `p113:zadatak 7` | 113 / 57 | [zadatak-2-113-7.png](images/02-dijatonika-b/zadatak-2-113-7.png) | PASS / independent_pass |
| 224 | 76 | `p114:Realizacija zadatka 4` | 114 / 58 | [zadatak-2-114-4-realizacija.png](images/02-dijatonika-b/zadatak-2-114-4-realizacija.png) | PASS / independent_pass |
| 225 | 77 | `p115:2.244` | 115 / 58 | [primjer-2-244.png](images/02-dijatonika-b/primjer-2-244.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 226 | 78 | `p115:2.245` | 115 / 58 | [primjer-2-245.png](images/02-dijatonika-b/primjer-2-245.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 227 | 79 | `p115:2.246` | 115 / 58 | [primjer-2-246.png](images/02-dijatonika-b/primjer-2-246.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 228 | 80 | `p116:2.247` | 116 / 59 | [primjer-2-247.png](images/02-dijatonika-b/primjer-2-247.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 229 | 81 | `p116:2.248` | 116 / 59 | [primjer-2-248.png](images/02-dijatonika-b/primjer-2-248.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 230 | 82 | `p116:2.249` | 116 / 59 | [primjer-2-249.png](images/02-dijatonika-b/primjer-2-249.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 231 | 83 | `p116:2.250` | 116 / 59 | [primjer-2-250.png](images/02-dijatonika-b/primjer-2-250.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 232 | 84 | `p116:2.251` | 116 / 59 | [primjer-2-251.png](images/02-dijatonika-b/primjer-2-251.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 233 | 85 | `p117:2.252` | 117 / 59 | [primjer-2-252.png](images/02-dijatonika-b/primjer-2-252.png) | PASS / independent_pass |
| 234 | 86 | `p117:zadatak 1` | 117 / 59 | [zadatak-2-117-1.png](images/02-dijatonika-b/recrops/zadatak-2-117-1.png) | PASS / independent_pass |
| 235 | 87 | `p117:zadatak 2` | 117 / 59 | [zadatak-2-117-2.png](images/02-dijatonika-b/zadatak-2-117-2.png) | PASS / independent_pass |
| 236 | 88 | `p117:zadatak 3` | 117 / 59 | [zadatak-2-117-3.png](images/02-dijatonika-b/recrops/zadatak-2-117-3.png) | PASS / independent_pass |
| 237 | 89 | `p117:zadatak 4` | 117 / 59 | [zadatak-2-117-4.png](images/02-dijatonika-b/zadatak-2-117-4.png) | PASS / independent_pass |
| 238 | 90 | `p117:zadatak 5` | 117 / 59 | [zadatak-2-117-5.png](images/02-dijatonika-b/recrops/zadatak-2-117-5.png) | PASS / independent_pass |
| 239 | 91 | `p117:zadatak 6` | 117 / 59 | [zadatak-2-117-6.png](images/02-dijatonika-b/zadatak-2-117-6.png) | PASS / independent_pass |
| 240 | 92 | `p117:Realizacija zadatka 4` | 117 / 59 | [zadatak-2-117-4-realizacija.png](images/02-dijatonika-b/zadatak-2-117-4-realizacija.png) | PASS / independent_pass |
| 241 | 93 | `p118:2.253` | 118 / 60 | [primjer-2-253.png](images/02-dijatonika-b/primjer-2-253.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 242 | 94 | `p118:2.254` | 118 / 60 | [primjer-2-254.png](images/02-dijatonika-b/primjer-2-254.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |
| 243 | 95 | `p118:2.255` | 118 / 60 | [primjer-2-255.png](images/02-dijatonika-b/primjer-2-255.png) | RECROP_REQUIRED / PROVISIONAL / source_limited / cleanup_required |

## Recrop decisions and margin qualification

- `p104:2.224`: **PASS**, `images/02-dijatonika-b/recrops/primjer-2-224.png`, rectangle `[182, 1400, 1707, 1595]`. Compared with source page 104 and inspected at native resolution, including all four edges. Number 2.224, variants a–d, all chords, accidentals, interval text and brackets, clef and staff ends are complete. The lower handwritten harmonic lettering is excluded without clipping the lowest notes. Genuine source margins remain on all sides (dark-content clearances left/top/right/bottom: 20/13/16/5 pixels). RGB mode, dimensions and every decoded pixel exactly match source rectangle [182,1400,1707,1595].
- `p106:2.229`: **PASS**, `images/02-dijatonika-b/recrops/primjer-2-229.png`, rectangle `[519, 103, 1268, 298]`. Compared with source page 106 and inspected at native resolution, including all four edges. The handwritten chord names above the example are excluded. Number 2.229, complete clef, key signature, chords, accidentals, staff ends and II7/IV7/VI7 labels remain. No surrounding prose or meaningful foreign edge marks appear. Genuine source margins remain (dark-content clearances left/top/right/bottom: 17/9/19/21 pixels). RGB mode, dimensions and every decoded pixel exactly match source rectangle [519,103,1268,298].
- `p117:zadatak 1`: **PASS**, `images/02-dijatonika-b/recrops/zadatak-2-117-1.png`, rectangle `[248, 687, 1763, 873]`. Compared with source page 117 and inspected at native resolution, including all four edges. The unrelated horizontal stroke above the staff is excluded. Exercise number 1, uppermost key-signature sharps, time signature, complete notation, final barline and every lowest stacked figure/accidental remain. Genuine source margins remain (dark-content clearances left/top/right/bottom: 17/6/16/9 pixels); no prose, page number or neighboring exercise is included. RGB mode, dimensions and every decoded pixel exactly match source rectangle [248,687,1763,873].
- `p117:zadatak 3`: **PASS**, `images/02-dijatonika-b/recrops/zadatak-2-117-3.png`, rectangle `[243, 1075, 1763, 1213]`. Compared with native-resolution source context and inspected on all four edges. Exercise number 3, clef, key/time signatures, complete slur, all notation and staff ends remain; exercise 2's bottom figure is completely excluded. Important margin qualification: there is NO full-width blank top row. The preceding figure's last dark pixels occur at source y=1074, while this exercise's slur first begins at y=1075, exactly the retained top row. Source inspection confirms no slur pixels are omitted above that boundary. Moving upward would introduce the preceding figure, and moving downward would clip the slur, so this is the natural source separation with no feasible clean top margin, not permission to add a border. Other dark-content clearances left/right/bottom are 18/8/7 pixels. RGB mode, dimensions and every decoded pixel exactly match source rectangle [243,1075,1763,1213].
- `p117:zadatak 5`: **PASS**, `images/02-dijatonika-b/recrops/zadatak-2-117-5.png`, rectangle `[261, 1434, 1763, 1609]`. Compared with source page 117 and inspected at native resolution, including all four edges. The lower-left foreign diagonal stroke is excluded. The entire number 5, clef, key/time signatures, slurs, ties, accidentals, notes, stems and final barline remain. Genuine source margins remain (dark-content clearances left/top/right/bottom: 5/3/16/15 pixels). Isolated small scan specks are not meaningful foreign lettering or handwriting. RGB mode, dimensions and every decoded pixel exactly match source rectangle [261,1434,1763,1609].

## Open issues and hand-off

All 34 remaining failures have source_limited=true and proposed_rect=null. Their exact per-image reasons are retained in the appended REVIEW.md table and integrated JSON. No safe complete clean alternative rectangle is established. Do not erase handwriting, clip notation, invent margins or approve these crops.

This batch is integrated provisionally through printed page 118 / PDF 60 only. Page 119 continuation is intentionally outside scope. **Not ready for final approval or milestone completion.** human_approved=false; milestone_complete=false; ready_for_final_integration=false.

Changed only:
- `chapters/02-dijatonika-b.md`
- `images/02-dijatonika-b/REVIEW.md` (append only)
- `review-candidates/book/M03/images-integrated.json` (95 records appended; aggregate metadata advanced)
- `review-candidates/book/M03/INTEGRATION-101-118.md`

No raw manifest, source image, crop image, shared tracker or milestone file edited. No delegation, model subprocess, API, GUI, commit or push.
