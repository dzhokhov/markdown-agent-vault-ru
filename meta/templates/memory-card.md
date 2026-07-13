---
id: fact-YYYY-MM-DD-001
project: ""
type: fact | decision | constraint | risk | plan | preference | open_question | status | historical
claim_type: observed | stated_by_user | stated_by_other | inferred | decision | assumption | hypothesis | preference | constraint | plan | risk | status | historical
status: active | stale | archived | contradicted | superseded
confidence: high | medium | low
created: YYYY-MM-DD
updated: YYYY-MM-DD
last_verified: YYYY-MM-DD
valid_from:
valid_until:
decay_policy: none | reduce_after_30_days | reduce_after_60_days | reduce_after_90_days | custom
needs_review: false

write_policy: auto | suggest | human_review_required | locked

source:
  - ""

evidence:
  kind: direct_user_statement | direct_quote | meeting_note | document_fact | agent_inference | repeated_pattern | external_source | unknown
  quote: ""
  strength: high | medium | low

interpretation:
  text: ""
  confidence: high | medium | low

authority:
  speaker: ""
  role: owner | product | developer | client | manager | external | unknown
  can_define_project_direction: true | false | unknown

supersedes:
superseded_by:
related_conflicts:
tags:
---

# Краткое название

## Утверждение

Что именно считается содержанием памяти.

## Основание

Почему это утверждение записано. Для важных утверждений добавить короткую цитату или точный фрагмент основания.

## Интерпретация

Как агент понял источник. Если это вывод агента, `claim_type` должен быть `inferred`, `assumption` или `hypothesis`, а не `observed` или `decision`.

## Ограничения применимости

Когда это утверждение может быть неприменимо.

## Проверка

Что нужно проверить, если факт важен для решения.
