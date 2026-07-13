---
id: github-pull-request-template
type: reference
status: active
created: 2026-07-13
updated: 2026-07-13
aliases:
  - "Шаблон заявки на изменение"
tags: [template, github, review]
source_path: "meta/templates/github_pull_request_template.md"
---

# Суть

Коротко опиши изменение в 2-4 предложениях.

## Что изменено

- 

## Зачем

- 

## Затронутые файлы

- 

## Риск закрытых данных

- [ ] Я проверил, что изменение не добавляет закрытые, персональные, финансовые, юридические данные, секреты или сырые импорты.
- [ ] Если риск есть, он описан ниже.

Комментарий:

## Проверки

```bash
python3 scripts/check_links.py
python3 scripts/check_forbidden_markers.py
python3 scripts/check_repository_manifest.py .
```

## Что должен проверить человек

- 
