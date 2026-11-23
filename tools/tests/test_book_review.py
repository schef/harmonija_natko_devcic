"""Isolated tests: no real review decisions, source images, or GUI are touched."""

import hashlib
import http.client
import json
import sys
import tempfile
import threading
import unittest
from http.server import HTTPServer
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from book_review_workflow import CleanupWorkflow, fingerprint, load_json, review_reason, save_json, triage
from review_book import ReviewApp, ReviewHandler, safe_image, validate_decision
from audit_book_review import audit


class Fixture(unittest.TestCase):
    def setUp(self):
        scratch = '/tmp/opencode' if Path('/tmp/opencode').is_dir() else None
        self.temporary = tempfile.TemporaryDirectory(prefix='harmonija-review-test-', dir=scratch)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / 'images').mkdir()
        for name in ('crop', 'source'):
            Image.new('RGB', (30, 30), 'white').save(self.root / f'images/{name}.png')
        self.record = {'id': 'M11:one', 'image': 'images/crop.png', 'source_image': 'images/source.png',
                       'printed_page': 380, 'pdf_page': 191, 'review_status': 'independent_pass',
                       'rect': [0, 0, 30, 30],
                       'review_note': 'All four edges pass', 'milestone': 'M11',
                       'integration_output': 'chapters/test.md'}
        self.blocked = {**self.record, 'id': 'M11:blocked', 'review_status': 'cleanup_required',
                        'review_note': 'Handwriting overlaps adjacent prose; no safe separation'}
        (self.root / 'chapters').mkdir()
        (self.root / 'chapters/test.md').write_text(
            '<!-- source-page: 380; pdf-page: 191 -->\nContext čćžšđ\n'
            '<!-- source-page: 381; pdf-page: 191 -->\nAnother page\n')
        save_json(self.root / 'review-candidates/book/review-queue.json', {'records': [self.record, self.blocked]})


