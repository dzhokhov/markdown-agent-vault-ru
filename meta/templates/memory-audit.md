---
id: memory-audit-YYYY-MM-DD
type: note
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
aliases:
  - "Memory Audit YYYY-MM-DD"
tags: [memory, audit, trust]
source_path: "<path>/memory-audit-YYYY-MM-DD.md"
knowledge_criticality: medium
verification_status: unverified
verified_by_me: false
curation_mode: llm_explicit_request
---

# Memory Audit - YYYY-MM-DD

## Summary

Краткая оценка состояния памяти.

## Problems found

- Есть ли активные факты без источников?
- Есть ли решения без основания?
- Есть ли утверждения с `evidence.strength: low`, попавшие в текущую картину как безусловные?
- Есть ли планы после `valid_until`?
- Есть ли факты с просроченным `last_verified`?
- Есть ли конфликты без статуса?
- Есть ли карточки без `claim_type`?
- Есть ли важные изменения без записи в `meta/memory/ledger.md`?
- Есть ли утверждения, где `claim_type: inferred`, но они используются как факт?
- Есть ли карточки с `write_policy: human_review_required`, которые агент изменил сам?
- Есть ли повторяющиеся или противоречащие друг другу карточки?

## High-risk issues

- ...

## Stale or weak facts

- ...

## Conflicts

- ...

## Recommended changes

- ...

## Changes requiring human review

- ...

## Rule

Проверка памяти не чинит стратегические решения, цели, правила памяти и спорные факты автоматически. Такие изменения идут через `human_review_required`.
