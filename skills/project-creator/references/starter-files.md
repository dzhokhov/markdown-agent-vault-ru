# Стартовые файлы проекта: шаблоны и примеры

Заполненные образцы `README.md`, `context.md`, `tasks.md`, `log.md` и снипеты правок индексов. Пример — `2026-acme-shop-positioning-strategy` (режим `operational`), тот же, что в [plan-authoring.md](./plan-authoring.md). Frontmatter — по [write-protocol §1](../../../meta/rules/write-protocol.md): `id`, `type`, `status`, `created`, `updated`, `aliases` (≥1 русский), `tags`, `source_path`. Даты — сегодняшние (`date +%F`).

## README.md — точка входа

Короткий навигатор: что за проект, где plan/tasks/context/log, где ключевые материалы. `type: project`.

```markdown
---
id: 2026-acme-shop-positioning-strategy-readme
type: project
status: active
created: 2026-07-10
updated: 2026-07-10
aliases:
  - "Позиционирование Acme Shop"
tags: [project, acme-shop, positioning, strategy]
source_path: "01_now/projects/2026-acme-shop-positioning-strategy/README.md"
freshness: seasonal
expires: 2027-01-10
knowledge_criticality: medium
verification_status: unverified
curation_mode: llm_explicit_request
---

# Позиционирование Acme Shop

## Суть
Проект по выбору ядра позиционирования Acme Shop: одна формулировка, проверяемая подстановкой конкурента, с аргументами против альтернатив.

## Детали
- Контур: acme-shop.
- Task Mode: `operational`.
- Service files:
  - [plan.md](./plan.md) — контракт проекта: цель, границы, рубежи, критерии.
  - [tasks.md](./tasks.md) — очередь исполнения текущего рубежа.
  - [context.md](./context.md) — устойчивые инварианты проекта.
  - [log.md](./log.md) — хронология решений.

## Следующий шаг
Начать M1: карта конкурентного поля.
```

## context.md — устойчивые инварианты

Только то, что переживёт сессии: термины, метрики, источники правды, ограничения, зависимости. **Без** эпизодики со встреч и без хроники (Правило 14).

```markdown
---
id: 2026-acme-shop-positioning-strategy-context
type: project
status: active
created: 2026-07-10
updated: 2026-07-10
aliases:
  - "Контекст — позиционирование Acme Shop"
tags: [project, context, acme-shop, positioning]
source_path: "01_now/projects/2026-acme-shop-positioning-strategy/context.md"
knowledge_criticality: medium
verification_status: unverified
curation_mode: llm_explicit_request
---

# Context

## Суть
Устойчивые решения проекта позиционирования Acme Shop.

## Детали
- Термины:
  - «Ядро позиционирования» — одна формулировка, которую не может повторить прямой конкурент.
  - «Лакмус-тест подстановкой» — проверка: если конкурент может сказать то же, формулировка не дифференцирует.
- Ограничения:
  - Работаем над ядром, не над лендингом и не над рекламой (см. Non-goals в plan.md).
  - Горизонт — российский рынок, прямые конкуренты.
- Метрики успеха:
  - Выбрано одно ядро с обоснованием против двух альтернатив.
  - Ядро проходит лакмус-тест подстановкой конкурента.
- Источник правды:
  - [plan.md](./plan.md).
  - Ранее собранный конкурентный обзор (ссылка добавляется при подключении).
- Зависимости:
  - Материалы обсуждения из чата-источника.

## Следующий шаг
Наполнять инвариантами по мере прохождения рубежей.
```

## tasks.md — очередь исполнения

Только исполнение. `tasks.md` производен от `plan.md`: объявлен `Task Mode`, указан `Current Milestone`, ровно один Active-шаг, `Пользовательский результат шага`, локальные Exit Criteria, короткий `Drift Guard (short)`, Next. **Запрещено:** `Goal`, `Milestones`, `Contingency`, `Quality Criteria`, секция `Blocked` (Правило 10).

### Вариант operational

