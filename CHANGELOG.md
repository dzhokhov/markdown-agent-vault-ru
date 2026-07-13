# Changelog

All notable public changes are tracked here.

This project uses early semantic versions. Until `v1.0.0`, breaking changes to structure or rules may happen when they make the starter pack clearer or safer.

## Unreleased

No unreleased changes yet.

## [v0.2.0] - 2026-07-13

### Added

- Added `project-creator`, a skill for creating complete active projects with agent-written `plan.md`, `tasks.md`, `context.md`, `log.md`, and `README.md`.
- Added autonomous planning guidance for agents, including Intent Lock, Owner Interaction Policy, Quality Criteria, and stricter question budgeting.
- Added `vault-memory`, a rule that separates current project memory from archive sources such as old logs, meetings, drafts, and inbox files.
- Added `meta/memory/` with memory ledger, anti-memory rules, and conflict index.
- Added memory trust templates: memory card, memory conflict, working context, and memory audit.
- Added `/memory-audit` prompt guidance for reviewing memory quality.
- Added `context-compression`, a skill for maintaining compact meeting history in `meetings/README.md`.
- Added `meetings_readme.md` template for compressed meeting history, decision chains, stale decisions, open questions, and anchor meetings.
- Added installation guidance and a compatibility table for common file-capable agents.
- Added Claude Cowork notes and the bundled `skills/sync-cowork-skills.sh` synchronization script.
- Added Google Antigravity to the agent list with its agent-management mode.
- Added intent reconstruction guidance for underspecified agent requests.
- Added contour GitHub repository mode: guide, rule, templates, example repository, manifest validation, and one-command contour validation.
- Added `repository-manifest.yml` as a machine-readable boundary file for contour repositories.
- Added `examples/github-contour-repository/` as a safe minimal contour repository example.
- Added `scripts/check_repository_manifest.py` and `scripts/validate_contour_repo.py`.

### Changed

- Updated `AGENTS.md` so agents route new project creation through `project-creator`, read current memory before archive sources, and record important memory changes.
- Updated write protocol, task routing, project templates, and meeting processing around current memory, trust fields, and agent-authored project plans.
- Updated onboarding and quickstart docs to explain the local-vault mode and the contour-repository mode.
- Updated `AGENTS.md`, write protocol, contour isolation, and pull request template for contour repository workflows.

## [v0.1.3] - 2026-05-02

### Removed

- Removed the text-editing skill that referenced a named third-party editing methodology.
- Removed the bundled stop-word reference list for that skill.
- Removed links and routing references to the deleted skill from adjacent skills and indexes.

## [v0.1.2] - 2026-05-02

### Changed

- Restored this repository as the Russian-first version after creating the separate English repository `dzhokhov/markdown-agent-vault`.
- Restored the root README and quickstart to Russian.

### Removed

- Removed transitional English entry files from this repository: `AGENTS.en.md`, `START_HERE.en.md`, `ONBOARDING.en.md`.

## [v0.1.1] - 2026-05-02

### Added

- English versions of the core first-run documents: `AGENTS.en.md`, `START_HERE.en.md`, and `ONBOARDING.en.md`.
- Language navigation in `README.md`.

### Changed

- `QUICKSTART.md` now points English-speaking users to the English first-run files while preserving the Russian originals.

## [v0.1.0] - 2026-05-02

First public starter-pack release.

### Added

- Public README with positioning, first 10-minute flow, comparison table, maturity status, topics, and validation commands.
- `QUICKSTART.md` for a safe 5-10 minute test.
- MIT license.
- Contribution, support, roadmap, and pull request guidance.
- GitHub issue templates for bugs, documentation fixes, examples, and method changes.
- Minimal `examples/first-session/` workflow showing an inbox note routed into a project.
- Release notes under `docs/releases/v0.1.0.md`.

### Notes

- This release is intentionally small.
- Tool-specific compatibility claims are not included yet.
- The repository should be tested as a copy before being used on a real vault.
