# Установка скиллов и субагентов для Claude Code

Этот документ описывает установку команды в Claude Code. Установка для Codex описана в [соседнем документе](./agent-installation.md); обе установки независимы и не мешают друг другу.

## Канонические файлы

- Вариант управляющего скилла для Claude Code: `skills/owner-only-dev-orchestrator/claude/SKILL.md`.
- Девять субагентов: `skills/owner-only-dev-orchestrator/assets/agents-claude/*.md`.
- Десять ролевых скиллов платформенно нейтральны и используются без изменений из `skills/`.
- Установщик: `skills/owner-only-dev-orchestrator/install-claude-code.sh`.

## Пользовательские скиллы

Claude Code обнаруживает личные скиллы в `~/.claude/skills/`. Там должны находиться символические ссылки:

| Ссылка | Цель в хранилище |
|---|---|
| `owner-only-dev-orchestrator` | `skills/owner-only-dev-orchestrator/claude/` |
| `product-owner` | `skills/product-owner/` |
| `productologist` | `skills/productologist/` |
| `solution-architect` | `skills/solution-architect/` |
| `architecture-critic` | `skills/architecture-critic/` |
| `architecture-fixer` | `skills/architecture-fixer/` |
| `implementation-developer` | `skills/implementation-developer/` |
| `test-gates` | `skills/test-gates/` |
| `test-fixer` | `skills/test-fixer/` |
| `technical-documenter` | `skills/technical-documenter/` |
| `release-rollback` | `skills/release-rollback/` |

Ссылка предпочтительнее копии: канонический текст остаётся один, а установленная версия не расходится с хранилищем.

## Пользовательские субагенты

Claude Code загружает личных субагентов из `~/.claude/agents/`. Там должны находиться девять ссылок на канонические файлы из `assets/agents-claude/`:

- `product-owner.md`;
- `productologist.md`;
- `dev-architect.md`;
- `architecture-critic.md`;
- `architecture-fixer.md`;
- `implementation-developer.md`;
- `independent-tester.md`;
- `test-fixer.md`;
- `technical-documenter.md`.

Соответствие имён Codex → Claude Code: `product_owner → product-owner`, `productologist → productologist`, `dev_architect → dev-architect`, `architecture_critic → architecture-critic`, `architecture_fixer → architecture-fixer`, `implementation_developer → implementation-developer`, `independent_tester → independent-tester`, `test_fixer → test-fixer`, `technical_documenter → technical-documenter`. Claude Code требует имена из строчных букв и дефисов, поэтому подчёркивания заменены дефисами; распределение ролей не изменилось.

## Перенос ограничений полномочий

| Ограничение Codex | Реализация в Claude Code |
|---|---|
| `architecture_critic`: `sandbox_mode = "read-only"` | Поле `tools: Read, Grep, Glob` — у субагента физически нет инструментов записи и команд |
| `independent_tester`: `workspace-write` + запрет менять отслеживаемые файлы | Поле `tools: Read, Grep, Glob, Bash` — команды разрешены, правка файлов недоступна; скилл требует доказательства через `git status` до и после |
| Продуктовые роли: запись только решения, команды не нужны | `tools: Read, Grep, Glob, Write, Edit` |
| Остальные роли: `workspace-write` | `tools: Read, Grep, Glob, Write, Edit, Bash` |
| `skills.config.path` на ролевой скилл | Первая обязательная инструкция субагента: прочитать и выполнять `SKILL.md` роли по абсолютному пути |
| Отдельные сеансы агентов | Каждый вызов инструмента `Agent` создаёт отдельный контекст; субагентам не выдан инструмент `Agent`, вложенные запуски невозможны |
| Отдельные ветки и рабочие копии Git | Требование процедуры управляющего скилла, как и в Codex |

## Проверка установки

1. Проверь одиннадцать ссылок в `~/.claude/skills/` через `readlink` и существование одиннадцати целевых `SKILL.md`.
2. Убедись, что в `~/.claude/agents/` есть девять файлов и каждый разрешается в канонический файл хранилища.
3. Разбери YAML-шапку каждого субагента: имя совпадает с именем файла, поле `tools` присутствует.
4. Убедись, что `architecture-critic` имеет только `Read, Grep, Glob`.
5. Убедись, что `independent-tester` имеет `Read, Grep, Glob, Bash` без `Write` и `Edit`, а его инструкции требуют проверять состояние Git.
6. Проверь, что путь к ролевому скиллу внутри каждого субагента существует.
7. В новом сеансе Claude Code выполни `/owner-only-dev-orchestrator` на безопасном задании и убедись, что архитектор и критик запускаются отдельными субагентами, а критик не пишет файлы.

Шаги 1–6 выполняет автоматически `install-claude-code.sh --verify`.

## Перенос хранилища

Пути к ролевым `SKILL.md` внутри субагентов абсолютны для текущего компьютера. После переноса хранилища запусти `install-claude-code.sh` заново с новым корнем: он пересоздаст ссылки и проверит пары. Не считай старую установленную копию или ссылку источником правды.
