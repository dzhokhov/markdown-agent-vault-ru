---
id: meta-memory-index
type: index
status: active
created: 2026-07-01
updated: 2026-07-01
aliases:
  - "Индекс meta/memory"
  - "Индекс слоя доверия памяти"
tags: [memory, trust, index, meta]
source_path: "meta/memory/README.md"
knowledge_criticality: high
verification_status: unverified
verified_by_me: false
curation_mode: llm_explicit_request
---

# README: `meta/memory`

## Суть

Служебный слой доверия к долговременной памяти vault: журнал изменений, антипамять и конфликты уровня правил.

## Файлы

- [Очередь проверки памяти](./review-queue.md) — нерешённые вопросы и конфликты источников.

- [Журнал изменений памяти](./ledger.md) — изменения доверия, статусов, текущих картин, конфликтов и важных утверждений.
- [Правила антипамяти](./anti-memory.md) — что нельзя запоминать как факт и выводить автоматически.
- [Конфликты памяти](./conflicts/README.md) — индекс конфликтов уровня vault.

## Связанные правила

- [Память vault](../rules/vault-memory.md) — главный стандарт актуальной памяти и доверия к утверждениям.
- [Протокол записи](../rules/write-protocol.md) — когда и как фиксировать изменения.
- [Протокол ревью vault](../rules/vault-review.md) — проверка качества памяти.

## Следующий шаг

Добавлять сюда только сквозные правила и журналы уровня vault. Проектные факты, решения и конфликты должны жить рядом с владельцем данных.
