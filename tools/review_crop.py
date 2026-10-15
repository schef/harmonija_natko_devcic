#!/usr/bin/env python3
"""Interactively refine a score crop using only pixels from its source scan.

Usage: python tools/review_crop.py 2.48
"""

import argparse
import json
import re
import subprocess
import tkinter as tk
from pathlib import Path

import numpy as np
from PIL import Image, ImageTk


ROOT = Path(__file__).resolve().parents[1]
CACHE = Path("/tmp/opencode/harmonija-crop-review")
PDF = next(ROOT.glob("*.pdf"))
MANIFEST = ROOT / "tools" / "crop-locations.json"
HANDLE = 7


def example_paths(example):
    chapter, number = example.split(".", 1)
    assert chapter in {"1", "2"} and number.isdigit(), "Example must look like 2.48"
    section = "01-uvod" if chapter == "1" else "02-dijatonika-a"
    image = ROOT / "images" / section / f"primjer-{chapter}-{number}.png"
    markdown = ROOT / "chapters" / ("01-uvod.md" if chapter == "1" else "02-dijatonika-a.md")
    assert image.is_file(), f"Missing crop: {image}"
    return image, markdown


def listed_examples(chapter):
    markdown = ROOT / "chapters" / ("01-uvod.md" if chapter == "1" else "02-dijatonika-a.md")
    content = markdown.read_text()
    matches = re.findall(r"^\*Primjer " + re.escape(chapter) + r"\.(\d+)\..*?Izvor: tiskan[ae] stranic[ae] ([\d–-]+)", content, re.MULTILINE)
    assert matches, f"No examples found in {markdown}"
    return [(f"{chapter}.{number}", pages) for number, pages in matches]


def printed_page(markdown, example):
    content = markdown.read_text()
    match = re.search(rf"\*Primjer {re.escape(example)}\..*?Izvor: tiskan[ae] stranic[ae] (\d+)", content)
    assert match, f"No source-page caption found for example {example}"
    return int(match.group(1))


def pdf_page_for_printed_page(page):
    return (page if page % 2 == 0 else page - 1) // 2 + 1


def render_source(pdf_page, rerender):
    CACHE.mkdir(parents=True, exist_ok=True)
    output = CACHE / f"pdf-page-{pdf_page}-300dpi.png"
    if rerender or not output.is_file():
        subprocess.run(["pdftoppm", "-f", str(pdf_page), "-l", str(pdf_page), "-r", "300", "-png", "-singlefile", str(PDF), str(output.with_suffix(""))], check=True)
    return output