```markdown
---
id: 2026-acme-shop-positioning-strategy-tasks
type: tasks
status: active
created: 2026-07-10
updated: 2026-07-10
aliases:
  - "Задачи — позиционирование Acme Shop"
tags: [project, tasks, acme-shop, positioning]
source_path: "01_now/projects/2026-acme-shop-positioning-strategy/tasks.md"
knowledge_criticality: medium
verification_status: unverified
curation_mode: llm_explicit_request
---

# Tasks

Task Mode: `operational`

## Current Milestone
[M1 — Карта конкурентного поля](./plan.md#m1--карта-конкурентного-поля)

## Active
- [ ] Собрать карту конкурентного поля: 5+ прямых конкурентов, их ядро и занятые слова.

## Пользовательский результат шага
Владелец видит карту занятых позиций и может отсечь неотличимые варианты до выбора ядра.

## Exit Criteria
- Таблица конкурентов заполнена, видно, какие слова заняты.

## Drift Guard (short)
- Не выбирать ядро позиционирования до завершения карты поля.
- Не переходить к лендингу или рекламе — это Non-goals проекта.

## Next
- [ ] Сформулировать 3 кандидата ядра и прогнать лакмус-тест.

## Backlog
- (пусто)
```

### Вариант development

Для `development` минимум: `Current Milestone` (ссылка на пункт `plan.md`), `Active Step`, `Пользовательский результат шага`, `Exit Criteria`, `Drift Guard (short)`, `Next`. Блокеры — в `plan.md §Blockers`, не здесь.

```markdown
# Tasks

Task Mode: `development`

## Current Milestone
[M1 — Каркас](./plan.md#m1--каркас)

## Active Step
- [ ] Инициализировать репозиторий и собрать пустой каркас.

## Пользовательский результат шага
Владелец может запустить минимальную рабочую версию и проверить основной сценарий.

## Exit Criteria
- Проект собирается, самопроверка проходит.

## Drift Guard (short)
- Не добавлять функции вне состава первой версии.

## Next
- [ ] Реализовать ядро по техническому заданию.

## Backlog
- (пусто)
```

## log.md — хронология

Первая запись — создание проекта. Формат: дата + заголовок + 3–7 буллетов. Подробный контент — в отдельные артефакты, не в log (Правило 5).

```markdown
---
id: 2026-acme-shop-positioning-strategy-log
type: log
status: active
created: 2026-07-10
updated: 2026-07-10
aliases:
  - "Журнал — позиционирование Acme Shop"
tags: [project, log, acme-shop, positioning]
source_path: "01_now/projects/2026-acme-shop-positioning-strategy/log.md"
knowledge_criticality: medium
verification_status: unverified
curation_mode: llm_explicit_request
---

# Project Log

## Суть
Ключевые решения и изменения состояния проекта позиционирования Acme Shop.

## Детали

### 2026-07-10 — Создан проект
- Проект выделен из обсуждения в чате: Acme Shop «звучит как все», нужно ядро позиционирования.
- Зафиксированы цель, границы (только ядро, не лендинг), режим `operational`.
- План составлен агентом: 3 рубежа (карта поля → кандидаты → выбор), критерии качества заданы.
- Принятые допущения: российский рынок, прямые конкуренты; зафиксированы в Intent Lock.
- Источник обсуждения — текущий чат; ключевые материалы переносятся в context.md по мере подключения.

## Следующий шаг
Начать M1: карта конкурентного поля.
```

## Обновление индексов

### 01_now/README.md — каталог проектов по контурам

Добавь проект в актуальный каталог под нужным контуром. Формат строки — как у соседних записей файла (сверься с ним перед правкой, стиль может отличаться):

```markdown
- [Позиционирование Acme Shop](./projects/2026-acme-shop-positioning-strategy/README.md) — выбор ядра позиционирования. `operational`, active.
```

### 01_now/projects/README.md

Каталог здесь автогенерируется в блоке `AUTOGEN-NAV` — вручную список подкаталогов не трогай. Достаточно, что папка с `README.md` создана; при следующем прогоне автонавигации проект появится. Если автогенерация не запускается сама — добавь строку в блок вручную, сохранив формат.

## Заметка по development-проектам

Для режима `development` дополнительно создай из `meta/templates/` артефакты dev-протокола: `AGENT_WORKFLOW.md`, `TEST_PLAN.md`, `RELEASE_CHECKLIST.md`, `CHANGELOG.md`, `INCIDENT_RUNBOOK.md` (см. [dev-protocol](../../../meta/rules/dev-protocol.md)). Они не заменяют пять базовых файлов, а дополняют их для кодовых проектов.
