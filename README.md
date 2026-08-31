# ai-skills

Набор ИИ-скиллов для работы с SS13 / BYOND, распространяемый как **плагин Claude Code**. Подписался один раз — дальше обновления приходят сами. Скиллы предоставляются «как есть», вы их используете на свой страх и риск.

A set of AI skills for SS13 / BYOND work, distributed as a **Claude Code plugin**. Subscribe once; updates follow automatically. Provided "as is" — use at your own risk.

## Установка / Install

```bash
claude plugin marketplace add PatapoIIIa/ai-skills
```

```bash
claude plugin install ss13-byond@ss13-ai-skills
```

Внутри Claude Code — то же самое через `/plugin marketplace add PatapoIIIa/ai-skills`, затем `/plugin install ss13-byond@ss13-ai-skills`.

**Про обновления.** В манифесте намеренно не задано поле `version`: версией считается git SHA, поэтому вы всегда получаете актуальный коммит ветки по умолчанию — без ручного повышения версий с моей стороны и без переустановки с вашей. Обновить прямо сейчас: `/plugin marketplace update ss13-ai-skills`.

*On updates: `version` is deliberately omitted from the manifest, so the git SHA acts as the version and you always track the default branch's latest commit. Force a refresh with `/plugin marketplace update ss13-ai-skills`.*

## Дерево зависимостей / Dependency tree

Один контроллер маршрутизирует задачу; архитектурные скиллы не знают друг о друге и не дублируют логику маршрутизации.

```mermaid
graph TD
    U([Задача / Task]) --> C{{byond-codemaster-controller}}

    C -->|хостинг, TGS, Docker| D[ss13-tgs-deploy]
    C -->|размещение на форке| M[tgstation-modular-content]
    C -->|интерфейс| T[ss13-tgui]
    C -->|DM-код, ревью, перф| K[byond-ss13-coding]
    C -->|база форка| B[(ai_navigation/)]

    K -.->|граница ui_data / ui_act| T
    M -.->|размещение решается раньше кода| K
    B -.->|код важнее базы| K

    classDef ctrl fill:#1e3a5f,stroke:#60a5fa,stroke-width:2px,color:#fff
    classDef ops fill:#4a3410,stroke:#f59e0b,color:#fff
    classDef data fill:#3b2a5c,stroke:#a78bfa,color:#fff
    class C ctrl
    class D ops
    class B data
```

Сплошные стрелки — маршрутизация (кто выполняет). Пунктирные — отношения между скиллами: `byond-ss13-coding` отдаёт всё за границей `ui_data`/`ui_act` в `ss13-tgui`; `tgstation-modular-content` решает *куда положить* раньше, чем другие решают *что написать*; семантическая база — подсказка для навигации, код всегда важнее.

*Solid edges = routing (who implements). Dashed = inter-skill contracts: the DM skill hands everything past the `ui_data`/`ui_act` boundary to the TGUI skill; placement is decided before implementation; a semantic base is a routing aid that never outranks code.*

## Что внутри / What's inside

| Скилл | Роль |
|---|---|
| `byond-codemaster-controller` | Маршрутизация (два гейта), контракт взаимодействия, жизненный цикл семантических баз |
| `byond-ss13-coding` | DM-семантика, архитектура SS13, производительность, ревью — авторитет по инвариантам движка |
| `ss13-tgui` | TGUI-интерфейсы, мост ByondUi, разбор проблем клиента |
| `tgstation-modular-content` | Размещение контента на форках, переживающее upstream sync |
| `ss13-tgs-deploy` | Развёртывание сервера через TGS/Docker — ось операций, вне стека кода |

- Документация (RU): [docs/skills-guide.ru.md](docs/skills-guide.ru.md)
- Documentation (EN): [docs/skills-guide.en.md](docs/skills-guide.en.md)
- Метрики и тесты (RU): [docs/benchmarks.ru.md](docs/benchmarks.ru.md)
- Benchmarks & tests (EN): [docs/benchmarks.en.md](docs/benchmarks.en.md)

Папки `ai_navigation_*` в корне — это семантические базы конкретных форков (данные, не скиллы). Они **не входят в плагин** и подписчикам не поставляются.

## Метрики / Benchmarks

Численный A/B-тест `byond-ss13-coding`: одна и та же задача, параллельно, одна и та же модель — с скиллом и без. Полная методология и ограничения: [docs/benchmarks.ru.md](docs/benchmarks.ru.md) / [docs/benchmarks.en.md](docs/benchmarks.en.md).

Numeric A/B test of `byond-ss13-coding`: same task, in parallel, same model — with the skill vs. without. Full methodology and limitations: [docs/benchmarks.en.md](docs/benchmarks.en.md) / [docs/benchmarks.ru.md](docs/benchmarks.ru.md).

**Track A — code review, 9 planted defects / Трек A — код-ревью, 9 заложенных дефектов**

| Metric / Метрика | With skill / Со скиллом | Without / Без скилла |
|---|---|---|
| Defects found / Найдено дефектов | **9 / 9 (100%)** | 8 / 9 (89%) |
| False positives / Ложные срабатывания | 0 | 0 |
| Tokens / Токены | 70,500 | 44,400 |
| Time / Время | 201 s | 128 s |

**Track B — engine-fact quiz, 10 questions / Трек B — квиз по фактам движка, 10 вопросов**

| Metric / Метрика | With skill / Со скиллом | Without / Без скилла |
|---|---|---|
| Correct / Верных ответов | **10 / 10** | 7.5 / 10 |
| Tokens / Токены | 46,200 | 37,100 |
| Time / Время | 19 s | 43 s |

**Track E — false-positive stress test (fixed patch) / Трек E — стресс-тест на ложные срабатывания (исправленный патч)**

| Metric / Метрика | With skill / Со скиллом |
|---|---|
| False positives / Ложные срабатывания | **0** |
| Nitpicks correctly rejected / Отклонённых придирок | 3 |

**Track C — independent fact audit of the skill itself / Трек C — независимый аудит фактов скилла**

| Metric / Метрика | Result / Результат |
|---|---|
| Confirmed / Подтверждено | **10 / 10** |
| Contradicted / Опровергнуто | 0 |

**4-skill linkage economy / Экономность связки 4 скиллов**

| Metric / Метрика | Value / Значение |
|---|---|
| Documents loaded / Загружено документов | 9 (of 20+ available / из 20+ доступных) |
| Routing loops / Циклов маршрутизации | 0 |
| Unused loads / Неиспользованных загрузок | 0 |

**Dollar cost @ Claude Sonnet 5 intro rates ($2/$10 per 1M in/out) / Стоимость в деньгах**

| Track / Трек | Δ tokens / Δ токенов | Est. cost / Оценка стоимости |
|---|---|---|
| A (review / ревью) | +26,100 | ~$0.05–0.10 / run |
| B (quiz / квиз) | +9,100 | ~$0.02–0.03 / run |

**Bottom line / Итог:** the skill's overhead (+25–59% tokens, a few cents per run) pays for itself on a single prevented incident — the one defect the baseline missed belongs to the most expensive bug class there is: "compiles clean, breaks live in production."

Оверхед скилла (+25–59% токенов, единицы центов за прогон) окупается уже на одном предотвращённом инциденте — единственный пропущенный baseline'ом дефект относится к самому дорогому классу ошибок: «компилируется зелёным, ломается у живых игроков».
