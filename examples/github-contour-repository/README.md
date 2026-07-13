---
id: example-github-contour-repository-readme
type: index
status: active
created: 2026-07-13
updated: 2026-07-13
aliases:
  - "Пример контурного GitHub-репозитория"
tags: [example, github, contours]
source_path: "examples/github-contour-repository/README.md"
---

# Example Contour Repository

## Суть

Безопасный пример контурного GitHub-репозитория без реальных компаний, людей и закрытых данных.

Он показывает, как отделить правила агента, машинно-читаемый манифест, состояние работы и заявку на изменение.

## Как читать пример

1. [AGENTS.md](./AGENTS.md) — короткие правила агента для этого контура.
2. [repository-manifest.yml](./repository-manifest.yml) — границы репозитория и действия, где нужно спросить человека.
3. [context.md](./context.md) — устойчивый контекст.
4. [plan.md](./plan.md) — цель и рубежи.
5. [tasks.md](./tasks.md) — ближайший шаг исполнения.
6. [log.md](./log.md) — история значимых изменений.
7. [materials/example-note.md](./materials/example-note.md) — безопасная учебная заметка.

## Проверка

Из корня стартового комплекта:

```bash
python3 scripts/validate_contour_repo.py examples/github-contour-repository
```

## Что здесь намеренно упрощено

- Нет реальных персональных, финансовых, юридических и коммерчески чувствительных данных.
- Нет внешнего трекера задач.
- Нет закрытого слоя.
- Пример показывает только один обычный контур и один безопасный материал.

## Следующий шаг

Скопируй структуру примера в новый репозиторий, замени владельца, контур и правила доступа, затем запусти проверку.
