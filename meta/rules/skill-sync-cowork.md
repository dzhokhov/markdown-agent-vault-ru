---
id: skill-sync-cowork
type: rules
status: active
created: 2026-04-22
updated: 2026-05-06
aliases:
  - "Синхронизация скиллов Cowork"
  - "Правило синхронизации скиллов"
tags: [rules, skills, cowork, sync]
source_path: "meta/rules/skill-sync-cowork.md"
globs: "skills/**"
---

# Правило: доставка скиллов vault в Cowork

## Когда срабатывает

При любом изменении файлов в `skills/`: создание нового скилла, редактирование `SKILL.md`, удаление скилла, сборка или обновление Cowork-пакета.

## Суть

Vault (`skills/`) — единственный долговременный источник правды для кастомных скиллов.

На 2026-05-06 проверено: встроенный пакет Cowork `anthropic-skills` загружается как управляемый приложением пакет `anthropic-skills@inline`. Его физическая папка в `~/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin/.../skills/` и соседний `manifest.json` могут быть перезаписаны Cowork после перезапуска или пересборки сессии. Поэтому `rsync` в `skills-plugin` и правка `manifest.json` — только диагностический/временный слой, а не надёжная доставка новых скиллов.

Надёжный путь для новых vault-скиллов в Cowork — отдельный пользовательский ZIP-плагин, загружаемый через `Customize` → `upload custom plugin file`.

## Что делать агенту

### После редактирования скилла, входящего в Cowork-пакет

1. Обнови исходный скилл в `skills/<name>/`.
2. Если скилл входит в пакет `vault-custom-skills`, запусти:

```bash
./skills/build-cowork-vault-plugin.sh
```

3. Проверь, что ZIP собран:

```bash
unzip -l skills/dist/vault-custom-skills-0.1.0.zip
```

4. Сообщи владельцу: «ZIP-плагин обновлён. Для Cowork его нужно загрузить через `Customize` → `upload custom plugin file`; после установки скилл будет доступен как `vault-custom-skills:<name>`».

### После создания нового скилла

1. Спроси владельца, нужен ли этот скилл именно в Cowork.
2. Если да:
   - добавь имя скилла в массив `PLUGIN_SKILLS` в `skills/build-cowork-vault-plugin.sh`;
   - пересобери ZIP через `./skills/build-cowork-vault-plugin.sh`;
   - при необходимости обнови `README.md` плагина и этот документ.
3. Не обещай появление нового скилла как `anthropic-skills:<name>`. Для пользовательского ZIP-плагина ожидаемый префикс — имя плагина, сейчас `vault-custom-skills:`.

### После удаления скилла

1. Если скилл входил в `vault-custom-skills`, убери его из `PLUGIN_SKILLS` в `skills/build-cowork-vault-plugin.sh`.
2. Пересобери ZIP.
3. Сообщи владельцу, что в уже установленном Cowork-плагине может потребоваться повторная загрузка ZIP или удаление старой версии через интерфейс Cowork.

## Текущий Cowork-пакет

Канонический пакет для трёх новых скиллов:

- исходная папка: `skills/cowork-vault-custom-skills-plugin/`
- ZIP для загрузки: `skills/dist/vault-custom-skills-0.1.0.zip`
- сборка: `skills/build-cowork-vault-plugin.sh`

Состав:

- `product-demo-analysis`
- `personal-essay-writer`
- `owner-voice-writer`
- `task-tracker-writer`
- `project-creator`

Ожидаемые имена после установки в Cowork:

- `vault-custom-skills:product-demo-analysis`
- `vault-custom-skills:personal-essay-writer`
- `vault-custom-skills:owner-voice-writer`
- `vault-custom-skills:task-tracker-writer`
- `vault-custom-skills:project-creator`

## Роль старого sync-скрипта

`skills/sync-cowork-skills.sh` можно использовать для:

- поддержки `~/.claude/skills/` для хостовых инструментов;
- диагностики старого `skills-plugin` кэша;
- временной проверки гипотез после обновлений Cowork.

Но успешные `copy ✓` и `manifest ✓` в старом кэше больше не считаются доказательством, что новый скилл будет доступен в Cowork. Управляемый пакет может быть перезаписан.

## Чего не делать

- Не редактировать `~/.claude/skills/`, `skills-plugin` или `manifest.json` как долговременный источник.
- Не считать `INCLUDE_SKILLS` гарантией доступности в Cowork.
- Не обещать, что новые скиллы появятся рядом со встроенными `anthropic-skills:*`.
- Не добавлять в Cowork-пакет скиллы, завязанные на инструменты, недоступные в Cowork.
