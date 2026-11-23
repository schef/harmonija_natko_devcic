'use strict';
const $ = id => document.getElementById(id);
const PREFS = 'harmonija-book-review-v2';
let queue = [], state = {}, jobs = {}, position = 0, current = null, busy = false, contextRequest = 0;
let drafts = {};
const controls = ['status-filter', 'chapter-filter', 'issue-filter', 'sort', 'page-filter', 'search', 'pending', 'full', 'highlight'];
const fileURL = path => '/file/' + path.split('/').map(encodeURIComponent).join('/');

async function api(path, payload) {
  const options = payload === undefined ? {} : {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(payload)};
  const response = await fetch(path, options);
  if (!response.ok) throw new Error(await response.text());
  return response.json();
}
function error(message = '') { $('error').textContent = message; }
function savePrefs() {
  const prefs = {id: current?.id, drafts};
  controls.forEach(id => prefs[id] = $(id).type === 'checkbox' ? $(id).checked : $(id).value);
  try { localStorage.setItem(PREFS, JSON.stringify(prefs)); } catch (_) { /* Disk decisions still persist. */ }
}
function restorePrefs() {
  let prefs = {};
  try { prefs = JSON.parse(localStorage.getItem(PREFS)) || {}; } catch (_) { /* Fresh preferences. */ }
  drafts = prefs.drafts && typeof prefs.drafts === 'object' ? prefs.drafts : {};
  controls.forEach(id => {
    if (prefs[id] === undefined) return;
    if ($(id).type === 'checkbox') $(id).checked = Boolean(prefs[id]);
    else if ($(id).tagName !== 'SELECT' || [...$(id).options].some(x => x.value === prefs[id])) $(id).value = prefs[id];
  });
  return prefs.id;
}
function rank(row) {
  const tags = row.triage_tags || [];
  if (tags.includes('source_damage')) return 5;
  if (tags.includes('notation_check')) return 4;
  if (tags.includes('layout')) return 3;
  if (tags.includes('inline_glyph')) return 2;
  if (tags.includes('handwriting')) return 1;
  return tags.includes('confirmation') ? 0 : 2.5;
}
function visible() {
  const search = $('search').value.trim().toLowerCase();
  const view = $('status-filter').value;
  let rows = queue.filter(row => {
    const ready = jobs[row.id]?.status === 'pending_independent_review';
    return (view === 'ready' ? ready : view === 'all' || row.review_status === view)
      && (view === 'ready' || !$('pending').checked || !state[row.id])
      && ($('chapter-filter').value === 'all' || row.milestone === $('chapter-filter').value)
      && ($('issue-filter').value === 'all' || row.triage_tags.includes($('issue-filter').value))
      && (!$('page-filter').value || row.printed_page === Number($('page-filter').value))
      && (!search || `${row.id} ${row.example || ''} ${row.review_note || ''} ${row.caption || ''}`.toLowerCase().includes(search));
  });
  if ($('sort').value === 'triage') rows = rows.slice().sort((a, b) => rank(a) - rank(b) || a.printed_page - b.printed_page);
  return rows;
}
function syncButtons() {
  document.querySelectorAll('[data-choice]').forEach(button => {
    button.disabled = busy || !current || (button.dataset.choice === 'accept' && (current.review_status !== 'independent_pass' || $('status-filter').value === 'ready'));
  });
  ['prepare', 'gimp', 'queue-saved'].forEach(id => $(id).disabled = busy || !current);
  if (current) {
    $('gimp').disabled ||= Object.values(jobs).some(job => ['editing', 'interrupted'].includes(job.status));
    $('queue-saved').disabled ||= !jobs[current.id] || jobs[current.id].status === 'editing';
  }
}
function sourceOverlay() {
  const image = $('source');
  const rect = current?.rect;
  $('source-rect').hidden = !$('highlight').checked || !rect || !image.naturalWidth;
  if (!image.naturalWidth || !rect) return;
  $('source-stage').style.width = $('full').checked ? image.naturalWidth + 'px' : '100%';
  Object.assign($('source-rect').style, {
    left: 100 * rect[0] / image.naturalWidth + '%', top: 100 * rect[1] / image.naturalHeight + '%',
    width: 100 * (rect[2] - rect[0]) / image.naturalWidth + '%', height: 100 * (rect[3] - rect[1]) / image.naturalHeight + '%'
  });
}
$('source').addEventListener('load', sourceOverlay);
$('focus-source').onclick = () => {
  if (!current || !$('source').naturalWidth) return;
  $('full').checked = true;
  document.querySelectorAll('.pane img').forEach(image => image.classList.add('full'));
  sourceOverlay(); savePrefs();
  const pane = $('source-pane');
  pane.scrollTop = $('source-stage').offsetTop - pane.offsetTop + current.rect[1] - 65;
  pane.scrollLeft = Math.max(0, current.rect[0] - 25);
};
async function showContext(row) {
  const request = ++contextRequest;
  $('context-text').textContent = 'Loading source-page context…';
  try {
    const result = await api('/api/context?id=' + encodeURIComponent(row.id));
    if (request !== contextRequest) return;
    $('context-label').textContent = `${result.chapter || 'No chapter recorded'} · printed page ${row.printed_page}${result.truncated ? ' · excerpt truncated' : ''}`;
    $('context-text').textContent = result.text;
  } catch (failure) { if (request === contextRequest) $('context-text').textContent = failure.message; }
}
function show(preferredID) {
  const rows = visible();
  if (preferredID) { const found = rows.findIndex(row => row.id === preferredID); if (found >= 0) position = found; }
  position = Math.max(0, Math.min(position, rows.length - 1));
  current = rows[position] || null;
  const done = queue.filter(row => state[row.id]).length;
  const counts = Object.values(state).reduce((acc, entry) => { acc[entry.decision] = (acc[entry.decision] || 0) + 1; return acc; }, {});
  const readyCount = Object.values(jobs).filter(job => job.status === 'pending_independent_review').length;
  $('progress').textContent = `${done} / ${queue.length} decisions · accepted ${counts.accept || 0} · cleanup ${counts.cleanup || 0} · recrop ${counts.recrop || 0} · rejected ${counts.reject || 0} · edited copies awaiting review ${readyCount} · view ${rows.length ? position + 1 : 0} / ${rows.length}`;
  syncButtons();
  if (!current) {
    ++contextRequest;
    $('crop-title').textContent = 'No images in this view';
    $('message').textContent = 'Try another view, clear filters, or uncheck Undecided only to revisit decisions.';
    ['crop', 'source', 'original'].forEach(id => $(id).removeAttribute('src'));
    $('source-rect').hidden = true;
    ['crop-link', 'source-link'].forEach(id => $(id).removeAttribute('href'));
    ['job', 'saved', 'context-text', 'context-label', 'note'].forEach(id => $(id).value !== undefined ? $(id).value = '' : $(id).textContent = '');
    return;
  }
  const job = jobs[current.id];
  const edited = $('status-filter').value === 'ready' && job?.candidate;
  const path = edited ? job.candidate : current.image;
  $('crop').src = fileURL(path); $('crop-link').href = fileURL(path);
  $('source').src = fileURL(current.source_image); $('source-link').href = fileURL(current.source_image);
  $('original-details').hidden = !edited;
  if (edited) $('original').src = fileURL(current.image); else $('original').removeAttribute('src');
  $('candidate-title').textContent = edited ? 'Edited snapshot — NOT independently approved' : 'Prepared crop';
  $('crop-title').textContent = current.caption || current.example || current.id;
  $('source-title').textContent = `Printed ${current.printed_page}, PDF ${current.pdf_page} · source rectangle ${JSON.stringify(current.rect)}`;
  $('message').textContent = `${current.id} · independent review: ${current.review_status}\nAdvisory tags: ${current.triage_tags.join(', ')}\n${current.review_note || ''}`;
  $('note').value = drafts[current.id] ?? state[current.id]?.note ?? '';
  $('saved').textContent = drafts[current.id] !== undefined ? 'Draft note — saved with next decision' : state[current.id] ? `Saved: ${state[current.id].decision}` : 'Undecided';
  $('job').textContent = job ? `Cleanup: ${job.status}\nExport PNG here: ${job.working}\n${job.candidate ? 'Review snapshot: ' + job.candidate + '\n' : ''}${job.error || job.last_result || ''}` : 'No working copy yet. Preparing a copy does not change the original or its approval.';
  document.querySelectorAll('.pane img').forEach(image => image.classList.toggle('full', $('full').checked));
  sourceOverlay();
  showContext(current); savePrefs();
}
async function action(task) {
  if (busy) return;
  busy = true; error(); syncButtons();
  try { await task(); } catch (failure) { error(failure.message); }
  finally { busy = false; syncButtons(); }
}
async function decide(decision) {
  if (!current || (decision === 'accept' && $('accept').disabled)) return;
  await action(async () => {
    const identity = current.id;
    state = await api('/api/decision', {id: identity, decision, note: $('note').value});
    delete drafts[identity];
    if (!$('pending').checked || $('status-filter').value === 'ready') position++;
    show();
  });
}
document.querySelectorAll('[data-choice]').forEach(button => button.onclick = () => decide(button.dataset.choice));
$('prev').onclick = () => { if (!busy) { position--; show(); } };
$('next').onclick = () => { if (!busy) { position++; show(); } };
$('undo').onclick = () => action(async () => {
  const result = await api('/api/undo', {}); state = result.state;
  const record = queue.find(row => row.id === result.id);
  if (record) { $('status-filter').value = record.review_status; $('chapter-filter').value = 'all'; $('issue-filter').value = 'all'; $('page-filter').value = ''; $('search').value = ''; }
  show(result.id);
});
controls.forEach(id => $(id).addEventListener('change', () => {
  const preferred = ['full', 'highlight'].includes(id) ? current?.id : null;
  if (!preferred) position = 0;
  show(preferred); savePrefs();
}));
$('search').addEventListener('input', () => { position = 0; show(); savePrefs(); });
$('note').addEventListener('input', () => {
  if (current) { drafts[current.id] = $('note').value; savePrefs(); $('saved').textContent = 'Draft note — saved with next decision'; }
});
async function cleanup(operation) {
  if (!current) return;
  if (operation === 'open' && !confirm('Open a separate GIMP instance on a WORKING COPY? Export to working.png and close that instance when finished. No image will be approved automatically.')) return;
  if (operation === 'queue' && !confirm('Is the editor closed and working.png exported? Queue a snapshot for independent review only?')) return;
  const identity = current.id;
  await action(async () => {
    await api('/api/cleanup/' + operation, {id: identity});
    jobs = await api('/api/jobs'); show(identity);
  });
}
$('prepare').onclick = () => cleanup('prepare'); $('gimp').onclick = () => cleanup('open'); $('queue-saved').onclick = () => cleanup('queue');
$('refresh').onclick = () => action(async () => { jobs = await api('/api/jobs'); show(current?.id); });
document.addEventListener('keydown', event => {
  if (event.defaultPrevented || event.altKey || event.ctrlKey || event.metaKey || /INPUT|TEXTAREA|SELECT/.test(event.target.tagName) || event.target.isContentEditable || busy) return;
  const key = event.key.toLowerCase();
  const choices = {a: 'accept', c: 'cleanup', r: 'recrop', x: 'reject'};
  if (choices[key]) { event.preventDefault(); decide(choices[key]); }
  else if (key === 'arrowleft' || key === 'arrowright') { event.preventDefault(); $(key === 'arrowleft' ? 'prev' : 'next').click(); }
  else if (key === 'u') { event.preventDefault(); $('undo').click(); }
  else if (key === 'g') { event.preventDefault(); if (!$('gimp').disabled) $('gimp').click(); }
  else if (key === 'f') { event.preventDefault(); $('full').checked = !$('full').checked; show(current?.id); }
});
Promise.all([api('/api/queue'), api('/api/state'), api('/api/jobs')]).then(([data, decisions, cleanupJobs]) => {
  queue = data.records; state = decisions; jobs = cleanupJobs;
  [...new Set(queue.map(row => row.milestone))].sort().forEach(name => {
    const option = document.createElement('option'); option.value = name; option.textContent = name; $('chapter-filter').append(option);
  });
  show(restorePrefs());
}).catch(failure => error(failure.message));
// Only refresh job metadata: never lose an in-progress note or change the current selection.
setInterval(async () => {
  if (busy || !Object.values(jobs).some(job => job.status === 'editing')) return;
  try {
    const updated = await api('/api/jobs');
    if (JSON.stringify(updated) !== JSON.stringify(jobs)) {
      const note = $('note').value; const identity = current?.id;
      jobs = updated; show(identity); if (current?.id === identity) $('note').value = note;
    }
  } catch (_) { /* Manual refresh reports errors explicitly. */ }
}, 3000);
