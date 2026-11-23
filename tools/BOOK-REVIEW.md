# Book image review workspace

The book is prepared. Use this workspace to confirm passing images and handle
manual cleanup without hunting through folders or editing manifests.

```bash
python tools/review_book.py
```

Open **http://127.0.0.1:8765**. Use `--port 8766` if the default port is occupied.
The server listens on loopback only. Keep it running during a cleanup session;
Ctrl+C stops the viewer, but does not close a GIMP instance you opened.

## Confirming prepared images

The default view is **Passed — confirm**, with **Undecided only** enabled.
The crop appears beside the authoritative source scan. A red overlay marks the
crop's position on that scan; it does not alter image pixels. Toggle the overlay
off to inspect covered edges, or use **Focus source region** for native-size detail.
Click either image to open its PNG separately.

The finding shown above the images is taken from the existing independent review,
including the different metadata schemas used by earlier milestones. Chapter
context below the images shows the original Markdown for that printed page.

| Key | Action |
| --- | --- |
| `A` | Accept an independently passing original |
| `C` | Record that cleanup is needed |
| `R` | Record that recropping is needed |
| `X` | Reject |
| `U` | Undo the last decision made in this workspace |
| `←` / `→` | Previous / skip forward without a decision |
| `F` | Toggle native-size images |
| `G` | Open the separate cleanup working copy in GIMP, after confirmation |

Shortcuts do not run while typing into a note, search field or selector.
Notes are saved on disk with a decision. Unsubmitted draft notes, filters and
the current image are retained in this browser's local storage; they are not
cross-browser backups. Switching chapters, native size or filters does not
discard a draft. Undo retains a journal rather than silently destroying history.

**Acceptance is disabled for failed originals, source-damage holds and edited
snapshots.** A user confirmation does not rewrite independent-review evidence.
The server also checks that an accepted original still matches its reviewed
source rectangle; replacing a PNG externally cannot inherit its old pass.

## Find manageable cleanup work

Select **Cleanup / layout holds**, optionally narrow by chapter or printed page,
then choose an issue filter and **Suggested triage order**.

- **Handwriting**: review reasons mention handwritten ink. Records without other
  advisory flags sort ahead of overlapping/layout or notation problems.
- **Layout / adjacent ink**: another example, prose, punctuation or footer
  intrudes; erasing it may not be a safe or sufficient fix.
- **Notation needs judgment**: review mentions uncertain or obscured notation.
- **Inline glyph**: inspect the symbol in the surrounding sentence, including
  parentheses and punctuation already represented in the text.
- **Source damage — notation decision** has its own main view. These are not
  ordinary handwriting-removal jobs.

Tags are inferred suggestions, can overlap and never certify that editing is
easy or safe. The read-only report is
`review-candidates/book/REVIEW-WORKFLOW-AUDIT.md`.

## GIMP: copy → edit → export → close → review queue

1. Choose a case and read its exact finding beside the source.
2. Click **Open working copy in GIMP** (or `G`). This prepares a distinct
   `working.png` automatically and opens a **dedicated GIMP instance**.
   **Prepare working copy** alone creates the copy without launching a GUI.
3. Edit only the working copy. The original crop and source scan are not opened
   for editing by this workflow. Do not invent missing notation or erase a mark
   whose musical meaning is uncertain.
4. Export the edited PNG to the displayed **`working.png`**. An XCF may be saved
   alongside it, but saving only the XCF does not update the exported PNG.
5. Close the dedicated GIMP application when done. The viewer waits for that
   process to exit. A changed, valid exported PNG becomes a separate versioned
   snapshot marked **pending independent review**, with a content hash.
6. Review queued edits under **Edited copies awaiting review**. The source scan
   and original crop remain available for comparison. Accept remains disabled.

**The automatic part is copying, detecting editor exit, validating the export,
snapshotting and queueing—not running an AI reviewer or approving/integrating
the result.** The local viewer does not spend model quota or launch agents.
Tell the assistant **“Review the ready cleanup copies”** to run the required
separate visual review using the generated bundle. Passing edits can then be
integrated explicitly; no chapter path or image status is silently changed.

Only one dedicated cleanup editor may be open at a time. Closing just an image
tab while leaving that GIMP instance running does not signal completion.
If GIMP crashes, the viewer does not treat that as successful completion.

### If you restart the viewer or use another editor

An interrupted editor job is marked **interrupted**, never assumed finished.
Close the editor, export `working.png`, then click **Queue saved PNG for review**.
This also works for manual editing in another application. It does not approve
the copy. If no exported PNG changed, no new review revision is created.

Existing working copies, XCF files and revision snapshots are not overwritten by
preparation. Original-crop hash mismatches stop the job for provenance inspection.
Do not move cleanup files by hand while the viewer is running.

## Where progress is stored

All paths below are relative to the repository root:

| Path | Purpose |
| --- | --- |
| `review-candidates/book/human-review-state.json` | Human decisions and notes, compatible with the previous viewer |
| `review-candidates/book/human-review-history.json` | Decision journal and undo records |
| `review-candidates/book/cleanup-state.json` | Separate cleanup-job status and version history |
| `review-candidates/manual-cleanup/book/<job>/working.png` | Editable copy; optional XCF can live beside it |
| `review-candidates/manual-cleanup/book/<job>/candidate-*.png` | Snapshots for independent review; not regenerated over existing files |
| `review-candidates/book/cleanup-review-queue.json` | Machine-readable pending edited-copy review queue |
| `review-candidates/book/CLEANUP-REVIEW-READY.md` | Reviewer hand-off with exact paths, hashes, source pages and findings |

These runtime files are created only when you make decisions or prepare/edit a
working copy. Keep backups of them if migrating machines. Do not bulk-stage XCF
files, manual cleanup or human decisions into a book-preparation commit without
explicitly deciding what belongs in that commit.

## Checks and limitations

```bash
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tools/tests -v
node --check tools/review_book_assets/review.js
python tools/audit_book_review.py
```

The isolated tests cover the HTTP API, preservation guards, alternate metadata
schemas, undo, interrupted sessions, export snapshots and a real Chromium browser
session. The browser test uses a **fake GIMP process** on a temporary fixture, not
your images. A real interactive GIMP edit/export/close cycle still needs a user
smoke test on this desktop. The real queue was also rendered read-only without
writing decisions, working copies or changing source pixels.

Structural audits are not visual transcription verification. Edited copies are
intentionally not source-pixel-equal; they require genuine independent visual
comparison rather than an automated hash-equality approval.
