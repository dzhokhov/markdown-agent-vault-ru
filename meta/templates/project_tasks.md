---
id: <yyyy-mm-dd>-<project-slug>-tasks
type: tasks
status: active
created: <YYYY-MM-DD>
updated: 2026-07-15
aliases:
  - "Шаблон задач проекта"
tags: [project, tasks]
source_path: "<path-before-migration-or-current>"
knowledge_criticality: low
verification_status: unverified
verified_by_me: false
curation_mode: none
---

# Tasks

## Суть

**Execution-очередь** проекта. Производный файл от `plan.md`: только текущий milestone, один активный шаг, локальные критерии выхода, короткая защита от дрифта и следующий шаг. `tasks.md` не хранит историю (для этого есть `log.md`), не хранит план (для этого есть `plan.md`), не хранит делегирования (для этого есть `ops/<contour>/delegations/<slug>.md`), не хранит личные обязательства владельца (для этого есть `01_now/personal/tasks.md`).

Полная методология: [task-routing-methodology-2026-04.md](../../03_knowledge/task-routing-methodology-2026-04.md). Правила владения: [AGENTS.md Правила 10–12](../../AGENTS.md).

## Запреты

- **Нельзя:** `Goal`, `Milestones`, `Contingency`, `Appetite`, `Quality Criteria` — всё это в `plan.md`.
- **Нельзя:** секция `Blocked` — блокеры живут в `plan.md §Blockers` как first-class сущности с карточками `Bx` (см. §5.4 методологии).
- **Нельзя:** строки вида «понять, что делать с X», «разобраться с Y» — это размышление, его место в `plan.md` под соответствующий milestone как открытый вопрос.
- **Нельзя:** строки вида «уточнить у владельца план», «попросить критерии», «согласовать пункты». Если вопрос меняет цель, границы, источник правды или цену ошибки — это `plan.md`; если не меняет — агент делает безопасное допущение.
- **Нельзя:** делегирование сотруднику («Дима сделает X») — это в `ops/<contour>/delegations/<person-slug>.md`.
- **Нельзя:** личное обязательство владельца — это в `01_now/personal/tasks.md`.

## Task Mode

Выбери один режим (он повторяет `task_mode` из `plan.md`) и удали второй шаблон ниже:
- `operational` — результатом являются анализ, решение, документ, досье, таблица или контент; вспомогательные скрипты допустимы
- `development` — программный инструмент, интеграция или внешний выпуск сами являются результатом

Держи только один `Active` / `Active Step` в каждый момент времени.

`Current Milestone` обязателен в обоих режимах и должен ссылаться на `M<N>` из `plan.md`. Если текущий шаг не выводится из этого milestone, сначала обнови `plan.md`.

---

## Шаблон `operational`

### Current Milestone
Ссылка на milestone из `plan.md`: `M<N> — <название>`. Не дублируй сюда цель и acceptance — они в `plan.md`.

### Active
- [ ] <один текущий шаг>

### Пользовательский результат шага
<что новое после шага сможет прочитать, использовать, решить или запустить владелец; если прямого ответа нет, это служебный шаг и он должен укладываться в Preparation Budget>

### Exit Criteria
- <локальное наблюдаемое условие завершения текущего шага>

### Drift Guard (short)
- <краткая выдержка из Drift Guard / Non-goals / Quality Criteria в plan.md>

### Next
- [ ] <1-3 ближайших шага в рамках текущего milestone из plan.md>

### Backlog
- [ ] <не сейчас, но только в рамках текущего milestone>

### Done
- [x] <последние 3-5 завершённых шагов, не больше — старое уходит в log.md>

---

## Шаблон `development`

### Current Milestone
Ссылка на милстоун из `plan.md`: `M<N> — <название>`. Не дублируй сюда цель и acceptance — они там.

### Active Step
- [ ] <один текущий шаг>

### Пользовательский результат шага
<что новое после шага сможет прочитать, использовать, решить или запустить владелец>

### Зачем
<почему этот шаг сейчас в контексте milestone>

### Exit Criteria
- <наблюдаемое условие завершения 1>
- <наблюдаемое условие завершения 2>

### Drift Guard (short)
- <краткая выдержка из Drift Guard / Non-goals / Quality Criteria в plan.md>

### Next
- [ ] <1-3 следующих шага в рамках текущего milestone>

### Backlog
- [ ] <позже, но только в рамках текущего milestone>

### Done
- [x] <последние 3-5 шагов>

## Drift protocol

Если собираешься работать вне `Active`/`Next`, или понимаешь, что текущий milestone больше не ведёт к цели:
1. Сначала правка `plan.md` (milestones, acceptance, quality criteria, owner interaction policy, drift guard, contingency).
2. Одна строка в `log.md`: «дрейф: было X, стало Y».
3. Только потом обновление `tasks.md` и возобновление работы.

## Следующий шаг
Выбрать `Task Mode`, удалить лишний шаблон, указать `Current Milestone` из `plan.md` и оставить один `Active` шаг.
