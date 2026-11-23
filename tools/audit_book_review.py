#!/usr/bin/env python3
"""Read-only structural checks and advisory triage summary for the prepared book."""

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import re

from book_review_workflow import review_reason, triage


ROOT = Path(__file__).resolve().parents[1]


def audit(root):
    root = Path(root).resolve()
    queue = json.loads((root / "review-candidates/book/review-queue.json").read_text())["records"]
    sources = json.loads((root / "sources/index.json").read_text())["pages"]
    index = {row["printed_page"]: row["pdf_page"] for row in sources if row["printed_page"] is not None}
    errors = []
    advisories = []
    counts = Counter()
    identifiers = Counter(row["id"] for row in queue)
    for identity, count in identifiers.items():
        if count != 1:
            errors.append(f"Duplicate queue ID: {identity}")
    for row in queue:
        if index.get(row["printed_page"]) != row["pdf_page"]:
            errors.append(f"Queue PDF mapping: {row['id']}")
        for key in ("image", "source_image"):
            if not (root / row[key]).is_file():
                errors.append(f"Missing queue file: {row['id']} / {key}")
        if not review_reason(row):
            errors.append(f"Missing review finding: {row['id']}")
    named_examples = set()
    for path in (root / "images").rglob("*.png"):
        match = re.match(r"primjer-(\d)-(\d+)(?:\D|$)", path.name)
        if match:
            named_examples.add(f"{match[1]}.{int(match[2])}")
    pages = Counter()
    reference_candidates = defaultdict(list)
    for chapter in sorted((root / "chapters").glob("*.md")):
        counts["chapters"] += 1
        text = chapter.read_text()
        relative = chapter.relative_to(root).as_posix()
        definitions = Counter(re.findall(r"^\[\^([^\]]+)\]:", text, re.M))
        references = Counter(re.findall(r"\[\^([^\]]+)\](?!:)", text))
        counts["footnote_definitions"] += sum(definitions.values())
        for key in references.keys() - definitions.keys():
            errors.append(f"Undefined footnote: {relative} / {key}")
        for key in definitions.keys() - references.keys():
            errors.append(f"Unreferenced footnote: {relative} / {key}")
        for key, count in definitions.items():
            if count > 1:
                errors.append(f"Duplicate footnote definition: {relative} / {key}")
        for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
            if target.startswith(("http://", "https://", "#")):
                continue
            counts["local_links"] += 1
            path = (chapter.parent / target.split("#")[0]).resolve()
            if not path.is_relative_to(root) or not path.is_file():
                errors.append(f"Broken/escaping local link: {relative} / {target}")
        for page, pdf in re.findall(r"source-page:\s*(\d+);\s*pdf-page:\s*(\d+)", text):
            page, pdf = int(page), int(pdf)
            if index.get(page) != pdf:
                errors.append(f"Chapter PDF mapping: {relative} / printed {page}")
            if 47 <= page <= 411:
                pages[page] += 1
        for number, line in enumerate(text.splitlines(), 1):
            if line.startswith(("[^", "<!--", "|")):
                continue
            for match in re.finditer(r"\b(?:pr\.|primjer(?:i|a|u|ima)?)\s+(\d\.\d{1,3})(?!\d)", line, re.I):
                counts["numbered_references"] += 1
                if match[1] not in named_examples:
                    reference_candidates[match[1]].append(f"{relative}:{number}")
    for page in range(47, 412):
        if pages[page] != 1:
            errors.append(f"Printed page {page} has {pages[page]} source markers; expected one")
    for example, locations in sorted(reference_candidates.items()):
        advisories.append(f"Reference {example} has no conventionally named PNG: {', '.join(locations)}")
    counts["source_pages_47_411"] = len(pages)
    statuses = Counter(row["review_status"] for row in queue)
    tags = Counter(tag for row in queue if row["review_status"] != "independent_pass" for tag in triage(row))
    handwriting_without_other_flags = [row["id"] for row in queue if triage(row) == ["handwriting"]]
    return {"checks": dict(counts), "queue_parts": len(queue), "statuses": dict(statuses),
            "advisory_tags_overlapping": dict(tags), "handwriting_only_suggestions": handwriting_without_other_flags,
            "errors": errors, "advisories": advisories}


def report(result):
    lines = ["# Review-workflow structural audit and triage", "",
             "Read-only checks. No text, pixels, review statuses or human decisions were changed.",
             "This is not a new visual review, a transcription certification or publication approval.", "",
             "## Structural checks", "", f"- Queue parts: **{result['queue_parts']}**"]
    lines.extend(f"- {key.replace('_', ' ')}: **{value}**" for key, value in result["checks"].items())
    lines.extend([f"- Structural errors: **{len(result['errors'])}**",
                  f"- Numbered-reference lookup exceptions: **{len(result['advisories'])}**", "",
                  "Footnote checks cover missing, duplicated and unused definitions. Numbered-reference",
                  "lookup checks the first example number in prose references against conventionally named",
                  "PNGs; it does not certify variants, range endpoints or printed anomalies.", "",
                  "## Advisory work queues", "",
                  "Tags are inferred from existing independent-review reasons and can overlap.",
                  "They do not establish that an edit is easy, safe or appropriate.", ""])
    lines.extend(f"- {key}: **{value}**" for key, value in result["advisory_tags_overlapping"].items())
    lines.extend(["", f"**{len(result['handwriting_only_suggestions'])}** records have a handwriting tag without another advisory tag.",
                  "Start with the viewer's Cleanup / layout holds view, Issue=Handwriting, Sort=Suggested triage order.",
                  "Inspect the source before removing ink; even handwriting-only suggestions are not editing authorization.", "",
                  "## Exceptions", ""])
    lines.extend(f"- {item}" for item in result["errors"] + result["advisories"])
    if not result["errors"] and not result["advisories"]:
        lines.append("No exceptions detected by these structural checks.")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, help="Write an explicit repository-local Markdown report")
    args = parser.parse_args()
    result = audit(ROOT)
    text = report(result)
    if args.report:
        path = (ROOT / args.report).resolve()
        if not path.is_relative_to(ROOT) or path.suffix != ".md":
            parser.error("Report must be a repository-local Markdown path")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        print(f"Wrote {path.relative_to(ROOT)}")
    else:
        print(text)
    raise SystemExit(1 if result["errors"] else 0)


if __name__ == "__main__":
    main()
