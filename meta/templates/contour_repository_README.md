---
id: contour-repository-readme-template
type: reference
status: active
created: 2026-07-13
updated: 2026-07-13
aliases:
  - "Шаблон README контурного репозитория"
tags: [template, github, contours]
source_path: "meta/templates/contour_repository_README.md"
---

# <Название контура>

## Суть

Коротко: что это за контур, кто им владеет и зачем существует этот репозиторий.

## Правила чтения

Перед работой агент читает:

1. [AGENTS.md](./AGENTS.md);
2. [repository-manifest.yml](./repository-manifest.yml);
3. [context.md](./context.md);
4. [plan.md](./plan.md) и [tasks.md](./tasks.md), если задача связана с текущим исполнением.

## Что здесь хранится

- `context.md` — устойчивые знания и ограничения контура.
- `plan.md` — цель, границы и крупные рубежи работы с контуром.
- `tasks.md` — ближайшая очередь исполнения самого markdown-слоя.
- `log.md` — короткая история решений и значимых изменений.
- `materials/` — рабочие материалы, разрешённые манифестом.

## Что здесь не хранится

- Закрытые данные, если репозиторий не предназначен для них.
- Сырые импорты внешних систем.
- Секреты и ключи доступа.
- Большие медиафайлы без явного решения.
- Материалы другого контура.

## Проверки

```bash
python3 scripts/validate_contour_repo.py .
```

## Следующий шаг

Заполнить `repository-manifest.yml`, затем проверить репозиторий локально.
