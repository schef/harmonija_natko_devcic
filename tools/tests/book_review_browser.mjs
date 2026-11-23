// Browser-level smoke test against an ISOLATED fixture server, never real decisions.
import assert from 'node:assert/strict';
import {spawn} from 'node:child_process';
import {existsSync, mkdtempSync, writeFileSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';

const [url, output] = process.argv.slice(2);
const profile = mkdtempSync(join(existsSync('/tmp/opencode') ? '/tmp/opencode' : tmpdir(), 'harmonija-browser-test-'));
const browser = spawn('chromium', ['--headless', '--no-sandbox', '--disable-gpu', '--disable-dev-shm-usage',
  '--no-first-run', '--remote-debugging-pipe', '--user-data-dir=' + profile, '--window-size=1500,1400'],
  {stdio: ['ignore', 'ignore', 'pipe', 'pipe', 'pipe']});
let sequence = 0, buffer = '';
const waiting = new Map();
const errors = [];
browser.stderr.on('data', () => {});
browser.stdio[4].on('data', data => {
  buffer += data.toString();
  let split;
  while ((split = buffer.indexOf('\0')) >= 0) {
    const raw = buffer.slice(0, split); buffer = buffer.slice(split + 1);
    if (!raw) continue;
    const message = JSON.parse(raw);
    if (message.id && waiting.has(message.id)) {
      const request = waiting.get(message.id); waiting.delete(message.id);
      clearTimeout(request.timeout);
      if (message.error) request.reject(new Error(JSON.stringify(message.error)));
      else request.resolve(message.result);
    }
    if (message.method === 'Runtime.exceptionThrown') errors.push(message.params.exceptionDetails.text);
  }
});
function call(method, params = {}, sessionId) {
  const id = ++sequence;
  return new Promise((resolve, reject) => {
    const timeout = setTimeout(() => { waiting.delete(id); reject(new Error('CDP timeout: ' + method)); }, 12000);
    waiting.set(id, {resolve, reject, timeout});
    browser.stdio[3].write(JSON.stringify({id, method, params, ...(sessionId ? {sessionId} : {})}) + '\0');
  });
}
let session;
async function evaluate(expression) {
  const response = await call('Runtime.evaluate', {expression, returnByValue: true, awaitPromise: true}, session);
  if (response.exceptionDetails) throw new Error(JSON.stringify(response.exceptionDetails));
  return response.result.value;
}
async function until(expression) {
  return evaluate(`new Promise((resolve,reject)=>{
    const started=Date.now();
    async function check(){try{if(await (${expression}))return resolve(true);}catch(_){}
      if(Date.now()-started>8000)return reject(new Error('Condition timed out'));
      setTimeout(check,30);
    }check();})`);
}
async function key(key) {
  await call('Input.dispatchKeyEvent', {type: 'keyDown', key}, session);
  await call('Input.dispatchKeyEvent', {type: 'keyUp', key}, session);
}
async function change(id, value) {
  await evaluate(`document.getElementById(${JSON.stringify(id)}).value=${JSON.stringify(value)};
    document.getElementById(${JSON.stringify(id)}).dispatchEvent(new Event('change'));`);
}
try {
  const target = await call('Target.createTarget', {url: 'about:blank'});
  session = (await call('Target.attachToTarget', {targetId: target.targetId, flatten: true})).sessionId;
  await call('Runtime.enable', {}, session);
  await call('Page.enable', {}, session);
  await call('Page.navigate', {url}, session);
  await until(`document.getElementById('progress')?.textContent.includes('decisions')`);
  assert.match(await evaluate(`document.getElementById('message').textContent`), /M11:one/);
  assert.equal(await evaluate(`document.getElementById('accept').disabled`), false);
  await until(`document.getElementById('context-text').textContent.includes('Context')`);
  await until(`document.getElementById('source').complete && document.getElementById('source').naturalWidth>0`);
  assert.equal(await evaluate(`document.getElementById('source-rect').hidden`), false);
  // Typing in note fields must never trigger review shortcuts.
  await evaluate(`document.getElementById('note').focus();document.getElementById('note').value='Draft čć';document.getElementById('note').dispatchEvent(new Event('input'));`);
  await key('a');
  assert.deepEqual(await evaluate(`fetch('/api/state').then(r=>r.json())`), {});
  await evaluate(`document.getElementById('note').blur()`);
  await key('f');
  assert.equal(await evaluate(`document.getElementById('note').value`), 'Draft čć');
  await key('a');
  await until(`document.getElementById('progress').textContent.startsWith('1 /')`);
  assert.equal((await evaluate(`fetch('/api/state').then(r=>r.json())`))['M11:one'].note, 'Draft čć');
  await key('u');
  await until(`document.getElementById('progress').textContent.startsWith('0 /')`);
  assert.match(await evaluate(`document.getElementById('message').textContent`), /M11:one/);
  await change('status-filter', 'cleanup_required');
  assert.equal(await evaluate(`document.getElementById('accept').disabled`), true);
  await key('a');
  assert.deepEqual(await evaluate(`fetch('/api/state').then(r=>r.json())`), {});
  await change('issue-filter', 'handwriting');
  assert.match(await evaluate(`document.getElementById('message').textContent`), /M11:blocked/);
  // Filters and current selection survive a reload.
  await call('Page.reload', {}, session);
  await until(`document.getElementById('message')?.textContent.includes('M11:blocked')`);
  assert.equal(await evaluate(`document.getElementById('issue-filter').value`), 'handwriting');
  await evaluate(`document.getElementById('prepare').click()`);
  await until(`document.getElementById('job').textContent.includes('Cleanup: prepared')`);
  // The fixture injects a fake GIMP process, exporting a changed PNG and exiting.
  await evaluate(`window.confirm=()=>true;document.getElementById('gimp').click()`);
  await until(`fetch('/api/jobs').then(r=>r.json()).then(j=>j['M11:blocked']?.status==='pending_independent_review')`);
  // Explicit refresh also works without waiting for the normal polling interval.
  await evaluate(`document.getElementById('refresh').click()`);
  await until(`document.getElementById('job').textContent.includes('pending_independent_review')`);
  await change('status-filter', 'ready');
  assert.match(await evaluate(`document.getElementById('candidate-title').textContent`), /NOT independently approved/);
  assert.equal(await evaluate(`document.getElementById('original-details').hidden`), false);
  assert.equal(await evaluate(`document.getElementById('accept').disabled`), true);
  await until(`document.getElementById('crop').complete && document.getElementById('crop').naturalWidth>0`);
  const screenshot = await call('Page.captureScreenshot', {format: 'png'}, session);
  writeFileSync(output, Buffer.from(screenshot.data, 'base64'));
  assert.deepEqual(errors, []);
  console.log('PASS: browser shortcuts, note safety, undo, filters/resume, context, working-copy/GIMP hand-off, edited-review gate and images.');
} finally {
  browser.kill('SIGTERM');
  for (const request of waiting.values()) clearTimeout(request.timeout);
}
