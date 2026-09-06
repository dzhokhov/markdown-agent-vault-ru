#!/usr/bin/env python3
"""Regression checks using synthetic inputs; no credentials are required."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPTS = Path(__file__).resolve().parent


class CheckerTests(unittest.TestCase):
    def setUp(self):
        # LIFECYCLE: temporary fixtures, deleted after each test by TemporaryDirectory.
        self.temp = tempfile.TemporaryDirectory(prefix="checker-fixtures-", dir=SCRIPTS.parent)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def run_checker(self, script, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPTS / script), str(self.root), *map(str, args)],
            capture_output=True, text=True, check=False,
        )

    def privacy(self, *args):
        return self.run_checker("check_forbidden_markers.py", *args)

    def test_generic_signatures_and_hidden_file_without_secret_output(self):
        secrets = [
            ("private_key", "-----BEGIN " + "RSA PRIVATE KEY-----"),
            ("github_token", "ghp_" + "aB1" * 12),
            ("github_token", "github_pat_" + "z9_" * 12),
            ("api_token", "sk-" + "proj-" + "aB12" * 10),
            ("slack_token", "xoxb-" + "12345-" * 5),
            ("aws_access_key", "AKIA" + "A1" * 8),
            ("private_home_path", "/Users/" + "fixture-owner/private.txt"),
            ("private_home_path", "/home/" + "fixture-owner/private.txt"),
            ("private_home_path", "C:" + "\\Users\\fixture-owner\\private.txt"),
        ]
        self.write("nested/.env", "\n".join(value for _, value in secrets))
        result = self.privacy()
        self.assertEqual(result.returncode, 1, result.stderr)
        for line, (category, value) in enumerate(secrets, 1):
            self.assertIn(f"nested/.env:{line}:{category}", result.stdout)
            self.assertNotIn(value, result.stdout + result.stderr)
        self.assertNotIn(str(self.root), result.stdout + result.stderr)

    def test_placeholders_and_public_metadata_are_allowed(self):
        self.write("README.md", "\n".join([
            "/Users/<user>/vault", "/home/<user>/vault", "/path/to/vault", "/abs/path/vault",
            "api_key = <your-key>", "api_key", "Keychain", "Telegram", "salary",
            "https://github.com/example-author/example-vault", "ghp_example", "sk-example",
        ]))
        self.assertEqual(self.privacy().returncode, 0)

    def test_custom_markers_are_literal_and_not_reported(self):
        markers = self.write("private.markers", "private.customer+example\n")
        self.write("data.txt", "PRIVATE.CUSTOMER+EXAMPLE\nprivateXcustomerexample\n")
        result = self.privacy("--markers", markers)
        self.assertEqual(result.returncode, 1)
        self.assertIn("data.txt:1:custom_marker", result.stdout)
        self.assertNotIn("data.txt:2:", result.stdout)
        self.assertNotIn("private.markers:", result.stdout)
        self.assertNotIn("PRIVATE.CUSTOMER+EXAMPLE", result.stdout)
        self.assertNotIn("private.customer+example", result.stdout)

    def test_marker_file_is_excluded_even_for_generic_signatures(self):
        marker = self.write("private.markers", "ghp_" + "aB1" * 12)
        self.assertEqual(self.privacy("--markers", marker).returncode, 0)

    def test_explicit_invalid_marker_file_fails(self):
        invalid_encoding = self.root / "invalid.txt"
        invalid_encoding.write_bytes(b"\xff\xfe")
        for path in [self.root / "missing.txt", self.root, invalid_encoding]:
            with self.subTest(path=path.name):
                result = self.privacy("--markers", path)
                self.assertEqual(result.returncode, 2)
                self.assertIn("markers_unreadable", result.stderr)
                self.assertNotIn(str(path), result.stderr)

    def test_only_git_and_caches_are_excluded(self):
        token = "ghp_" + "aB1" * 12
        for directory in [".git", ".cache", "__pycache__", "nested/.pytest_cache"]:
            self.write(directory + "/secret.txt", token)
        self.assertEqual(self.privacy().returncode, 0)
        self.write("scripts/check_forbidden_markers.py", token)
        result = self.privacy()
        self.assertEqual(result.returncode, 1)
        self.assertIn("scripts/check_forbidden_markers.py:1:github_token", result.stdout)

    def test_checker_and_tests_can_scan_their_own_source(self):
        for name in ["check_forbidden_markers.py", "test_checkers.py"]:
            self.write("scripts/" + name, (SCRIPTS / name).read_text(encoding="utf-8"))
        self.assertEqual(self.privacy().returncode, 0)

    def links(self):
        return self.run_checker("check_links.py")

    def test_real_broken_link_is_reported_in_references(self):
        self.write("skills/example/references/guide.md", "[Missing](missing.md)\n")
        result = self.links()
        self.assertEqual(result.returncode, 1)
        self.assertIn("guide.md -> missing.md", result.stdout)

    def test_fenced_examples_are_skipped_and_real_links_still_checked(self):
        self.write("existing.md", "Present\n")
        self.write("guide.md", "\n".join([
            "[Present](existing.md)",
            "```markdown", "[Template](missing-in-backticks.md)", "```",
            "~~~markdown", "[Template](missing-in-tildes.md)", "~~~",
            "[Present](existing.md)",
        ]))
        self.assertEqual(self.links().returncode, 0)
        with (self.root / "guide.md").open("a", encoding="utf-8") as stream:
            stream.write("\n[Missing](after-fence.md)\n")
        result = self.links()
        self.assertEqual(result.returncode, 1)
        self.assertIn("after-fence.md", result.stdout)
        self.assertNotIn("missing-in-", result.stdout)

    def test_shorter_or_different_fences_do_not_close_outer_fence(self):
        for marker in ["`", "~"]:
            with self.subTest(marker=marker):
                self.write("guide.md", "\n".join([
                    marker * 4 + "markdown", marker * 3,
                    "[Template](still-inside.md)",
                    ("~" if marker == "`" else "`") * 4,
                    "[Template](also-inside.md)",
                    marker * 5 + " trailing text", "[Template](not-closed.md)",
                    "   " + marker * 5 + "  ", "[Missing](outside.md)",
                ]))
                result = self.links()
                self.assertEqual(result.returncode, 1)
                self.assertIn("outside.md", result.stdout)
                self.assertNotIn("inside.md", result.stdout)
                self.assertNotIn("not-closed.md", result.stdout)

    def test_unclosed_fence_hides_rest_of_example(self):
        self.write("guide.md", "```md\n[Template](missing.md)\n")
        self.assertEqual(self.links().returncode, 0)

    def test_backtick_in_info_string_is_not_an_opening_fence(self):
        self.write("guide.md", "```invalid`info\n[Missing](visible.md)\n")
        result = self.links()
        self.assertEqual(result.returncode, 1)
        self.assertIn("visible.md", result.stdout)


if __name__ == "__main__":
    unittest.main()