def suggested_rectangle(source, crop):
    scaled_source = source.with_name(f"{source.stem}-half.png")
    scaled_crop = CACHE / "match-template-half.png"
    if not scaled_source.is_file():
        subprocess.run(["magick", str(source), "-resize", "50%", str(scaled_source)], check=True)
    subprocess.run(["magick", str(crop), "-resize", "50%", str(scaled_crop)], check=True)
    result = subprocess.run(["magick", "compare", "-metric", "NCC", "-subimage-search", str(scaled_source), str(scaled_crop), "null:"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=False)
    match = re.search(r"@ (\d+),(\d+) \[([\d.]+)\]", result.stdout)
    assert match, f"Could not locate crop on source page:\n{result.stdout}"
    scaled_x, scaled_y, certainty = int(match.group(1)), int(match.group(2)), float(match.group(3))
    assert certainty > 0.90, f"Template match is uncertain ({certainty:.3f}); supply --pdf-page"
    with Image.open(crop) as image:
        width, height = image.size
    with Image.open(scaled_source) as image:
        scaled_width, scaled_height = image.size
    with Image.open(source) as image:
        source_width, source_height = image.size
    x, y = round(scaled_x * source_width / scaled_width), round(scaled_y * source_height / scaled_height)
    assert x + width <= source_width and y + height <= source_height, "Suggested crop falls outside the source page"
    return [x, y, x + width, y + height], certainty


def exact_rectangle(source, crop):
    result = subprocess.run(["magick", "compare", "-metric", "NCC", "-subimage-search", str(source), str(crop), "null:"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=False)
    match = re.search(r"@ (\d+),(\d+) \[([\d.]+)\]", result.stdout)
    assert match, f"Could not locate crop on source page:\n{result.stdout}"
    x, y, certainty = int(match.group(1)), int(match.group(2)), float(match.group(3))
    with Image.open(crop) as image:
        width, height = image.size
    with Image.open(source) as image:
        source_width, source_height = image.size
    assert x + width <= source_width and y + height <= source_height, "Exact crop match falls outside the source page"
    return [x, y, x + width, y + height], certainty


def coarse_rectangle(source, crop, scale=0.25):
    with Image.open(source) as image:
        source_width, source_height = image.size
        source_pixels = np.asarray(image.convert("L").resize((round(source_width * scale), round(source_height * scale)), Image.Resampling.LANCZOS), dtype=float)
    with Image.open(crop) as image:
        crop_width, crop_height = image.size
        crop_pixels = np.asarray(image.convert("L").resize((round(crop_width * scale), round(crop_height * scale)), Image.Resampling.LANCZOS), dtype=float)
    template = crop_pixels - crop_pixels.mean()
    template_height, template_width = template.shape
    assert template_height <= source_pixels.shape[0] and template_width <= source_pixels.shape[1], "Crop is larger than source page"
    shape = (source_pixels.shape[0] + template_height - 1, source_pixels.shape[1] + template_width - 1)
    axes = (0, 1)
    correlation = np.fft.irfftn(np.fft.rfftn(source_pixels, shape, axes=axes) * np.fft.rfftn(template[::-1, ::-1], shape, axes=axes), shape, axes=axes)
    correlation = correlation[template_height - 1:source_pixels.shape[0], template_width - 1:source_pixels.shape[1]]
    sums = np.pad(np.cumsum(np.cumsum(source_pixels, axis=0), axis=1), ((1, 0), (1, 0)))
    sums_squared = np.pad(np.cumsum(np.cumsum(source_pixels * source_pixels, axis=0), axis=1), ((1, 0), (1, 0)))
    total = sums[template_height:, template_width:] - sums[:-template_height, template_width:] - sums[template_height:, :-template_width] + sums[:-template_height, :-template_width]
    total_squared = sums_squared[template_height:, template_width:] - sums_squared[:-template_height, template_width:] - sums_squared[template_height:, :-template_width] + sums_squared[:-template_height, :-template_width]
    count = template_height * template_width
    denominator = np.sqrt(np.maximum(total_squared - total * total / count, 1) * np.sum(template * template))
    normalized = correlation / denominator
    y, x = np.unravel_index(np.argmax(normalized), normalized.shape)
    certainty = float(normalized[y, x])
    return [round(x / scale), round(y / scale), round(x / scale) + crop_width, round(y / scale) + crop_height], certainty


def manifest_key(image):
    return image.relative_to(ROOT).as_posix()


def read_manifest():
    assert MANIFEST.is_file(), f"Missing crop manifest: {MANIFEST}. Run python tools/build_crop_locations.py first."
    return json.loads(MANIFEST.read_text())


def write_manifest(manifest):
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")


class CropReview:
    def __init__(self, root, example, source_path, crop_path, rectangle, printed, pdf_page, manifest):
        self.root, self.example, self.crop_path = root, example, crop_path
        self.source = Image.open(source_path).convert("L")
        self.rectangle, self.printed, self.pdf_page, self.scale = rectangle, printed, pdf_page, 0.28
        self.manifest = manifest
        self.drag_target = None
        self.canvas = None
        self.preview_label = None
        self.status = tk.StringVar()
        self.build()
        self.redraw()

    def build(self):
        self.root.title(f"Crop review — example {self.example}")
        self.root.geometry("1560x980")
        controls = tk.Frame(self.root)
        controls.pack(fill="x", padx=8, pady=8)
        tk.Button(controls, text="− Zoom", command=lambda: self.change_zoom(0.8)).pack(side="left")
        tk.Button(controls, text="+ Zoom", command=lambda: self.change_zoom(1.25)).pack(side="left", padx=(4, 12))
        tk.Button(controls, text="Fit", command=self.fit).pack(side="left")
        tk.Button(controls, text="Save crop", command=self.save).pack(side="right")
        tk.Label(controls, text=f"Example {self.example} · printed page {self.printed} · PDF spread {self.pdf_page}").pack(side="left", padx=16)
        body = tk.PanedWindow(self.root, orient="horizontal", sashrelief="raised")
        body.pack(fill="both", expand=True, padx=8)
        source_frame, preview_frame = tk.Frame(body), tk.Frame(body, background="#ececec")
        body.add(source_frame, stretch="always")
        body.add(preview_frame, minsize=410)
        self.canvas = tk.Canvas(source_frame, background="#303030", highlightthickness=0)
        self.preview_label = tk.Label(preview_frame, background="#ececec", anchor="n")
        source_frame.rowconfigure(0, weight=1)
        source_frame.columnconfigure(0, weight=1)
        horizontal = tk.Scrollbar(source_frame, orient="horizontal", command=self.canvas.xview)
        vertical = tk.Scrollbar(source_frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(xscrollcommand=horizontal.set, yscrollcommand=vertical.set)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        vertical.grid(row=0, column=1, sticky="ns")
        horizontal.grid(row=1, column=0, sticky="ew")
        tk.Label(preview_frame, text="Saved crop preview", background="#ececec", font=("TkDefaultFont", 12, "bold")).pack(pady=(10, 6))
        self.preview_label.pack(fill="both", expand=True, padx=10, pady=10)
        tk.Label(self.root, textvariable=self.status, anchor="w").pack(fill="x", padx=12, pady=8)
        self.canvas.bind("<ButtonPress-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.drag)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drag)
        self.root.bind("<Return>", lambda event: self.save())
        self.root.bind("<Escape>", lambda event: self.root.destroy())
        self.root.bind("<plus>", lambda event: self.change_zoom(1.25))
        self.root.bind("<minus>", lambda event: self.change_zoom(0.8))
        self.root.bind("<Left>", lambda event: self.nudge(-1, 0))
        self.root.bind("<Right>", lambda event: self.nudge(1, 0))
        self.root.bind("<Up>", lambda event: self.nudge(0, -1))
        self.root.bind("<Down>", lambda event: self.nudge(0, 1))

    def fit(self):
        self.scale = min(0.30, 1050 / self.source.width, 820 / self.source.height)
        self.redraw()

    def change_zoom(self, factor):
        self.scale = min(1.0, max(0.08, self.scale * factor))
        self.redraw()

    def source_point(self, event):
        return int(self.canvas.canvasx(event.x) / self.scale), int(self.canvas.canvasy(event.y) / self.scale)

    def hit_target(self, x, y):
        left, top, right, bottom = self.rectangle
        corners = {"nw": (left, top), "ne": (right, top), "sw": (left, bottom), "se": (right, bottom)}
        target, (corner_x, corner_y) = min(corners.items(), key=lambda item: abs(item[1][0] - x) + abs(item[1][1] - y))
        if abs(corner_x - x) + abs(corner_y - y) <= 24 / self.scale:
            return target
        return "move" if left <= x <= right and top <= y <= bottom else None

    def start_drag(self, event):
        x, y = self.source_point(event)
        self.drag_target, self.drag_origin = self.hit_target(x, y), (x, y, self.rectangle.copy())

    def drag(self, event):
        if not self.drag_target:
            return
        x, y = self.source_point(event)
        origin_x, origin_y, original = self.drag_origin
        left, top, right, bottom = original
        if self.drag_target == "move":
            width, height = right - left, bottom - top
            left, top = max(0, min(self.source.width - width, left + x - origin_x)), max(0, min(self.source.height - height, top + y - origin_y))
            right, bottom = left + width, top + height
        else:
            if "w" in self.drag_target:
                left = max(0, min(x, right - 2))
            if "e" in self.drag_target:
                right = min(self.source.width, max(x, left + 2))
            if "n" in self.drag_target:
                top = max(0, min(y, bottom - 2))
            if "s" in self.drag_target:
                bottom = min(self.source.height, max(y, top + 2))
        self.rectangle = [left, top, right, bottom]
        self.redraw()

    def stop_drag(self, event):
        self.drag_target = None

    def nudge(self, dx, dy):
        left, top, right, bottom = self.rectangle
        width, height = right - left, bottom - top
        left, top = max(0, min(self.source.width - width, left + dx)), max(0, min(self.source.height - height, top + dy))
        self.rectangle = [left, top, left + width, top + height]
        self.redraw()

    def redraw(self):
        rendered = self.source.resize((int(self.source.width * self.scale), int(self.source.height * self.scale)), Image.Resampling.LANCZOS)
        self.display = ImageTk.PhotoImage(rendered)
        self.canvas.configure(width=rendered.width, height=rendered.height, scrollregion=(0, 0, rendered.width, rendered.height))
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.display, anchor="nw")
        left, top, right, bottom = [value * self.scale for value in self.rectangle]
        self.canvas.create_rectangle(left, top, right, bottom, outline="#00e5ff", width=3)
        for x, y in ((left, top), (right, top), (left, bottom), (right, bottom)):
            self.canvas.create_rectangle(x - HANDLE, y - HANDLE, x + HANDLE, y + HANDLE, fill="#00e5ff", outline="white")
        crop = self.source.crop(tuple(self.rectangle))
        factor = min(1, 440 / crop.width, 760 / crop.height)
        preview = crop.resize((max(1, int(crop.width * factor)), max(1, int(crop.height * factor))), Image.Resampling.LANCZOS)
        self.preview = ImageTk.PhotoImage(preview)
        self.preview_label.configure(image=self.preview)
        self.status.set(f"Crop: {self.rectangle[0]}, {self.rectangle[1]} → {self.rectangle[2]}, {self.rectangle[3]}  |  Drag rectangle to move; drag cyan corners to resize; Enter saves; Esc cancels.")

    def save(self):
        self.source.crop(tuple(self.rectangle)).save(self.crop_path)
        self.manifest["images"][manifest_key(self.crop_path)]["rect"] = self.rectangle
        self.manifest["images"][manifest_key(self.crop_path)]["pdf_page"] = self.pdf_page
        write_manifest(self.manifest)
        self.status.set(f"Saved exact source crop: {self.crop_path}")
        self.root.after(700, self.root.destroy)


def main():
    parser = argparse.ArgumentParser(description="Interactively review one Harmonija score crop.")
    parser.add_argument("example", nargs="?", help="Example number, for example 2.48")
    parser.add_argument("--list", choices=("1", "2"), metavar="CHAPTER", help="List available examples in a chapter")
    parser.add_argument("--compact", action="store_true", help="With --list, print space-separated example numbers only")
    args = parser.parse_args()
    if args.list:
        examples = listed_examples(args.list)
        if args.compact:
            print(" ".join(example for example, pages in examples))
        else:
            for example, pages in examples:
                print(f"{example:<6} printed source page {pages}")
        return
    assert args.example, "Supply an example number, or use --list 1 / --list 2"
    image, markdown = example_paths(args.example)
    printed = printed_page(markdown, args.example)
    manifest = read_manifest()
    entry = manifest["images"].get(manifest_key(image))
    assert entry, f"No manifest entry for {image}. Run python tools/build_crop_locations.py first."
    assert "source_image" in entry, "Crop locations have not been migrated. Run python tools/split_source_pages.py first."
    assert "rect_on_spread" not in entry, f"{args.example} crosses a source-page seam and needs manual resolution before interactive review."
    source = ROOT / entry["source_image"]
    assert source.is_file(), f"Missing source page: {source}. Run python tools/split_source_pages.py first."
    pdf_page = entry["pdf_page"]
    rectangle = entry["rect"]
    with Image.open(source) as source_image:
        width, height = source_image.size
    assert 0 <= rectangle[0] < rectangle[2] <= width and 0 <= rectangle[1] < rectangle[3] <= height, f"Stored rectangle for {args.example} falls outside {entry['source_page']}; review its manifest entry before saving."
    print(f"Loaded {args.example} from manifest at {rectangle} on {entry['source_page']} (PDF spread {pdf_page}).")
    root = tk.Tk()
    CropReview(root, args.example, source, image, rectangle, printed, pdf_page, manifest)
    root.mainloop()


if __name__ == "__main__":
    main()
