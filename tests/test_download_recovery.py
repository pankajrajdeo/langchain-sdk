import contextlib
import io
import json
from pathlib import Path
import ssl
import tempfile
import unittest
from unittest.mock import MagicMock, patch
from urllib.error import HTTPError, URLError

import update_docs as updater


PAGE = "https://docs.langchain.com/langsmith/example"
CHILD = "https://docs.langchain.com/langsmith/child"


class DownloadRecoveryTests(unittest.TestCase):
    def run_mirror(self, download, discovery_errors=None):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            stale = root / "langsmith/stale.md"
            stale.parent.mkdir()
            stale.write_text("previous content")
            manifest = root / ".mirror-manifest.json"
            manifest.write_text(json.dumps({"files": {"langsmith/stale.md": {}}}))
            with (
                patch.object(updater, "OUTPUT_ROOT", root),
                patch.object(updater, "MANIFEST_PATH", manifest),
                patch.object(updater, "discover_seed_urls", return_value=({PAGE}, {}, discovery_errors or [])),
                patch.object(updater, "download_one", side_effect=download) as mocked,
                patch.object(updater.time, "sleep") as sleep,
                contextlib.redirect_stdout(io.StringIO()),
                contextlib.redirect_stderr(io.StringIO()),
            ):
                status = updater.mirror(workers=1, timeout=1, clean=True)
            return status, json.loads(manifest.read_text()), stale.exists(), mocked, sleep

    def test_recovery_crawls_new_links_and_allows_cleanup(self):
        attempts = {}

        def download(page, timeout, full_pages):
            attempts[page] = attempts.get(page, 0) + 1
            if page == PAGE and attempts[page] == 1:
                return updater.Download(page, error="TLS EOF")
            body = f"# Example\n\n[Child]({CHILD})\n" if page == PAGE else "# Child\n\nContent.\n"
            return updater.Download(page, final_url=page + ".md", raw_body=body.encode())

        status, manifest, stale_exists, _, sleep = self.run_mirror(download)
        self.assertEqual(status, 0)
        self.assertEqual(manifest["failures"], {})
        self.assertEqual(manifest["page_count"], 2)
        self.assertEqual(attempts, {PAGE: 2, CHILD: 1})
        self.assertFalse(stale_exists)
        sleep.assert_called_once_with(10)

    def test_persistent_failure_is_bounded_and_preserves_stale_files(self):
        status, manifest, stale_exists, download, sleep = self.run_mirror(
            lambda page, *_: updater.Download(page, error="TLS EOF")
        )
        self.assertEqual(status, 1)
        self.assertEqual(manifest["failures"], {PAGE: "TLS EOF"})
        self.assertTrue(stale_exists)
        self.assertEqual(download.call_count, 3)
        self.assertEqual([call.args[0] for call in sleep.call_args_list], [10, 20])

    def test_request_retries_tls_eof_and_broken_pipe(self):
        response = MagicMock()
        response.__enter__.return_value = response
        response.read.return_value = b"# Example"
        response.geturl.return_value = PAGE
        response.headers.get_content_type.return_value = "text/markdown"
        with (
            patch.object(updater.OPENER, "open", side_effect=[
                URLError(ssl.SSLEOFError("unexpected EOF")),
                URLError(BrokenPipeError("broken pipe")),
                response,
            ]) as request,
            patch.object(updater.time, "sleep"),
        ):
            self.assertEqual(updater.request_bytes(PAGE, 1)[0], b"# Example")
        self.assertEqual(request.call_count, 3)

    def test_normalization_failure_preserves_stale_files(self):
        status, manifest, stale_exists, _, _ = self.run_mirror(
            lambda page, *_: updater.Download(
                page, raw_body=b"# Example\n\nexport const UnknownComponent = () => null;\n"
            )
        )
        self.assertEqual(status, 1)
        self.assertIn(PAGE, manifest["normalization_warnings"])
        self.assertTrue(stale_exists)

    def test_incomplete_discovery_preserves_stale_files(self):
        _, manifest, stale_exists, _, _ = self.run_mirror(
            lambda page, *_: updater.Download(page, raw_body=b"# Example\n\nContent.\n"),
            discovery_errors=["sitemap unavailable"],
        )
        self.assertEqual(manifest["discovery_warnings"], ["sitemap unavailable"])
        self.assertTrue(stale_exists)

    def test_retry_after_seconds_and_dates_are_bounded(self):
        with patch.object(updater.random, "uniform", return_value=0.25), patch.object(
            updater.time, "time", return_value=0
        ):
            for header, expected in [
                ("30", 30),
                ("Thu, 01 Jan 1970 00:01:00 GMT", 60),
                ("999999", 120),
                ("invalid", 1.25),
                ("-10", 1.25),
            ]:
                with self.subTest(header=header):
                    error = HTTPError(PAGE, 429, "Too many requests", {"Retry-After": header}, None)
                    self.assertEqual(updater.retry_delay(error, 0), expected)
                    error.close()

    def test_http_rate_limit_uses_server_cooldown(self):
        error = HTTPError(PAGE, 429, "Too many requests", {"Retry-After": "30"}, None)
        with (
            patch.object(updater.OPENER, "open", side_effect=error) as request,
            patch.object(updater.time, "sleep") as sleep,
        ):
            with self.assertRaises(RuntimeError):
                updater.request_bytes(PAGE, 1)
        self.assertEqual(request.call_count, 3)
        self.assertEqual([call.args[0] for call in sleep.call_args_list], [30, 30])

    def test_missing_pages_are_not_retried(self):
        with (
            patch.object(updater.OPENER, "open", side_effect=HTTPError(PAGE, 404, "Missing", {}, None)) as request,
            patch.object(updater.time, "sleep") as sleep,
        ):
            with self.assertRaises(updater.MissingPage):
                updater.request_bytes(PAGE, 1)
        self.assertEqual(request.call_count, 1)
        sleep.assert_not_called()
