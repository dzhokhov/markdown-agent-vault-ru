#!/usr/bin/env python3
"""Check local Markdown links inside a vault-like folder."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+\.md(?:#[^)]+)?)\)")
IGNORED_TARGETS = {
    "./relative-path.md",
    "./abs-path-to-SKILL.md",
}
FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")


def prose_lines(text: str):
    """Yield lines outside Markdown fences, respecting marker and fence length."""
    fence = None
    for line in text.splitlines(keepends=True):
        match = FENCE_RE.match(line)
        if fence is not None:
            if (match and match.group(1)[0] == fence[0]
                    and len(match.group(1)) >= len(fence)
                    and not match.group(2).strip()):
                fence = None
            continue
        if match and (match.group(1)[0] == "~" or "`" not in match.group(2)):
            fence = match.group(1)
            continue
        yield line


def iter_markdown_files(root: Path):
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        yield path


def should_ignore(path: Path, target: str) -> bool:
    if "meta/templates" in path.as_posix():
        return True
    if target.startswith(("http://", "https://", "mailto:")):
        return True
    if "<" in target or "..." in target:
        return True
    if target in IGNORED_TARGETS:
        return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".", help="Vault root, default: current directory")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    broken: list[tuple[Path, str]] = []

    for path in iter_markdown_files(root):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in LINK_RE.finditer("".join(prose_lines(text))):
            target = match.group(1).split("#", 1)[0]
            if should_ignore(path, target):
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(root)
            except ValueError:
                continue
            if not resolved.exists():
                broken.append((path.relative_to(root), target))

    if broken:
        print(f"BROKEN_LINKS {len(broken)}")
        for path, target in broken:
            print(f"{path} -> {target}")
        return 1

    print("OK links")
    return 0


if __name__ == "__main__":
    sys.exit(main())
