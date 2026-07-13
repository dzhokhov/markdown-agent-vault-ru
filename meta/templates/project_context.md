---
id: <yyyy-mm-dd>-<project-slug>-context
type: project
status: active
created: <YYYY-MM-DD>
updated: 2026-07-01
aliases:
  - "Шаблон контекста проекта"
tags: [project, context]
source_path: "<path-before-migration-or-current>"
knowledge_criticality: low
verification_status: unverified
verified_by_me: false
curation_mode: none
---

# Context

## Суть
Устойчивые инварианты проекта в одном месте: термины, метрики, SoT, ограничения. **НЕ хранит эпизодику со встреч** — она живёт в файлах самих встреч под `## Упомянуто вскользь` с canonical-тегом. Триггер переноса из эпизодики в `context.md` — момент, когда владелец/агент формулирует опинион («мы знаем про X, что Y»), а не счётчик упоминаний.

Если сюда начинает попадать текущий расклад («что сейчас главное», «что изменилось», «что устарело»), вынести его в отдельную текущую картину и сослаться на неё из этого файла и `README.md`. См. [Память vault](../rules/vault-memory.md).

Для инвариантов, которые влияют на решения, сроки, архитектуру, продуктовые обязательства или текущую картину, добавлять лёгкий блок доверия:

```yaml
claim_type: observed | stated_by_user | stated_by_other | inferred | decision | assumption | hypothesis | preference | constraint | plan | risk | status | historical
source:
  - ""
evidence:
  kind: direct_user_statement | direct_quote | meeting_note | document_fact | agent_inference | repeated_pattern | external_source | unknown
  strength: high | medium | low
confidence: high | medium | low
last_verified: YYYY-MM-DD
write_policy: auto | suggest | human_review_required | locked
```

Если основание слабое или старое, не формулировать инвариант как безусловный факт. Использовать пометки «требует проверки» или «неподтверждённое предположение».

См. [task-routing-methodology-2026-04.md §8](../../03_knowledge/task-routing-methodology-2026-04.md). Цель / Non-goals / Milestones — НЕ сюда, они в [plan.md](./plan.md).

## Детали
- Термины:
- Ограничения:
- Метрики успеха:
- Source of truth (данные, артефакты, трекеры):
- Текущая картина (если есть):
- Зависимости:
- Stakeholders (роли, не хронология):

## Trust notes

- Слабые или давно не проверявшиеся инварианты:
- Нерешённые конфликты, влияющие на контекст:
- Утверждения, основанные на выводе агента, а не на прямом источнике:

## Следующий шаг