class WorkflowTests(Fixture):
    def test_prepare_idempotent_and_preserves_original(self):
        workflow = CleanupWorkflow(self.root)
        original_hash = fingerprint(self.root / self.record['image'])
        first = workflow.prepare(self.record)
        working = self.root / first['working']
        Image.new('RGB', (25, 25), 'gray').save(working)
        second = workflow.prepare(self.record)
        self.assertEqual(first['working'], second['working'])
        self.assertNotEqual(fingerprint(working), original_hash)
        self.assertEqual(fingerprint(self.root / self.record['image']), original_hash)
        self.assertFalse((self.root / 'review-candidates/book/human-review-state.json').exists())

    def test_orphaned_cleanup_files_never_overwritten(self):
        workflow = CleanupWorkflow(self.root)
        token = hashlib.sha256(self.record['id'].encode()).hexdigest()[:20]
        folder = self.root / f'review-candidates/manual-cleanup/book/{token}'
        folder.mkdir(parents=True)
        note = folder / 'INSTRUCTIONS.md'
        note.write_text('User work')
        with self.assertRaisesRegex(ValueError, 'already contains files'):
            workflow.prepare(self.record)
        self.assertEqual(note.read_text(), 'User work')

    def test_changed_exports_snapshot_not_approve(self):
        workflow = CleanupWorkflow(self.root)
        job = workflow.prepare(self.record)
        original = fingerprint(self.root / self.record['image'])
        Image.new('RGB', (25, 28), 'gray').save(self.root / job['working'])
        queued = workflow.queue_saved(self.record['id'])
        self.assertEqual(queued['status'], 'pending_independent_review')
        self.assertEqual(queued['candidate_size'], [25, 28])
        self.assertEqual(fingerprint(self.root / queued['candidate']), queued['candidate_sha256'])
        snapshot = (self.root / queued['candidate']).read_bytes()
        Image.new('RGB', (20, 20), 'black').save(self.root / job['working'])
        self.assertEqual((self.root / queued['candidate']).read_bytes(), snapshot)
        second = workflow.queue_saved(self.record['id'])
        self.assertEqual(len(second['history']), 2)
        self.assertEqual(fingerprint(self.root / self.record['image']), original)
        bundle = (self.root / 'review-candidates/book/CLEANUP-REVIEW-READY.md').read_text()
        self.assertIn('NOT approved', bundle)
        self.assertIn(second['candidate_sha256'], bundle)
        machine_queue = load_json(self.root / 'review-candidates/book/cleanup-review-queue.json', {})
        self.assertFalse(machine_queue['records'][0]['approved'])
        self.assertFalse(machine_queue['records'][0]['source_pixel_equality_expected'])
        self.assertFalse((self.root / 'review-candidates/book/human-review-state.json').exists())

    def test_unchanged_does_not_queue(self):
        workflow = CleanupWorkflow(self.root)
        workflow.prepare(self.record)
        job = workflow.queue_saved(self.record['id'])
        self.assertEqual(job['history'], [])
        self.assertNotEqual(job['status'], 'pending_independent_review')

    def test_original_tampering_blocks_review(self):
        workflow = CleanupWorkflow(self.root)
        workflow.prepare(self.record)
        Image.new('RGB', (30, 30), 'black').save(self.root / self.record['image'])
        with self.assertRaisesRegex(ValueError, 'Original crop changed'):
            workflow.queue_saved(self.record['id'])

    def test_invalid_png_blocks_review(self):
        workflow = CleanupWorkflow(self.root)
        job = workflow.prepare(self.record)
        Image.new('RGB', (25, 25), 'gray').save(self.root / job['working'], format='JPEG')
        with self.assertRaisesRegex(ValueError, 'actual PNG'):
            workflow.queue_saved(self.record['id'])

    def test_recover_does_not_guess_editor_closed(self):
        workflow = CleanupWorkflow(self.root)
        job = workflow.prepare(self.record)
        state = workflow.state()
        state[job['id']]['status'] = 'editing'
        save_json(workflow.state_path, state)
        workflow.recover()
        self.assertEqual(workflow.state()[job['id']]['status'], 'interrupted')
        self.assertEqual(workflow.state()[job['id']]['history'], [])
        with self.assertRaisesRegex(ValueError, 'state is unknown'):
            workflow.start(self.record)
        workflow.queue_saved(job['id'])
        self.assertNotEqual(workflow.state()[job['id']]['status'], 'interrupted')

    def test_editor_exit_queues_changed_png(self):
        workflow = CleanupWorkflow(self.root)
        job = workflow.prepare(self.record)
        before = fingerprint(self.root / job['working'])
        Image.new('RGB', (30, 30), 'gray').save(self.root / job['working'])
        class Process:
            def wait(self): return 0
        workflow.active.add(job['id'])
        workflow._watch(job['id'], Process(), before)
        self.assertEqual(workflow.state()[job['id']]['status'], 'pending_independent_review')
        self.assertFalse(workflow.active)

    def test_editor_failure_never_queues(self):
        workflow = CleanupWorkflow(self.root)
        job = workflow.prepare(self.record)
        class Process:
            def wait(self): return 2
        workflow._watch(job['id'], Process(), fingerprint(self.root / job['working']))
        self.assertEqual(workflow.state()[job['id']]['status'], 'editor_error')
        self.assertEqual(workflow.state()[job['id']]['history'], [])

    def test_path_escape_rejected(self):
        workflow = CleanupWorkflow(self.root)
        for path in ('../outside.png', '/etc/passwd'):
            with self.assertRaises(ValueError): workflow.inside(path)
        with self.assertRaises(ValueError): safe_image('../outside.png', self.root)

    def test_working_link_to_original_rejected(self):
        workflow = CleanupWorkflow(self.root)
        job = workflow.prepare(self.record)
        working = self.root / job['working']
        working.unlink()
        working.hardlink_to(self.root / self.record['image'])
        with self.assertRaisesRegex(ValueError, 'cannot be an original'):
            workflow.queue_saved(job['id'])

    def test_triage_is_advisory(self):
        self.assertEqual(triage(self.record), ['confirmation'])
        self.assertIn('handwriting', triage(self.blocked))
        self.assertIn('layout', triage(self.blocked))
        self.assertEqual(triage({**self.blocked, 'review_status': 'source_damage'}), ['source_damage'])
        self.assertNotIn('handwriting', triage({**self.blocked, 'review_note': 'No handwriting visible; adjacent prose retained'}))
        self.assertEqual(self.blocked['review_status'], 'cleanup_required')

    def test_alternate_manifest_reason_schemas(self):
        row = {**self.blocked, 'review_reason': 'Pencil handwriting remains', 'review_note': ''}
        self.assertEqual(review_reason(row), 'Pencil handwriting remains')
        self.assertIn('handwriting', triage(row))


