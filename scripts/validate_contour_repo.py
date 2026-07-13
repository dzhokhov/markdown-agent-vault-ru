#!/usr/bin/env python3
"""Run the minimal validation suite for a contour repository."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "repository-manifest.yml",
    "context.md",
    "plan.md",
    "tasks.md",
    "log.md",
    "CODEOWNERS",
]


def run(command: list[str]) -> int:
    print("+ " + " ".join(command))
    completed = subprocess.run(command, check=False)
    return completed.returncode


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".", help="Contour repository root")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    scripts_dir = Path(__file__).resolve().parent
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        if not (root / relative).exists():
            errors.append(f"missing required file: {relative}")

    if errors:
        print(f"CONTOUR_REQUIRED_FILE_ERRORS {len(errors)}")
        for error in errors:
            print(f"- {error}")
        return 1

    commands = [
        [sys.executable, str(scripts_dir / "check_repository_manifest.py"), str(root)],
        [sys.executable, str(scripts_dir / "check_links.py"), str(root)],
        [sys.executable, str(scripts_dir / "check_forbidden_markers.py"), str(root)],
    ]

    failed = 0
    for command in commands:
        if run(command) != 0:
            failed += 1

    if failed:
        print(f"CONTOUR_VALIDATION_FAILED {failed}")
        return 1

    print("OK contour repository")
    return 0


if __name__ == "__main__":
    sys.exit(main())
