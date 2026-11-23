#!/usr/bin/env python3
"""Render local chapter previews without modifying Markdown or source images."""

import argparse
import html
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import urlsplit

import markdown


ROOT = Path(__file__).resolve().parents[1]
STYLE = """
body{font:18px/1.6 Georgia,serif;max-width:1100px;margin:30px auto;padding:0 24px;color:#202020}
nav,.source-page{font:14px/1.5 system-ui,sans-serif;background:#eef2f5;padding:8px 12px;margin:20px 0}
nav{position:sticky;top:0;z-index:1}img{max-width:100%;height:auto;vertical-align:middle}
img.glyph{max-height:3.5em;width:auto}table{border-collapse:collapse;width:100%;margin:20px 0}
th,td{border:1px solid #ccc;padding:6px 10px;text-align:left;vertical-align:top}
th{background:#f3f5f7}blockquote{border-left:5px solid #be7c20;background:#fff8e9;margin:18px 0;padding:8px 16px}
h1,h2,h3,h4{font-family:system-ui,sans-serif;line-height:1.3}.footnote{font-size:15px}
a{color:#155c96}code{font-size:14px;overflow-wrap:anywhere}.source-page{scroll-margin-top:65px}
"""


class LocalLinks(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=False)
        self.source = source
        self.parts = []

    def start(self, tag, attrs, close=False):
        rewritten = []
        glyph = False
        for key, value in attrs:
            if key in {"href", "src"} and value:
                target = urlsplit(value)
                if not target.scheme and not value.startswith("#"):
                    path = (self.source.parent / target.path).resolve()
                    if not path.is_relative_to(ROOT) or not path.is_file():
                        raise ValueError(f"Unresolved preview link in {self.source}: {value}")
                    glyph = tag == "img" and ("/dodaci/" in str(path) or path.name.startswith(("progresija-", "sifra-")))
                    value = path.as_uri() + (f"#{target.fragment}" if target.fragment else "")
            rewritten.append((key, value))
        if glyph:
            rewritten.append(("class", "glyph"))
        encoded = "".join(f' {key}="{html.escape(value, quote=True)}"' if value is not None else f" {key}" for key, value in rewritten)
        self.parts.append(f"<{tag}{encoded}{' /' if close else ''}>")

    def handle_starttag(self, tag, attrs):
        self.start(tag, attrs)

    def handle_startendtag(self, tag, attrs):
        self.start(tag, attrs, True)

    def handle_endtag(self, tag):
        self.parts.append(f"</{tag}>")

    def handle_data(self, data):
        self.parts.append(data)

    def handle_entityref(self, name):
        self.parts.append(f"&{name};")

    def handle_charref(self, name):
        self.parts.append(f"&#{name};")

    def handle_comment(self, data):
        self.parts.append(f"<!--{data}-->")


def render(source, output):
    text = source.read_text()
    text = re.sub(
        r"<!--\s*source-page:\s*(\d+);\s*pdf-page:\s*(\d+)\s*-->",
        lambda match: f'\n\n<div class="source-page" id="page-{int(match[1])}">Izvor: tiskana stranica {int(match[1])}; PDF stranica {int(match[2])}.</div>\n\n',
        text,
    )
    body = markdown.markdown(text, extensions=["tables", "footnotes", "fenced_code", "sane_lists"])
    parser = LocalLinks(source)
    parser.feed(body)
    title = html.escape(source.name)
    document = (f'<!doctype html><html lang="hr"><meta charset="utf-8"><title>{title}</title>'
                f'<style>{STYLE}</style><nav><a href="index.html">Pregled poglavlja</a> · {title} · '
                'Lokalni pregled — nije potvrda objave</nav>' + "".join(parser.parts) + "</html>")
    output.write_text(document)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("/tmp/opencode/harmonija-book-preview"))
    parser.add_argument("--chapter", action="append", help="Chapter basename; repeat to preview selected completed files")
    args = parser.parse_args()
    chapters = sorted((ROOT / "chapters").glob("*.md"))
    if args.chapter:
        requested = set(args.chapter)
        chapters = [path for path in chapters if path.name in requested]
        if {path.name for path in chapters} != requested:
            parser.error("A requested chapter file does not exist")
    args.output.mkdir(parents=True, exist_ok=True)
    links = []
    for chapter in chapters:
        destination = args.output / f"{chapter.stem}.html"
        render(chapter, destination)
        links.append(f'<li><a href="{html.escape(destination.name)}">{html.escape(chapter.name)}</a></li>')
    (args.output / "index.html").write_text(
        '<!doctype html><html lang="hr"><meta charset="utf-8"><title>Harmonija — lokalni pregled</title>'
        f'<style>{STYLE}</style><h1>Harmonija — lokalni pregled</h1>'
        '<p>Privremena integracija. Oznake PROVISIONAL i SOURCE DAMAGE nisu odobrenja slika ili notacije.</p><ul>'
        + "".join(links) + '</ul></html>'
    )
    print(f"Rendered {len(chapters)} chapters: {(args.output / 'index.html').resolve().as_uri()}")


if __name__ == "__main__":
    main()