class AppTests(Fixture):
    def test_accept_gate_and_backward_compatible_state(self):
        app = ReviewApp(self.root)
        state = app.decide({'id': self.record['id'], 'decision': 'accept', 'note': 'čitko'})
        self.assertEqual(state[self.record['id']], {'decision': 'accept', 'note': 'čitko'})
        with self.assertRaises(ValueError): app.decide({'id': self.blocked['id'], 'decision': 'accept'})
        with self.assertRaises(ValueError): validate_decision({'id': self.record['id'], 'decision': 'bad'}, app.records())
        with self.assertRaises(ValueError): validate_decision({'id': self.record['id'], 'decision': 'accept', 'note': 7}, app.records())

    def test_externally_changed_original_cannot_inherit_pass(self):
        app = ReviewApp(self.root)
        Image.new('RGB', (30, 30), 'gray').save(self.root / self.record['image'])
        with self.assertRaisesRegex(ValueError, 'no longer matches'):
            app.decide({'id': self.record['id'], 'decision': 'accept'})
        self.assertFalse(app.state_path.exists())

    def test_undo_preserves_previous_decisions_and_journal(self):
        app = ReviewApp(self.root)
        save_json(app.state_path, {self.record['id']: {'decision': 'cleanup', 'note': 'old'}})
        app.decide({'id': self.record['id'], 'decision': 'accept'})
        result = app.undo()
        self.assertEqual(result['state'][self.record['id']]['note'], 'old')
        self.assertIn('undone_at', load_json(app.history_path, [])[0])
        with self.assertRaises(ValueError): app.undo()

    def test_undo_removes_only_new_decision(self):
        app = ReviewApp(self.root)
        app.decide({'id': self.record['id'], 'decision': 'accept'})
        self.assertEqual(app.undo()['state'], {})

    def test_context_is_source_page_scoped(self):
        context = ReviewApp(self.root).context(self.record['id'])
        self.assertIn('Context čćžšđ', context['text'])
        self.assertNotIn('Another page', context['text'])

    def test_alternate_chapter_field_schemas(self):
        app = ReviewApp(self.root)
        for key in ('chapter', 'chapter_path'):
            row = {k: v for k, v in self.record.items() if k != 'integration_output'}
            row[key] = 'chapters/test.md'
            save_json(app.queue_path, {'records': [row]})
            self.assertIn('Context', app.context(row['id'])['text'])


