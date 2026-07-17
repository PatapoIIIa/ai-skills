# ai-skills
Набор ИИ скиллов для работы с СС13. Скиллы предоставляются "как есть", вы их используете на свой страх и риск.

A set of AI skills for working with SS13. These skills are provided "as is" and you use them at your own risk.

- Документация (RU): [docs/skills-guide.ru.md](docs/skills-guide.ru.md)
- Documentation (EN): [docs/skills-guide.en.md](docs/skills-guide.en.md)
- Метрики и тесты (RU): [docs/benchmarks.ru.md](docs/benchmarks.ru.md)
- Benchmarks & tests (EN): [docs/benchmarks.en.md](docs/benchmarks.en.md)

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
