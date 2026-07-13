---
id: example-contour-note
type: note
status: active
created: 2026-07-13
updated: 2026-07-13
aliases:
  - "Учебная заметка контура"
tags: [example, material]
source_path: "examples/github-contour-repository/materials/example-note.md"
sensitivity: ordinary
---

# Учебная заметка

## Суть

Это безопасный материал для проверки, что агент умеет работать с контурным репозиторием без закрытых данных.

## Детали

Заметка может быть изменена агентом без дополнительного вопроса, потому что путь `materials/**/*.md` разрешён в `repository-manifest.yml`.

Если бы заметка содержала закрытые данные, агент должен был бы остановиться и спросить человека до записи.

## Следующий шаг

Использовать файл для учебной заявки на изменение.
