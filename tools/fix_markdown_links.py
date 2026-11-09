#!/usr/bin/env python3
"""Fix broken repository-root links in nested Markdown, without changing prose."""

import argparse
import os
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]]*\]\(([^)\n]+)\)")


def corrected_text(path):
    text = path.read_text()
    count = 0

    def replace(match):
        nonlocal count
        target = match.group(1)
        if target.startswith(("http://", "https://", "mailto:", "#", "/")):
            return match.group()
        filename, separator, fragment = target.partition("#")
        if (path.parent / filename).is_file():
            return match.group()
        source = (ROOT / filename).resolve()
        if not source.is_relative_to(ROOT) or not source.is_file():
            return match.group()
        relative = os.path.relpath(source, path.parent.resolve())
        replacement = relative + (separator + fragment if separator else "")
        start = match.start(1) - match.start()
        end = match.end(1) - match.start()
        count += 1
        return match.group()[:start] + replacement + match.group()[end:]

    return LINK.sub(replace, text), count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    total = 0
    for path in sorted((ROOT / "chapters").glob("*.md")):
        text, count = corrected_text(path)
        if count:
            if args.apply:
                path.write_text(text)
            print(f"{path.relative_to(ROOT)}: {count} {'corrected' if args.apply else 'need correction'}")
            total += count
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
