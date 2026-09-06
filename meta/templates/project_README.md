---
id: <yyyy-mm-dd>-<project-slug>-readme
type: project
status: active
created: <YYYY-MM-DD>
updated: 2026-06-15
aliases:
  - "Шаблон индекса проекта"
tags: [project, work]
source_path: "<path-before-migration-or-current>"
knowledge_criticality: low
verification_status: unverified
verified_by_me: false
curation_mode: none
---

# <Проект>

## Суть
Короткая формулировка проекта — одно предложение. Подробности (Goal, Non-goals, Appetite, Milestones) — в [plan.md](./plan.md), не здесь.

## Детали
- Контур: <имя контура из карты `meta/config/contours-map.md`, например acme-shop>
- Task Mode: `operational` | `development`
- Артефакты:
- Текущая картина: <нет | [название](./current-*.md)>  # если проекту нужен отдельный пересобираемый слой актуального состояния
- Service files:
  - [plan.md](./plan.md) — контракт проекта (Goal/Non-goals/Appetite/Milestones/Drift Guard/Contingency)
  - [tasks.md](./tasks.md) — execution-очередь текущего milestone
  - [context.md](./context.md) — устойчивые инварианты проекта
  - [log.md](./log.md) — хронология событий и решений

## Связанные файлы вне папки проекта
- Делегирования по этому проекту: см. `01_now/ops/<contour>/delegations/<person-slug>.md` (по каждому исполнителю)
- Личные обязательства владельца, упомянутые на встречах проекта: см. [01_now/personal/tasks.md](../../personal/tasks.md)

## Следующий шаг
