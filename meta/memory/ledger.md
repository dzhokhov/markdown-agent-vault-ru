---
id: memory-ledger
type: log
status: active
created: 2026-07-13
updated: 2026-07-13
aliases:
  - "Журнал изменений памяти"
  - "Memory ledger"
tags: [memory, trust, ledger, vault]
source_path: "meta/memory/ledger.md"
knowledge_criticality: high
verification_status: unverified
verified_by_me: false
curation_mode: llm_explicit_request
---

# Журнал изменений памяти

## Суть

Журнал фиксирует изменения долговременной памяти vault: текущих картин, карточек памяти, решений, важных утверждений, статусов доверия, конфликтов и правил памяти.

Запись обязательна, когда агент или скрипт меняет:

- важное утверждение памяти;
- `claim_type`, `confidence`, `last_verified`, `status`, `write_policy`;
- текущую картину проекта или контура;
- цель проекта, архитектурное решение, продуктовое решение или ключевое ограничение;
- статус утверждения: `stale`, `contradicted`, `superseded`, `archived`;
- конфликт памяти.

## Формат записи

```md
## YYYY-MM-DD HH:MM

Changed:
- `path/to/file.md`

Action:
- created | updated | marked_stale | superseded | archived | restored | deleted | proposed

Reason:
- why this change was made

Source:
- `path/to/source.md`

Changed by:
- agent | human | script

Review:
- auto_applied | pending_human_review | approved | rejected
```

## Записи

Пока нет записей.

## Следующий шаг

Добавлять сюда только изменения долговременной памяти. Обычные правки текста, навигации и форматирования без изменения доверия или статуса утверждений сюда не попадают.
