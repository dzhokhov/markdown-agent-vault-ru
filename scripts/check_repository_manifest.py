#!/usr/bin/env python3
"""Validate the minimal repository-manifest.yml contract."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_TOP_LEVEL = [
    "schema_version",
    "repo",
    "human_model",
    "access",
    "write_model",
    "agent_policy",
    "meeting_policy",
    "validation",
    "action_log",
    "questions_for_user",
]

REQUIRED_READ_FIRST = [
    "AGENTS.md",
    "repository-manifest.yml",
    "README.md",
    "context.md",
]

REQUIRED_QUESTIONS = [
    "when_ambiguous_contour",
    "when_private_data_risk",
    "when_meeting_material",
    "when_deleting_or_moving",
]


def strip_quotes(value: str) -> str:
    value = value.strip().split("#", 1)[0].strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def scalar(lines: list[str], key: str) -> str | None:
    pattern = re.compile(rf"^\s*{re.escape(key)}:\s*(.+?)\s*$")
    for line in lines:
        match = pattern.match(line)
        if match:
            return strip_quotes(match.group(1))
    return None


def has_top_level(lines: list[str], key: str) -> bool:
    return any(re.match(rf"^{re.escape(key)}:\s*", line) for line in lines)


def list_values_after(lines: list[str], key: str) -> list[str]:
    key_pattern = re.compile(rf"^(\s*){re.escape(key)}:\s*$")
    for index, line in enumerate(lines):
        match = key_pattern.match(line)
        if not match:
            continue
        base_indent = len(match.group(1))
        values: list[str] = []
        for nested in lines[index + 1 :]:
            if not nested.strip():
                continue
            indent = len(nested) - len(nested.lstrip(" "))
            if indent <= base_indent:
                break
            item_match = re.match(r"^\s*-\s*(.+?)\s*$", nested)
            if item_match:
                values.append(strip_quotes(item_match.group(1)))
        return values
    return []


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".", help="Repository root, default: current directory")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    manifest = root / "repository-manifest.yml"
    errors: list[str] = []

    if not manifest.exists():
        print(f"MISSING repository-manifest.yml in {root}")
        return 1

    lines = manifest.read_text(encoding="utf-8").splitlines()

    for key in REQUIRED_TOP_LEVEL:
        if not has_top_level(lines, key):
            errors.append(f"missing top-level section: {key}")

    visibility = scalar(lines, "visibility")
    if visibility not in {"public", "private", "internal"}:
        errors.append("repo.visibility must be public, private, or internal")

    data_class = scalar(lines, "data_class")
    if data_class not in {"ordinary", "private", "mixed"}:
        errors.append("repo.data_class must be ordinary, private, or mixed")

    default_change_path = scalar(lines, "default_change_path")
    if default_change_path not in {"branch-and-change-request", "direct-main-only"}:
        errors.append("write_model.default_change_path must be branch-and-change-request or direct-main-only")

    for key in ["name", "contour", "owner", "main_branch", "durable_source_of_truth"]:
        if not scalar(lines, key):
            errors.append(f"repo.{key} is required")

    read_first = set(list_values_after(lines, "read_first"))
    for item in REQUIRED_READ_FIRST:
        if item not in read_first:
            errors.append(f"agent_policy.read_first must include {item}")

    for list_key in ["may_edit_without_asking", "ask_before", "never_commit"]:
        if not list_values_after(lines, list_key):
            errors.append(f"agent_policy.{list_key} must be a non-empty list")

    if scalar(lines, "required_in_this_repository") not in {"true", "false"}:
        errors.append("meeting_policy.required_in_this_repository must be true or false")

    for list_key in ["required_frontmatter", "allowed_meeting_scope_values", "allowed_audience_values"]:
        if not list_values_after(lines, list_key):
            errors.append(f"meeting_policy.{list_key} must be a non-empty list")

    if not list_values_after(lines, "required_before_change_request"):
        errors.append("validation.required_before_change_request must be a non-empty list")

    for question in REQUIRED_QUESTIONS:
        if not scalar(lines, question):
            errors.append(f"questions_for_user.{question} is required")

    if errors:
        print(f"MANIFEST_ERRORS {len(errors)}")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK repository manifest")
    return 0


if __name__ == "__main__":
    sys.exit(main())
