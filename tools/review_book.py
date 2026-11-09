#!/usr/bin/env python3
"""Serve the whole-book confirmation queue locally; never alter source images."""

import argparse
import json
from http.server import BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "review-candidates/book/review-queue.json"
STATE = ROOT / "review-candidates/book/human-review-state.json"
DECISIONS = {"accept", "recrop", "cleanup", "reject"}

HTML = """<!doctype html>
<html lang="en"><meta charset="utf-8"><title>Harmonija — image confirmation</title>
<style>
body{font:16px system-ui;margin:20px;background:#eee;color:#222}
header{position:sticky;top:0;background:#eee;padding:8px;z-index:1}
button,select,input{font:inherit;margin:4px;padding:6px}button{cursor:pointer}
.panes{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.pane{background:white;padding:12px;overflow:auto;max-height:78vh}
img{max-width:100%;height:auto} .pane img.full{max-width:none}
#message{white-space:pre-wrap}#note{width:60%}
</style>
<header><h2>Harmonija — confirm prepared images</h2>
<div id="progress"></div><div id="message"></div>
<button id="prev">← Previous</button><button id="next">Next →</button>
<button data-choice="accept">Accept</button><button data-choice="recrop">Needs recrop</button>
<button data-choice="cleanup">Needs GIMP cleanup</button><button data-choice="reject">Reject</button>
<label>View <select id="status-filter"><option value="independent_pass">Independently passed — confirm</option><option value="cleanup_required">Cleanup required</option><option value="pending_independent_review">Independent review pending</option><option value="all">All prepared images</option></select></label>
<label><input type="checkbox" id="pending" checked>Undecided only</label>
<label><input type="checkbox" id="full">Native-resolution images</label>
<input id="note" placeholder="Optional review note"><span id="saved"></span></header>
<div class="panes"><section class="pane"><h3 id="crop-title">Crop</h3><img id="crop"></section>
<section class="pane"><h3 id="source-title">Source page</h3><img id="source"></section></div>
<script>
let queue=[],state={},position=0,current=null;
const $=id=>document.getElementById(id);
function visible(){return queue.filter(x=>(!$('pending').checked||!state[x.id])&&($('status-filter').value==='all'||x.review_status===$('status-filter').value));}
function show(){const rows=visible();position=Math.max(0,Math.min(position,rows.length-1));
current=rows[position]||null;$('progress').textContent=`${Object.keys(state).length} decisions / ${queue.length} images; ${rows.length} in this view`;
if(!current){$('message').textContent='No images remain in this view. Uncheck Undecided only to revisit decisions.';$('crop').removeAttribute('src');$('source').removeAttribute('src');return;}
$('crop').src='/file/'+current.image;$('source').src='/file/'+current.source_image;
$('crop-title').textContent=current.example||current.id;
$('source-title').textContent=`Printed ${current.printed_page}, PDF ${current.pdf_page}; rectangle ${JSON.stringify(current.rect)}`;
$('message').textContent=`${current.milestone||''} · independent review: ${current.review_status||'pending'}\n${current.review_note||''}`;
$('note').value=state[current.id]?.note||'';$('saved').textContent=state[current.id]?.decision||'';}
async function decide(decision){if(!current)return;const response=await fetch('/api/decision',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({id:current.id,decision,note:$('note').value})});
if(!response.ok){alert(await response.text());return;}state=await response.json();if(!$('pending').checked)position++;show();}
document.querySelectorAll('[data-choice]').forEach(b=>b.onclick=()=>decide(b.dataset.choice));
$('prev').onclick=()=>{position--;show()};$('next').onclick=()=>{position++;show()};
$('pending').onchange=()=>{position=0;show()};$('full').onchange=()=>document.querySelectorAll('.pane img').forEach(i=>i.classList.toggle('full',$('full').checked));
$('status-filter').onchange=()=>{position=0;show()};
Promise.all([fetch('/api/queue').then(r=>r.json()),fetch('/api/state').then(r=>r.json())]).then(([q,s])=>{queue=q.records;state=s;show()}).catch(e=>$('message').textContent=String(e));
</script></html>"""


def load_json(path, default):
    return json.loads(path.read_text()) if path.is_file() else default


def safe_image(relative):
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT) or path.suffix.lower() != ".png":
        raise ValueError("Only repository PNG files may be viewed")
    if not path.is_file():
        raise ValueError("Image not found")
    return path


def validate_decision(payload, records):
    if not isinstance(payload, dict):
        raise ValueError("Expected a JSON object")
    if payload.get("id") not in {row["id"] for row in records}:
        raise ValueError("Unknown queue image")
    if payload.get("decision") not in DECISIONS:
        raise ValueError("Unknown decision")
    if not isinstance(payload.get("note", ""), str):
        raise ValueError("Note must be text")
    return {"decision": payload["decision"], "note": payload.get("note", "")}


class ReviewHandler(BaseHTTPRequestHandler):
    def send(self, status, body, content_type="application/json"):
        data = body if isinstance(body, bytes) else body.encode()
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        route = unquote(urlsplit(self.path).path)
        if route == "/":
            self.send(200, HTML, "text/html; charset=utf-8")
        elif route == "/api/queue":
            self.send(200, json.dumps(load_json(QUEUE, {"records": []})))
        elif route == "/api/state":
            self.send(200, json.dumps(load_json(STATE, {})))
        elif route.startswith("/file/"):
            try:
                self.send(200, safe_image(route[6:]).read_bytes(), "image/png")
            except ValueError as error:
                self.send(404, str(error), "text/plain")
        else:
            self.send(404, "Not found", "text/plain")

    def do_POST(self):
        if self.path != "/api/decision":
            self.send(404, "Not found", "text/plain")
            return
        # Only same-origin/local requests may write decisions.
        origin = self.headers.get("Origin")
        if origin and origin != f"http://{self.headers.get('Host')}":
            self.send(403, "Cross-origin writes are disabled", "text/plain")
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= 65536:
                raise ValueError("Invalid request size")
            payload = json.loads(self.rfile.read(length))
            records = load_json(QUEUE, {"records": []})["records"]
            decision = validate_decision(payload, records)
            state = load_json(STATE, {})
            state[payload["id"]] = decision
            STATE.parent.mkdir(parents=True, exist_ok=True)
            temporary = STATE.with_suffix(".json.tmp")
            temporary.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")
            temporary.replace(STATE)
            self.send(200, json.dumps(state))
        except (ValueError, KeyError) as error:
            self.send(400, str(error), "text/plain")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    if not QUEUE.is_file():
        parser.error("No consolidated queue yet: review-candidates/book/review-queue.json")
    # Single-threaded writes avoid concurrent state-file replacement races.
    from http.server import HTTPServer

    server = HTTPServer(("127.0.0.1", args.port), ReviewHandler)
    print(f"Open http://127.0.0.1:{args.port} — decisions save to {STATE.relative_to(ROOT)}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
