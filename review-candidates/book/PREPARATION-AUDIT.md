# Existing later-milestone assets — preliminary audit

Checked on 2026-11-22 while the single M07 reviewer was running. This is an
inventory and source-index check, **not independent approval of these crops**.

| Milestone | Existing provisional crop records | Pages represented | Missing image files | Incorrect source/PDF mappings |
| --- | ---: | ---: | ---: | ---: |
| M08, printed 277–308 | 103 | 31 | 0 | 0 |
| M09, printed 309–348 | No consolidated manifest | Not established | Not established | Not established |
| M10, printed 349–378 | 86 | 30 | 0 | 0 |
| M11, printed 379–411 | 44 | 9 | 0 | 0 |

- **M08:** printed page 279 has no crop record. The parent opened its source PNG
  and confirmed that it contains prose only, with no printed score or diagram.
  It still requires full prose transcription/verification with its surrounding
  paragraph continuation; absence from the crop manifest is not an omitted
  musical example.
- **M09:** full extraction/coverage work remains necessary; do not infer that a
  missing manifest means the source lacks examples.
  During the resumed M08 image-review/integration tasks, the parent text agent
  visually transcribed and verified pages **309–318** into three separate shards:
  `text-309-312.md`, `text-313-316.md`, and `text-317-318.md`, with matching
  per-page review JSON. These cover examples 4.53–4.75, exercises 1–9 and the
  realization of exercise 3, preserving the printed asterisk explanation and
  the joined 317/318 paragraph. Sequential text workers subsequently verified
  pages 319–333 and 334–348. All **40 M09 text pages and 134 visual slots** are
  now accounted for in those five shards and per-page review JSON. They remain
  text-only hand-offs, not chapter or image approvals; extraction and review
  must still include the last five pages absent from the old crop plan.
- **M10:** all 30 source pages have crop records, but this does not establish
  complete example coverage, correct individual bounds or independent review.
  All 86 original crops subsequently passed a mechanical source-pixel and
  source-index/PDF preflight; this is still not visual approval. The parent
  visually transcribed and verified pages 349–350 into `text-349-350.md` and
  its review JSON, preserving all seven score positions (4.143–4.149) and the
  printed asterisk explanation.
  The parent then verified pages 351–354 and 355–358 in their named text shards
  and review JSON. Combined parent coverage is now **ten pages 349–358 and 38
  visual parts**, including the page-specific continuations of 4.152 and
  exercises 8/11, every printed explanatory note, and all exercise instructions.
  The word škol-/skih, interrupted by image 4.151, was joined losslessly with
  the original layout interruption documented. Sequential text workers then
  verified **359–368** and **369–378**. All **30 M10 text pages and 86 visual
  slots** are now accounted for; crop coverage reconciliation and independent
  visual review remain separate and pending.
- **M11:** pages 388–411 have no crop records. The parent subsequently opened
  page 388 and confirmed it is blank apart from scan specks. Page 389 begins
  **USPOREDNI PREGLED TERMINA**, a two-column multilingual terminology list with
  an introductory paragraph and footnote 8; it belongs in the appendices, not
  the recap chapter. Its entries must be transcribed, not replaced by a full-page
  image. Pages 390–411 still require individual visual checks for all reference
  material and any meaningful visuals; they have not been assumed complete.

During subsequent resumed tasks, the parent transcribed and visually verified
**all terminology entries on pages 389–392**: 15, 22, 20 and 21 entries by page,
**78 entries total**, with footnote 8. The shards are `text-388-389.md` (including
the blank page), `text-390-391.md`, and `text-392.md`, each with review JSON.
Unusual printed foreign spellings were checked in enlarged native source details
and retained, not silently standardized. The parent also transcribed all **37
main/subentry and cross-reference rows** on page 393, beginning **INDEKS POJMOVA**,
into `text-393.md` and its review JSON. All printed-page references are retained
as source numbers, not converted to PDF numbers.

The parent subsequently opened and verified all nine pages **379–387** into
`text-379-387.md` and its review JSON, retaining **44 visual slots** matching the
old manifest's per-page counts: 19 exercise/realization parts and 25 inline
figured-bass symbols. The numbered recap chapter ends on page 385; the separate
unnumbered **OBILJEŽAVANJE AKORDA** starts the appendices on page 386 and
continues onto 387. Exact prose, labels, source punctuation and that cross-page
list continuation are retained. This does not approve any of the old crops.
The parent also verified page 394's **38 index rows** in `text-394.md` and its
review JSON, retaining the printed trailing comma in the dominanta dominante
references. Parent index coverage is now 75 main/subentry/cross-reference rows.
The parent additionally verified all **80 index rows on pages 395–396** in
`text-395-396.md` and its review JSON, preserving the continuation of izmjenični
ton subentries and all printed reference ranges.
The parent then verified pages 397–399 in `text-397-399.md` and review JSON,
retaining **112 additional index rows**, the long kvintakord/kvintni-krug lists,
and the cross-page modulacije hierarchy. No index reference was converted to PDF
numbering or silently normalized.
M11 text is now verified through **page 399**, including blank 388. The parent
also verified all **29 final contents entries on page 411** in `text-411.md`
and its review JSON, excluding the library stamp. Only **400–410** remains for
text work, suitable for one bounded eleven-page verification task. These
remaining index/name/contents pages must retain every
printed-page reference, not be summarized or replaced by scans.
The subsequent single text worker completed **400–410**, visually checking all
11 pages and transcribing **312 logical rows**. This confirms that the concept
index ends on 405, 406 is blank, the name index occupies 407–408, and contents starts on 409.
Together the ten text shards now cover **all 33 pages 379–411**, with all 44 visual
slots limited to 379–387. No later reference page requires a score-image crop.
The earlier pending-text descriptions above are historical; M11 text is complete
as a verified hand-off, not yet promoted to a finished appendix/chapter.
The old tiny-figure crops also need careful reconciliation with the inline prose:
`slika-386-1.png` visibly includes unrelated upper-right ink, and
`slika-386-2.png` includes a closing parenthesis while the verified text already
retains its surrounding parentheses. These are extraction hints, not review
decisions. Re-extract the intended figures from source with independently chosen
edges, retaining full strokes and avoiding duplicated prose punctuation; do not
paint pixels or silently approve the old glyph crops.

The preliminary M09 `extract.py` contains a wrong even-page PDF arithmetic
formula. Do not blindly run it or trust its metadata: use `sources/index.json`
and independently check each proposed source rectangle before promotion.
Its crop declarations end at printed page 343; pages 344–348 are not covered by
that partial plan and must be inspected explicitly. Several realization headings
were intentionally excluded in the old draft plan, which does not satisfy the
current image-identification checklist; new extraction must retain the printed
titles/identifiers where feasible or document the source-layout conflict.

Use authoritative `sources/index.json` for PDF-page mappings. Preserve the
existing source-only assets, verify text and slot coverage, and use a distinct
reviewer before promoting any image to independent-pass status.
# Final preparation outcome

The historical notes below describe incremental discoveries, not current gaps.
All remaining text and visual preparation through printed page 411 is now
provisionally integrated. The final queue has 1,206 parts: 870 passes, 333
cleanup/layout holds and three source-damage holds. No further extraction is
pending. See `review-candidates/book/PREPARATION-COMPLETE.md` and `STATUS.md`
for the final hand-off; no hold has been silently approved.
