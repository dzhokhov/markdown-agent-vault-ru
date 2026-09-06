#!/usr/bin/env python3
"""Scan for common secret signatures and optional private literal markers.

This heuristic check does not replace a review before publication. Custom markers
belong in a separate, private UTF-8 file, with one literal substring per line.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path


# Keep these signatures generic: never embed an owner's private stop-list.
GENERIC_PATTERNS = {
    "private_key": re.compile(r"-----BEGIN (?:[A-Z0-9]+ )*PRIVATE KEY-----"),
    "github_token": re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{20,})\b"),
    "api_token": re.compile(r"\bsk-(?:proj-|ant-api\d+-)?[A-Za-z0-9_-]{20,}\b"),
    "slack_token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    "aws_access_key": re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
}
HOME_PATH_RE = re.compile(
    r"(?<![\w/])(?:/(?:Users|home)/|[A-Za-z]:[\\/]Users[\\/])"
    r"(?P<user><[^>\r\n]+>|[^\s/\\\"'`:,;<>]+)",
    re.IGNORECASE,
)
SKIP_PARTS = {".git", "__pycache__", ".cache", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
SKIP_SUFFIXES = {".pyc", ".pyo"}


def iter_text_files(root: Path, markers_path: Path | None = None):
    def traversal_error(error):
        raise error

    for directory, dirs, files in os.walk(root, onerror=traversal_error):
        dirs[:] = [name for name in dirs if name not in SKIP_PARTS]
        for name in sorted(files):
            path = Path(directory) / name
            if name in SKIP_PARTS or name == ".DS_Store" or path.suffix in SKIP_SUFFIXES:
                continue
            # Do not follow links out of the selected package.
            if path.is_symlink() or path.resolve() == markers_path:
                continue
            yield path


def categories(line: str, markers: list[str]):
    for category, pattern in GENERIC_PATTERNS.items():
        if pattern.search(line):
            yield category
    if any(match.group("user").lower() != "<user>" for match in HOME_PATH_RE.finditer(line)):
        yield "private_home_path"
    if any(marker in line.casefold() for marker in markers):
        yield "custom_marker"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="Vault root, default: current directory")
    parser.add_argument("--markers", type=Path, help="Private UTF-8 file: one case-insensitive literal substring per line")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print("ERROR root_not_directory", file=sys.stderr)
        return 2
    markers_path = args.markers.resolve() if args.markers is not None else None
    markers: list[str] = []
    if markers_path is not None:
        try:
            markers = [line.casefold() for line in markers_path.read_text(encoding="utf-8").splitlines() if line]
        except (OSError, UnicodeError):
            print("ERROR markers_unreadable", file=sys.stderr)
            return 2

    hits: list[tuple[Path, int, str]] = []
    try:
        for path in iter_text_files(root, markers_path):
            content = path.read_text(encoding="utf-8", errors="ignore")
            for lineno, line in enumerate(content.splitlines(), 1):
                for category in categories(line, markers):
                    hits.append((path.relative_to(root), lineno, category))
    except OSError:
        print("ERROR scan_unreadable", file=sys.stderr)
        return 2

    if hits:
        print(f"FORBIDDEN_MARKERS {len(hits)}")
        for path, lineno, category in hits:
            print(f"{path}:{lineno}:{category}")
        return 1

    print("OK forbidden markers")
    return 0


if __name__ == "__main__":
    sys.exit(main())
