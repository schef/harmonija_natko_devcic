"""Optional real-browser test using a temporary repository and a fake GIMP."""

import shutil
import subprocess
import threading
from pathlib import Path
from http.server import HTTPServer
import unittest

from PIL import Image

from test_book_review import Fixture
from review_book import ReviewApp, ReviewHandler


@unittest.skipUnless(shutil.which('chromium') and shutil.which('node'), 'Requires Chromium and Node')
class BrowserTests(Fixture):
    def test_review_workspace(self):
        class FakeProcess:
            pid = 123456789
            def wait(self): return 0

        def launch(path):
            Image.new('RGB', (30, 30), 'gray').save(path)
            return FakeProcess()

        class QuietHandler(ReviewHandler):
            def log_message(self, *args): pass

        server = HTTPServer(('127.0.0.1', 0), QuietHandler)
        server.app = ReviewApp(self.root, launcher=launch)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            output = Path('/tmp/opencode/harmonija-review-workspace-test.png')
            output.parent.mkdir(parents=True, exist_ok=True)
            result = subprocess.run(['node', str(Path(__file__).with_name('book_review_browser.mjs')),
                                     f'http://127.0.0.1:{server.server_port}', str(output)],
                                    capture_output=True, text=True, timeout=90)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertTrue(output.is_file())
            self.assertFalse(server.app.workflow.active)
        finally:
            server.shutdown(); server.server_close(); thread.join()


if __name__ == '__main__':
    unittest.main()