class AuditTests(Fixture):
    def prepare_book(self):
        save_json(self.root / 'sources/index.json', {'pages': [
            {'printed_page': page, 'pdf_page': page // 2 + 1} for page in range(47, 412)
        ]})
        chapter = self.root / 'chapters/test.md'
        chapter.write_text('\n'.join(f'<!-- source-page: {page}; pdf-page: {page // 2 + 1} -->' for page in range(47, 412)))
        return chapter

    def test_structural_pass(self):
        self.prepare_book()
        result = audit(self.root)
        self.assertEqual(result['errors'], [])
        self.assertEqual(result['checks']['source_pages_47_411'], 365)
        self.assertEqual(result['queue_parts'], 2)

    def test_footnote_and_reference_exceptions(self):
        chapter = self.prepare_book()
        chapter.write_text(chapter.read_text() + '\nUnresolved[^missing]. Primjer 4.999.\n[^unused]: unused\n')
        result = audit(self.root)
        self.assertTrue(any('Undefined footnote' in e for e in result['errors']))
        self.assertTrue(any('Unreferenced footnote' in e for e in result['errors']))
        self.assertEqual(len(result['advisories']), 1)

    def test_duplicate_source_marker(self):
        chapter = self.prepare_book()
        chapter.write_text(chapter.read_text() + '\n<!-- source-page: 380; pdf-page: 191 -->\n')
        self.assertTrue(any('380 has 2 source markers' in e for e in audit(self.root)['errors']))


class HTTPTests(Fixture):
    def setUp(self):
        super().setUp()
        class QuietHandler(ReviewHandler):
            def log_message(self, *args): pass
        self.server = HTTPServer(('127.0.0.1', 0), QuietHandler)
        self.server.app = ReviewApp(self.root)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.addCleanup(self.shutdown)

    def shutdown(self):
        self.server.shutdown(); self.server.server_close(); self.thread.join()

    def request(self, method, path, payload=None, headers=None):
        connection = http.client.HTTPConnection('127.0.0.1', self.server.server_port)
        self.addCleanup(connection.close)
        base = {'Content-Type': 'application/json'}
        base.update(headers or {})
        connection.request(method, path, json.dumps(payload) if payload is not None else None, base)
        response = connection.getresponse()
        return response.status, response.read()

    def test_readonly_routes_and_assets(self):
        for path in ('/', '/assets/review.js', '/assets/review.css', '/api/queue', '/api/state', '/api/jobs',
                     '/api/context?id=M11%3Aone', '/file/images/crop.png'):
            self.assertEqual(self.request('GET', path)[0], 200, path)

    def test_bad_host_origin_and_form_posts_rejected(self):
        payload = {'id': self.record['id'], 'decision': 'accept'}
        for headers in ({'Host': 'evil.example'}, {'Origin': 'https://evil.example'},
                        {'Content-Type': 'text/plain'}, {'Sec-Fetch-Site': 'cross-site'}):
            self.assertEqual(self.request('POST', '/api/decision', payload, headers)[0], 403)
        self.assertFalse(self.server.app.state_path.exists())

    def test_decision_and_undo_endpoints(self):
        self.assertEqual(self.request('POST', '/api/decision', {'id': self.record['id'], 'decision': 'accept'})[0], 200)
        status, result = self.request('POST', '/api/undo', {})
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(result)['state'], {})
        self.assertEqual(self.request('POST', '/api/decision', {'id': self.blocked['id'], 'decision': 'accept'})[0], 400)

    def test_only_queued_images_served_and_invalid_payload_rejected(self):
        Image.new('RGB', (20, 20)).save(self.root / 'images/private.png')
        self.assertEqual(self.request('GET', '/file/images/private.png')[0], 400)
        self.assertEqual(self.request('GET', '/file/../outside.png')[0], 400)
        self.assertEqual(self.request('POST', '/api/decision', [1, 2])[0], 400)

    def test_prepare_and_queue_endpoints(self):
        status, data = self.request('POST', '/api/cleanup/prepare', {'id': self.blocked['id']})
        self.assertEqual(status, 200)
        job = json.loads(data)
        Image.new('RGB', (30, 30), 'gray').save(self.root / job['working'])
        status, data = self.request('POST', '/api/cleanup/queue', {'id': self.blocked['id']})
        self.assertEqual(status, 200)
        candidate = json.loads(data)
        self.assertEqual(candidate['status'], 'pending_independent_review')
        self.assertEqual(self.request('GET', '/file/' + candidate['candidate'])[0], 200)
        self.assertFalse(self.server.app.state_path.exists())


if __name__ == '__main__':
    unittest.main()
