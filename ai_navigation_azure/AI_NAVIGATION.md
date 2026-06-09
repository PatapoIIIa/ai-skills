# FamilyTree Module AI Navigation

Актуально для `C:/Axis/Twilight-Axis/modular_twilight_axis/familytree_module` на 2026-04-24.

Эта инструкция нужна, чтобы быстро входить в подсистему семей без широкого сканирования репозитория. Код остается источником истины: если этот файл расходится с `.dm`/`.tsx`, доверяй исходникам и обнови карту.

## Старт Работы

- Начинай с `familytree_module_config.dm`: это include-root и актуальная карта файлов модуля.
- Не открывай и не правь `.dme`; порядок загрузки не задача агента без явного апрува пользователя.
- Игнорируй `_compile_options.dm`.
- Не запускай компиляцию, debug-сценарии, внешние тестовые скрипты и in-game симуляции без явного запроса пользователя.
- Учитывай грязный worktree и не откатывай чужие изменения.
- Для поиска сначала используй точечные `rg` по `modular_twilight_axis/familytree_module`, потом расширяйся в `tgui/packages/tgui/interfaces` или `code/**`.
- **Перед любой правкой этой подсистемы пройди по Subsystem Development Protocol (в конце файла) и составь impact-list.**

Быстрые команды — в разделе "Fast Search Commands" в конце файла.

## Agent TL;DR

Куда идти для какой задачи (primary files → related layers):

| Задача | Открывать сначала | Затрагиваемые смежные слои |
|---|---|---|
| Настройки семьи в UI | `familytree_prefs_ui.dm`, `FamilySettingsPanel.tsx` | `FamilySettingsPanel.scss`, `load_familytree_runtime_preferences` |
| Сохранение prefs (savefile) | `familytree_prefs_ui.dm` (`familytree_module_save_character` / `_load_character` / `_sanitize_character`) | `familytree_module_config.dm` константы |
| Режимы семьи / saved pref mapping | `familytree_module_config.dm` + `familytree_prefs_ui.dm` (`_family_to_ui`, `_ui_to_family`) | `FamilySettingsPanel.tsx` |
| Автоматическое назначение семьи | `familytree_subsystem_core.dm` + `familytree_subsystem_matching.dm` | `familytree_lifecycle.dm` для confirmations |
| Matching spouse/family/favorite name | `familytree_subsystem_matching.dm` | `familytree_subsystem_helpers.dm`, `familytree_social.dm`, `familytree_lifecycle.dm` |
| Species/anatomy/gender compatibility | `familytree_subsystem_helpers.dm` | `familytree_subsystem_royal.dm` для royal partner jobs |
| Отношения / названия родственников | `familytree_member.dm` | `familytree_graph_api.dm`, `familytree_heritage_core.dm` |
| Отображение дерева | `familytree_heritage_core.dm` + `familytree_graph_api.dm` | `FamilyDisplayPanel/*.tsx` |
| Graph / caching / dirty validation | `familytree_graph_support.dm` + `familytree_graph_api.dm` | `familytree_member.dm`, `familytree_heritage_core.dm` |
| Royal / monarch / hand / progeny flow | `familytree_subsystem_royal.dm` + `familytree_lifecycle.dm` | `familytree_subsystem_core.dm` routing |
| Estates / role tiers / polygamy | `familytree_social.dm` | matching, prefs UI |
| Церковные family bonds | `familytree_holy_verbs.dm` + `familytree_rituals.dm` | graph API, `family_member` |
| Диагностика / ручное наполнение домов | `familytree_debug.dm` + `familytree_debug_populate.dm` | graph API (admin/debug only) |
| Кольца и stash-выдача | `familytree_subsystem_matching.dm` `give_wedding_ring()` | base item: `code/modules/clothing/rogueclothes/rings.dm` |

## Include / Compile Map

`familytree_module_config.dm` — compile hub. Он:

1. Определяет saved compatibility macros (`FAMILY_NONE`/`FAMILY_PARTIAL`/`FAMILY_NEWLYWED`/`FAMILY_FULL`) с `#ifndef` guards.
2. Определяет runtime masks (`FAMILYTREE_MODE_*`, `FAMILYTREE_JOIN_CREATE_DELAY`, `FAMILYTREE_RELATIVE_JOIN_DELAY`).
3. Определяет gender / family-label / polygamy / relative / reject-reason bitmask константы.
4. Подключает файлы модуля в порядке:
   1. `familytree_prefs_ui.dm`
   2. `familytree_mob_procs.dm`
   3. `familytree_heritage_core.dm`
   4. `familytree_member.dm`
   5. `familytree_social.dm`
   6. `familytree_storytellers.dm`
   7. `familytree_rituals.dm`
   8. `familytree_holy_verbs.dm`
   9. `familytree_lifecycle.dm`
   10. `familytree_subsystem_core.dm`
   11. `familytree_subsystem_helpers.dm`
   12. `familytree_subsystem_matching.dm`
   13. `familytree_subsystem_royal.dm`
   14. `familytree_graph_support.dm`
   15. `familytree_graph_api.dm`
   16. `familytree_debug.dm`
   17. `familytree_debug_populate.dm`

`familytree_module_deinclude.dm` снимает все макросы модуля после compile-секции.

Обязательно:

- Любой новый `#define` в `familytree_module_config.dm` должен получить соответствующий `#undef` в `familytree_module_deinclude.dm`. Иначе макрос утечёт в другие модули.
- Любой новый файл модуля добавляется в FILE MAP, в `#include` последовательность `familytree_module_config.dm` и в раздел "Состав Модуля" этого файла.

## Состав Модуля

- `familytree_module_config.dm` — defines, include-root, reject bitmasks, file map.
- `familytree_module_deinclude.dm` — очистка макросов после compile-секции.
- `familytree_prefs_ui.dm` — vars на prefs/human, savefile load/save/sanitize, display panel datum, TGUI-backend настроек (`/datum/family_options`).
- `familytree_mob_procs.dm` — `MarryTo()`, player verbs, known families, UI toggles, spouse/bond display, `familytree_module_open_preferences` entry.
- `familytree_heritage_core.dm` — `/datum/heritage`: house, members, marriage, species calculation, family tree data, icons, curses.
- `familytree_member.dm` — `/datum/family_member`: graph-facing accessors, relation terms, `GetRelationshipTo()`, phantom links.
- `familytree_social.dm` — estates, high/low role tiers, polygamy и lore-based polygyny/polyandry.
- `familytree_storytellers.dm` — storyteller influence (Astrata / Eora / Baota / Xylix / Psaidon), intimacy tracking, house karma.
- `familytree_rituals.dm` — clergy helpers, desired relative role, `familytree_ritual_adopt`, `familytree_vampire_bind`, `/datum/family_curse`.
- `familytree_holy_verbs.dm` — holy skill spells: `familytree_establish_bond`, `familytree_dissolve_marriage`, manual marriage/adoption/sibling rituals.
- `familytree_lifecycle.dm` — latejoin royal hooks, Enigma tier integration, noble dynasty, notifications, confirmation sessions (`/datum/family_confirm_session`, `request_family_confirmation`, `request_mutual_confirmation`), setspouse reset offer.
- `familytree_subsystem_core.dm` — `SUBSYSTEM_DEF(familytree)`: init, signals, queue, local/royal assignment runners, Xylix roulette.
- `familytree_subsystem_helpers.dm` — species/anatomy compatibility, job helpers, royal status predicates, age checks, `DetermineAppropriateRole`.
- `familytree_subsystem_matching.dm` — local matching, joining houses, forming new families, favorite matching, wedding rings, desired-role assignment.
- `familytree_subsystem_royal.dm` — royal partner jobs, optional royal hand family offer, royal lineage generation.
- `familytree_graph_support.dm` — `/datum/family_node`, `/datum/family_edge`, `/datum/family_graph_cache`, validation/debug helpers.
- `familytree_graph_api.dm` — SSfamilytree graph facade, legacy hook sync, relation/display cache.
- `familytree_debug.dm` — debug/admin сценарии (stress, royal, favorite, isolated, edge, lifecycle, roles). Admin only.
- `familytree_debug_populate.dm` — "populate my house" панель (`ftpop_*` procs). Admin only.
- `relations.dmi` — relation/adoption/spouse image asset.
- TGUI вне модуля:
  - `tgui/packages/tgui/interfaces/FamilySettingsPanel.tsx`
  - `tgui/packages/tgui/styles/interfaces/FamilySettingsPanel.scss`
  - `tgui/packages/tgui/interfaces/FamilyDisplayPanel.tsx`
  - `tgui/packages/tgui/interfaces/FamilyDisplayPanel/FamilyListSections.tsx`
  - `tgui/packages/tgui/interfaces/FamilyDisplayPanel/FamilyTree.tsx`
  - `tgui/packages/tgui/interfaces/FamilyDisplayPanel/FamilyTreeBranch.tsx`
  - `tgui/packages/tgui/interfaces/FamilyDisplayPanel/FamilyTreeCard.tsx`
  - `tgui/packages/tgui/interfaces/FamilyDisplayPanel/types.ts`

## Текущая Модель Режимов

В UI должно быть три режима:

- `FAMILY_NONE` / `"none"` — без семьи. Обычная локальная семейная система не назначает персонажа.
- `FAMILY_NEWLYWED` / `"couple"` — создать семью. Игрок ищет супруга для нового дома. Он не должен быть присоединён к уже существующей семье через этот режим.
- `FAMILY_PARTIAL` / `"member"` — присоединиться к семье. Игрок ищет существующий дом на выбранной роли. Если выбран `RELATIVE_SPOUSE`, он может либо вступить супругом в существующий дом, либо стать супругом игрока из `FAMILY_NEWLYWED`; главой нового дома остается тот, кто выбрал создание семьи.

`FAMILY_FULL` — legacy-значение; sanitation переводит его в `FAMILY_PARTIAL`, UI больше не показывает отдельную карточку "родитель".

Legacy `"parent"` UI string всё ещё существует в `_ui_to_family` (`familytree_prefs_ui.dm:410`) и мапится в `FAMILY_PARTIAL` — compatibility layer. Не удалять без отдельной причины.

`desired_relative_role` имеет смысл для `FAMILY_PARTIAL` и `FAMILY_NEWLYWED`. Для `FAMILY_PARTIAL` это желаемая роль вступления в дом. Для `FAMILY_NEWLYWED` это роль создателя в новом доме: создатель с `RELATIVE_PARENT` остаётся в поиске супруга, но при последующем присоединении детей/родственников система предпочитает цеплять их к нему как к родителю. Остальные режимы санитайзят роль в `RELATIVE_ANY`.

## Data Model

Гибридная модель: heritage-container + family_member wrapper + graph layer.

### `/datum/heritage` (familytree_heritage_core.dm)

House/family container. Хранит: `housename`, `members`, `member_nodes`, founder, house leader, dominant race, closed-state, curses, display/list logic.

Ключевые procs:

- `CreateFamilyMember(person)` — создаёт `/datum/family_member`, регистрирует node в графе.
- `RemovePersonFromFamily(person)`
- `AddToFamily(person, parent1, parent2, adopt)` — через `member.AddParent` + graph hooks.
- `MarryMembers(member1, member2)` — через `member.AddSpouse` + graph hook.
- `ListFamily()`, `BuildFamilyTreeRoots()`, `BuildFamilyDisplayEntry()`, `AddFamilyDisplaySections()`.

### `/datum/family_member` (familytree_member.dm)

Person-facing relation wrapper. Хранит: `person`, `family`, `generation`, `adoption_status`, `phantom_parent_members`, `phantom_child_members`, cloned look, relation terms.

Normal parent/spouse relations резолвятся через graph layer. Phantom parent/child остаются как локальные списки (для призрачных предков/детей, у которых нет реального `person`).

Ключевые procs (для non-phantom ходят через граф):

- `AddParent(parent)`, `RemoveParent(parent)`
- `AddSpouse(spouse)`, `RemoveSpouse(spouse, divorce)`
- `get_parent_members()`, `get_child_members()` — combine graph + phantom lists.
- `get_spouse_members()`, `get_former_spouse_members()` — читают ТОЛЬКО граф.
- `GetRelationshipTo(other_member)`.

### `/datum/family_node` (familytree_graph_support.dm)

Graph node per human: `person`, `primary_house`, `edges` list.

### `/datum/family_edge` (familytree_graph_support.dm)

Graph edge с `relation_type`: `"parent_child"`, `"adoptive_parent_child"`, `"spouse"`, `"former_spouse"`. Хранит обе стороны и тип.

### `/datum/family_graph_cache` (familytree_graph_support.dm)

Relation/display/generation cache per house. Флаги: `dirty_relations`, `dirty_generations`, `dirty_display`. `mark_dirty()` выставляет флаги избирательно.

### Source of truth

**Граф — источник истины для нормальных parent/spouse edge-ей.** Не писать документацию, что parents/spouses хранятся ТОЛЬКО как прямые списки на `family_member` — это устаревшее понимание. `family_member` методы `AddParent`/`AddSpouse` вызывают graph hooks, а чтение идёт через `get_*_members()` комбайн.

Phantom родители/дети живут как прямые списки на `family_member` (нет `person`, не создают graph node).

### Graph API (familytree_graph_api.dm)

- `SSfamilytree.get_or_create_family_node(person)`
- `SSfamilytree.graph_on_member_created(member)`
- `SSfamilytree.graph_on_parent_added(child_member, parent_member, adopted)`
- `SSfamilytree.graph_on_spouse_added(member_a, member_b)`
- `SSfamilytree.graph_on_spouse_removed(member_a, member_b, former)`
- `SSfamilytree.graph_sync_adoption_status(child_member, parent_member, adopted)`
- `SSfamilytree.mark_family_dirty(family, flags)`
- `SSfamilytree.get_cached_relation(looker_member, lookee_member)`
- `SSfamilytree.get_display_tree_for(family, checker_member)`

Всегда помечать кэш dirty при мутации графа.

## Runtime Assignment Flow

```text
SSfamilytree.Initialize()
  -> creates ruling_family
  -> builds preset family species houses
  -> creates isolated species houses (gnolls, goblins)
  -> snapshots and closes royal partner jobs
  -> checks Xylix roulette (check_xylix_roulette)
  -> loads Enigma tier additions (load_enigma_roles)
  -> registers mob-created signal
  -> registers existing humans via register_human()
  -> schedules holy spell scan
```

`register_human(H)` биндит на человека сигналы:

- `COMSIG_MOB_LOGIN`
- `COMSIG_MOB_LOGOUT`
- `COMSIG_MOB_DEATH`
- `COMSIG_LIVING_REVIVE`
- `COMSIG_JOB_RECEIVED`
- `COMSIG_SEX_CLIMAX`

```text
try_queue_assignment(H)
  -> unsubscribe guards: dummy / npc / invalid species / banned antag / wildshape
  -> dead / no-client / already-assigned / already-scheduled / already-viable guards
  -> load_familytree_runtime_preferences(H): copy saved prefs to H runtime mirrors
  -> check_xylix_roulette: if active -> apply_xylix_roulette_preferences(H)
  -> royal_suitor_job -> unsubscribe (bypasses family assignment)
  -> royal_hand_job:
       if monarch exists -> schedule run_royal_hand_assignment_offer (TGUI выбор)
       else -> fall through на normal family prefs
  -> other royal status -> schedule run_royal_assignment
  -> FAMILY_NONE -> stop tracking
  -> else -> schedule run_local_assignment
```

`run_local_assignment()` / `run_royal_assignment()` re-check block reasons перед мутацией. Death ставит паузу; no client отложит; hard-invalid reasons делают unsubscribe.

```text
AddLocal(H, status)
  -> runtime guards
  -> non-hand royal jobs и royal suitor пропускаются
  -> setspouse path уходит в mutual confirmation перед мутацией
  -> noble dynasty только для FAMILY_PARTIAL + RELATIVE_ANY
  -> selected relative role используется для FAMILY_PARTIAL, запоминается для FAMILY_NEWLYWED
  -> FAMILY_PARTIAL:
       RELATIVE_SPOUSE -> find_and_confirm_family -> do_execute_family; если не нашли — ждём FAMILY_NEWLYWED founder
       other selected role -> wait_for_relative_house, solo confirmation, затем do_assign_desired_role()
       auto role -> solo confirmation перед AssignToHouse(); если нет дома — ждём
  -> FAMILY_NEWLYWED:
       find_and_confirm_newlywed() -> mutual confirmation -> do_execute_newlywed();
       созданный дом остаётся открытым для относителей, если leader-pref не закрывает его
```

Matching entry-points:

- `TryAssignToFavorite()` — setspouse / favoriteName; не мутирует напрямую, идёт через confirmation.
- `FindFavoriteMob()` — ищет по families, viable_spouses, alive_mob_list.
- `find_and_confirm_newlywed()` / `do_execute_newlywed()` — пара через mutual confirmation.
- `FindNewlyWedMatch()` — лучший по приоритету newlywed партнёр.
- `find_and_confirm_family()` / `do_execute_family()` — вступление в дом супругом.
- `FindFamilyMatch()` — возвращает `list(house, member)`.
- `AssignToHouse()` — вступление в существующий дом как child/sibling/parent. Forced role для selected relative.
- `AssignToFamily()` — legacy spouse path.
- `AddPersonToHouse()` — core add-to-family.
- `familytree_create_new_relative_house()` — закрытый дом для одиночного родственника.
- `do_execute_targeted_spouse_match()` — форсированный взаимный setspouse.
- `do_assign_desired_role()` — реальное имя для "assign with desired role" (в коде нет `AssignWithDesiredRole`).
- `pick_least_filled_house()` — выбор дома для forced relative роли (в коде нет `pick_weighted_house`; эта функция выбирает наименее заполненный подходящий дом).
- `give_wedding_ring()` — silver wedding ring в `H.mind.special_items["Silver wedding ring"]`, не `SLOT_RING`.

## Matching Rules / Filters

Перед любым matching / mutation проверяются (порядок примерный):

- Species compatibility (`SpeciesCompatible`, `GetSpeciesCompatibilityFailureReason`).
- Isolated species (изолированные дома: goblins/gnolls).
- Sterile species.
- Banned antagonist types / wildshape.
- Age checks (`CanBeParentOf`, `CanBeSiblings`, `WouldCreateAgeConflict`).
- Anatomy compatibility (`AnatomyCompatible`).
- Gender preference (`gender_choice_pref` + partner's `gender_choice_pref`).
- Estates compatibility (`familytree_estates_compatible`).
- Role tiers (`familytree_get_role_tier`, `familytree_role_tiers_compatible`, `allow_low_status_marriage`).
- Polygamy (`familytree_polygamy_compatible`, `familytree_lore_allows_polygyny`, `familytree_lore_allows_polyandry`).
- `setspouse` / `favoriteName` targeting (bypass broad filtering через confirmation).
- `desired_relative_role` forced-role pathway.
- `allow_relatives_in_family`.
- Xylix roulette override (`check_xylix_roulette`): bypass species/polygamy и частично tier при активном шторителлере.

Причины reject диагностируются через `FTREJ_H_*` / `FTREJ_N_*` / `FTREJ_F_*` bitmasks (см. `familytree_module_config.dm`).

## Confirmation System

Solo confirmation:

```text
request_family_confirmation(H, callback, type)
  -> no client: callback immediately
  -> client: tgui_alert, timeout = no
  -> accept: callback
  -> reject / timeout: familytree_opted_out + unsubscribe
```

Mutual confirmation:

```text
request_mutual_confirmation(A, B, callback, type)
  -> no clients: callback immediately
  -> one client: solo confirmation on that side
  -> two clients: /datum/family_confirm_session
  -> both accept: callback
  -> reject / timeout: refuser opts out; other side rescheduled if still eligible
```

`confirm_type`: `"spouse"`, `"family"`, `"house"`, `"dynasty"`, `"sibling_house"`. Timeout ~ 60 секунд (`MUTUAL_CONFIRM_TIMEOUT`).

## Royal Flow

Royal status определяется по джобе (`familytree_subsystem_core.dm`):

- `is_royal_monarch_job` — `/datum/job/roguetown/lord` (parent/monarch branch).
- `is_royal_consort_job` — `/datum/job/roguetown/lady`.
- `is_royal_progeny_job` — `/datum/job/roguetown/prince` (child of monarch).
- `is_royal_hand_job` — `/datum/job/roguetown/hand` (optional branch).
- `is_royal_suitor_job` — `/datum/job/roguetown/suitor` (bypasses normal assignment).
- `get_royal_status(job)` возвращает `FAMILY_FATHER` / `FAMILY_MOTHER` / `FAMILY_PROGENY` / `FAMILY_OMMER` или null.

Процедуры:

- `run_royal_assignment` → `AddRoyal(H, status)`.
- `run_royal_hand_assignment_offer(H)` — ASYNC tgui вопрос. Accept → `AddRoyal(H, FAMILY_OMMER)`. Decline → fallback на normal local flow (если prefs = FAMILY_NONE, то стоп).
- `GetCurrentMonarch()` — ищет gen12 monarch в `ruling_family`.
- `CreateBranchFamily()` — branch house для hand; без dummy spouse.
- `GenerateRoyalLineage()` — 6 поколений предков.

Royal partner jobs (lady, suitor) контролируются prefs монарха:

- `refresh_royal_partner_jobs()` — применяет partner-job state после Init / после job receive.
- `get_royal_partner_mode_from_preferences(monarch)` — `"consort"` / `"suitor"`.
- `royal_partner_candidate_allowed(client, job)` — latejoin-фильтр по species / gender / anatomy prefs монарха и по `setspouse` / favoriteName match.

## Preferences / TGUI Flow

`/datum/preferences` vars (savefile):

- `family` (FAMILY_NONE / FAMILY_PARTIAL / FAMILY_NEWLYWED / legacy FAMILY_FULL)
- `setspouse` (string: favorite name)
- `gender_choice_pref`
- `species_preference_mode`
- `preferred_species_types`
- `preferred_species_anatomy`
- `polygamy_mode`
- `desired_relative_role`
- `allow_low_status_marriage`
- `allow_relatives_in_family`

`/mob/living/carbon/human` runtime mirrors (после spawn):

- `familytree_pref`
- `setspouse`
- `gender_choice_pref`
- `desired_relative_role`
- `allow_low_status_marriage`
- `allow_relatives_in_family`
- `family_datum` (`/datum/heritage`)
- `family_member_datum` (`/datum/family_member`)
- `spouse_mob` (legacy single pointer; предпочитать `family_member_datum.get_spouse_members()`)
- `familytree_assignment_scheduled`
- `familytree_confirmation_pending`
- `familytree_opted_out`

UI backend:

- `/client/proc/familytree_module_open_preferences()` — входная точка (`familytree_mob_procs.dm`).
- `/datum/family_options/ui_interact(...)` — открытие TGUI.
- `/datum/family_options/ui_data(user)` — сериализует prefs для TGUI.
- `/datum/family_options/ui_act("save", params)` — сохраняет через `familytree_module_save_character()` и обновляет UIs.
- `familytree_module_load_character(prefs, savefile)` — savefile → prefs.
- `familytree_module_save_character(prefs, savefile)` — prefs → savefile.
- `familytree_module_sanitize_character(prefs)` — clamps / collapses режимов, включая FAMILY_FULL → FAMILY_PARTIAL.
- `familytree_sanitize_pref(value)` — нормализатор одного family-значения.
- `load_familytree_runtime_preferences(H)` — prefs → H runtime mirrors.

UI string mapping (`_family_to_ui` / `_ui_to_family`, `familytree_prefs_ui.dm:393-411`):

- `"none"` ↔ `FAMILY_NONE`
- `"member"` ↔ `FAMILY_PARTIAL`
- `"couple"` ↔ `FAMILY_NEWLYWED`
- `"parent"` → `FAMILY_PARTIAL` (**legacy compatibility, всё ещё присутствует**; нормализуется в `"member"` при save)

Важно:

- Savefile хранит `FAMILY_*` compatibility значения. Runtime matching работает на `FAMILYTREE_MODE_*` масках. Не путать.
- Не добавлять act polling / update loops в TGUI: `ui_act("save")` уже делает save + `update_uis()`.

## Display Flow

- `/datum/heritage/ListFamily()` — текстовое представление.
- `/datum/familytree_display_panel` — backend TGUI панели просмотра.
- `BuildFamilyDisplayEntry(member, checker_member)` — один узел для отображения.
- `AddFamilyDisplaySections(...)` — группировка (nuclear / extended / spouses / former).
- `BuildFamilyTree(checker_member)` — полный family tree через граф (heritage proc).
- `BuildFamilyTreeRoots(checker_member)` — корни дерева.
- `SSfamilytree.get_display_tree_for(family, checker_member)` — cached display tree per viewer.
- `SSfamilytree.get_cached_relation(looker, lookee)` — cached relation matrix.

Рендер в TGUI: `FamilyDisplayPanel.tsx` + `FamilyDisplayPanel/FamilyTree.tsx` + `FamilyTreeBranch.tsx` + `FamilyTreeCard.tsx` + `FamilyListSections.tsx` + `types.ts`. Layout: простой node/edge, fit-to-viewport, pan/zoom, `ResizeObserver`-refit.

Loop avoidance (обязательно при любой правке display):

- visited lists при обходе.
- Depth guard.
- Graph validation (`family_graph_cache` dirty flags).
- Cached relation lookup вместо повторной прогонки графа.

## Species And Child Assignment

`SpeciesCalculation()` покрывает: same species, tieberian, northern human, elf/halfelf, orc/halforc. `SingleParentSpeciesCalculation()` — для одного родителя.

`DetermineAppropriateRole()` должен выбирать `"child"` только если хотя бы один совместимый родитель доступен через `SingleParentSpeciesCalculation()`. Форсированное child-назначение всё ещё может создать adoption, если species-пара несовместима.

## Social Status

Центральные фильтры:

```text
familytree_estates_compatible(A, B)
familytree_get_role_tier(H)
familytree_role_tiers_compatible(A, B)
familytree_polygamy_compatible(A, B)
familytree_lore_allows_polygyny(H)
familytree_lore_allows_polyandry(H)
```

Low tier сейчас включает wretch, bandit, assassin, lunatic, vagabond, bathworker, плюс fallback по title (Beggar, Excommunicado, Thug, Doomsayer). Tooltip чекбокса в `FamilySettingsPanel.tsx` должен описывать это на языке игрока.

## Wedding Ring

Family-created marriage выдаёт `/obj/item/clothing/ring/band`, имя `silver wedding ring`.

`give_wedding_ring()` кладёт кольцо в `H.mind.special_items["Silver wedding ring"]`, не в `SLOT_RING`. Только no-mind fallback может заспавнить его на turf.

## Manual Mutation Flows

Ручные/ритуальные мутации обходят часть автоматического matching, но ОБЯЗАНЫ оставлять graph / heritage / family_member consistent.

Файлы и procs:

- `familytree_holy_verbs.dm`:
  - `familytree_establish_bond()` — священник связывает двух персонажей (marriage/adoption/sibling).
  - `familytree_dissolve_marriage()` — расторжение брака.
- `familytree_rituals.dm`:
  - `familytree_ritual_adopt()` — adoption ритуал.
  - `familytree_vampire_bind()` — vampire sire bond.
- `familytree_debug_populate.dm` (admin):
  - `ftpop_add_parent()`, `ftpop_add_child()`, `ftpop_add_sibling()`, `ftpop_add_spouse()`, `ftpop_clear_user_house()`.

Если меняешь `AddParent` / `AddSpouse` / `AddToFamily` / `RemoveFamilyMember`, обязательно проверь эти manual flows — самые вероятные места забытой синхронизации.

## Debug Tooling

- `familytree_debug.dm` — сценарии (random / lifecycle / royal / favorite / roles / isolated / edge / stress).
- `familytree_debug_populate.dm` — панель "populate my house".

Это admin/debug tooling. **Не считать это runtime flow.** Не запускать без явного запроса пользователя (они спавнят мобов и мутируют state SS).

Полезны для:

- scenario testing
- edge cases
- royal testing
- desired role testing
- isolated species testing
- stress testing
- graph compare/debug

## Gotchas

- Saved `FAMILY_*` — compatibility layer. Runtime matching использует `FAMILYTREE_MODE_*` маски.
- `FAMILY_NEWLYWED = 4`, `FAMILY_FULL = 3`. Не считать, что порядок enum значит что-то про поведение.
- `familytree_sanitize_pref()` может схлопнуть режимы обратно в saved compatibility значения (FAMILY_FULL → FAMILY_PARTIAL, некорректные → FAMILY_NONE).
- Граф — source of truth для нормальных parent/spouse edge. Phantom parent/child остаются как direct lists на `family_member`.
- `AddParent` / `AddSpouse` ДОЛЖНЫ дёргать graph hooks; не дублировать direct relation storage.
- Всегда вызывать `mark_family_dirty()` при мутации графа.
- Не добавлять act polling / update loops в TGUI. `ui_act("save")` делает save + `update_uis()`.
- Assignment — signal/timer driven. Не делать рекурсивного immediate-assignment.
- Некоторые matching пути phase-gated: `FAMILYTREE_JOIN_CREATE_DELAY` и `FAMILYTREE_RELATIVE_JOIN_DELAY`.
- Xylix roulette намеренно обходит restrictions — не "чинить" это случайно.
- Royal suitor / royal partner jobs могут обойти normal local assignment.
- `desired_relative_role` в FAMILY_NEWLYWED НЕ надо сбрасывать — это валидная роль создателя нового дома.
- `setspouse` — player-directed, может обойти broad matching. Держать confirmation перед мутацией.
- `ruling_family` отдельно от `families`; нормальные family scans могут не захватить royal, если явно не проверяют `ruling_family`.
- `spouse_mob` — legacy single pointer. Для полного списка супругов — `family_member_datum.get_spouse_members()`.
- `RemoveSpouse()` чистит legacy pointers только для удалённой пары. Проверять callers при расторжении брака.
- Новые нормальные дома должны регистрироваться через `SSfamilytree.register_family()`.
- Debug populate может создать искусственные layout связей — не путать с player-facing flow.
- Если добавлен новый `#define` в `familytree_module_config.dm` — обязательно `#undef` в `familytree_module_deinclude.dm`.
- Если добавлен новый pref — обновить: `/datum/preferences` vars, runtime mirror (если нужен после spawn), reset/sanitize/load/save, `ui_data`/`ui_act`, FamilySettingsPanel.tsx, `load_familytree_runtime_preferences`, смежные matching/royal/helper уровни, этот файл.

## Common Recipes

Короткие пошаговые рецепты. Для полной impact-карты — Subsystem Development Protocol ниже.

### Add a new family preference

1. Добавить var в `/datum/preferences`.
2. Добавить runtime mirror в `/mob/living/carbon/human`, если pref нужен после spawn.
3. Обновить reset / sanitize / load / save в `familytree_prefs_ui.dm`.
4. Обновить `/datum/family_options/ui_data()`.
5. Обновить `/datum/family_options/ui_act("save")`.
6. Обновить `FamilySettingsPanel.tsx` (и `.scss` если нужно).
7. Обновить `load_familytree_runtime_preferences()` в `familytree_subsystem_core.dm`.
8. Обновить matching / royal / helper, если pref влияет на назначение.
9. Обновить этот файл (состав prefs + TL;DR если заметно).

### Add a new relation type

1. Решить: graph edge, derived relation, или phantom-only.
2. Обновить `familytree_member.dm` relation helpers / terms (`GetRelationshipTo`, relation labels).
3. Обновить graph API, если stored edge (добавить `relation_type` значение, проверить hooks).
4. Обновить display tree / sections, если отношение видимое (`AddFamilyDisplaySections`, FamilyDisplayPanel).
5. Обновить matching / manual flows, если assignable.
6. Обновить debug_populate, если применимо.

### Change spouse matching

Открыть: `familytree_subsystem_matching.dm`, `familytree_social.dm`, `familytree_subsystem_helpers.dm`, `familytree_lifecycle.dm` (confirmations), `familytree_holy_verbs.dm` (manual marriage).

### Change family display

Открыть: `familytree_heritage_core.dm`, `familytree_graph_api.dm`, `familytree_prefs_ui.dm`, `FamilyDisplayPanel/*.tsx`.

### Change royal partner behavior

Открыть: `familytree_subsystem_royal.dm`, `familytree_subsystem_helpers.dm`, `familytree_prefs_ui.dm`, `FamilySettingsPanel.tsx`.

### Change species filters

Открыть: `familytree_prefs_ui.dm`, `familytree_subsystem_helpers.dm`, `familytree_subsystem_royal.dm`, `familytree_heritage_core.dm` (SpeciesCalculation).

## Fast Search Commands

```bash
rg "SUBSYSTEM_DEF\(familytree\)"
rg "try_queue_assignment|run_local_assignment|AddLocal"
rg "familytree_module_load_character|familytree_module_save_character|familytree_module_sanitize_character"
rg "FamilySettingsPanel|FamilyDisplayPanel"
rg "ui_data|ui_act|ui_interact" modular_twilight_axis/familytree_module tgui/packages/tgui/interfaces
rg "AddPersonToHouse|AssignToHouse|AssignToFamily"
rg "FindNewlyWedMatch|FindFamilyMatch|TryAssignToFavorite|FindFavoriteMob"
rg "desired_relative_role|RELATIVE_"
rg "setspouse|favoriteName"
rg "polygamy|POLYGAMY_"
rg "allow_low_status_marriage|allow_relatives_in_family"
rg "SpeciesCompatible|GetSpeciesCompatibilityFailureReason|AnatomyCompatible"
rg "family_node|family_edge|family_graph_cache"
rg "graph_on_parent_added|graph_on_spouse_added|mark_family_dirty"
rg "GetRelationshipTo|BuildFamilyTree|ListFamily"
rg "AddRoyal|GenerateRoyalLineage|refresh_royal_partner_jobs"
rg "familytree_establish_bond|familytree_dissolve_marriage"
rg "ftpop_add_|familytree_debug"
rg "do_assign_desired_role|pick_least_filled_house"
rg "silver wedding ring|/obj/item/clothing/ring/band|special_items"
```

Дополнительные поисковые цепочки (PowerShell):

```powershell
rg -n "SSfamilytree|family_datum|family_member_datum|familytree_pref|spouse_mob" modular_twilight_axis/familytree_module
rg -n "FAMILY_NEWLYWED|FAMILY_PARTIAL|desired_relative_role|setspouse" modular_twilight_axis/familytree_module
rg -n "royal hand|FAMILY_OMMER|CreateBranchFamily|GetCurrentMonarch|run_royal_hand" modular_twilight_axis/familytree_module
```

# Subsystem Development Protocol / Правила разработки семейной подсистемы

Семейная подсистема стала большой и связанной. Нельзя менять только один файл "по месту", если фича затрагивает prefs, matching, graph, display, royal flow, TGUI, debug или manual rituals. Этот раздел описывает процесс разработки, чтобы будущий ИИ-агент всегда проверял смежные слои и не создавал баги из-за точечных изменений. Этот раздел ДОПОЛНЯЕТ, а не дублирует Common Recipes: рецепты — как сделать X, Protocol — что проверить независимо от X.

## 1. No isolated edits by default

Запрещён подход: "я нашёл один proc и поменял только его".

Перед правкой агент обязан определить impact area. 12 областей:

1. Preference / character setup
2. Runtime human vars
3. Matching / assignment
4. Graph relations
5. Heritage / house container
6. Display / TGUI tree
7. Royal family flow
8. Social rules / estates / polygamy
9. Manual mutation flows
10. Debug / admin tools
11. Config / include / deinclude
12. Save / load compatibility

Если изменение касается хотя бы одной области — проверить все соседние из impact map ниже.

## 2. Impact Map

### Меняешь preferences

Проверить:

- `familytree_prefs_ui.dm`
- `/datum/preferences` vars
- `/mob/living/carbon/human` runtime mirror vars
- `familytree_module_load_character()`
- `familytree_module_save_character()`
- `familytree_module_sanitize_character()`
- `/datum/family_options/ui_data()`
- `/datum/family_options/ui_act("save")`
- `FamilySettingsPanel.tsx` (и `.scss` при необходимости)
- `load_familytree_runtime_preferences()`
- matching код, если pref влияет на assignment
- royal код, если pref влияет на royal partners
- `familytree_module_config.dm` константы / комментарии
- AI_NAVIGATION.md (этот файл)

### Меняешь matching

Проверить:

- `familytree_subsystem_core.dm`
- `familytree_subsystem_matching.dm`
- `familytree_subsystem_helpers.dm`
- `familytree_social.dm`
- `familytree_subsystem_royal.dm`
- `familytree_lifecycle.dm` (confirmation / session)
- `familytree_debug.dm` (сценарии)
- `familytree_debug_populate.dm` (ручные связи)
- prefs / TGUI, если matching читает player settings

### Меняешь relation graph

Проверить:

- `familytree_graph_support.dm`
- `familytree_graph_api.dm`
- `familytree_member.dm`
- `familytree_heritage_core.dm` (display / build tree)
- manual mutation flows (`familytree_holy_verbs.dm`, `familytree_rituals.dm`, `familytree_debug_populate.dm`)
- cache dirty / validation paths
- `GetRelationshipTo()`
- `BuildFamilyTree()`
- `ListFamily()`
- display cache invalidation (`mark_family_dirty`)

### Меняешь /datum/family_member

Проверить:

- graph API wrappers
- phantom parent / child logic
- relation terms
- generation recalculation
- display tree generation
- debug_populate
- manual marriage / adoption / sibling flows

### Меняешь /datum/heritage

Проверить:

- `AddToFamily()`
- `RemoveFamilyMember()` / `RemovePersonFromFamily()`
- `CreateFamilyMember()`
- `MarryMembers()`
- `ListFamily()`
- `BuildFamilyTree()`, `BuildFamilyTreeRoots()`, `BuildFamilyDisplayEntry()`
- family-house creation в matching
- royal house / branch creation
- debug house population

### Меняешь display / TGUI

Проверить:

- `familytree_prefs_ui.dm`
- `familytree_heritage_core.dm`
- `familytree_graph_api.dm` cached display tree
- `FamilyDisplayPanel.tsx` + `FamilyDisplayPanel/*.tsx`
- `FamilySettingsPanel.tsx`, если настройки задействованы
- `ui_data` keys и frontend prop names
- избегать act polling / update loops

### Меняешь royal flow

Проверить:

- `familytree_subsystem_royal.dm`
- `familytree_subsystem_core.dm` (routing)
- `familytree_subsystem_helpers.dm` (job / species / gender)
- `familytree_social.dm` (estate / role tier)
- `familytree_lifecycle.dm` (noble / enigma / lineage)
- prefs compatibility для monarch preferences
- debug royal scenarios

### Меняешь social rules / polygamy / estates

Проверить:

- `familytree_social.dm`
- matching spouse logic
- royal spouse / partner logic
- prefs UI, если exposed player
- manual marriage validation
- debug_populate spouse creation

### Меняешь manual family mutation

Проверить:

- `familytree_holy_verbs.dm`
- `familytree_rituals.dm`
- `familytree_debug_populate.dm`
- graph dirty / cache invalidation
- `family_member` wrappers
- heritage membership consistency
- display tree after mutation

### Добавляешь новый файл / модуль

Проверить:

- `familytree_module_config.dm` include order
- `familytree_module_deinclude.dm`, если добавлены макросы
- AI_NAVIGATION.md file map
- compile order dependencies (файл до / после graph / matching / royal / debug)

## 3. Required development workflow

### Before coding

1. Определи тип запрошенного изменения.
2. По impact map составь список затронутых файлов.
3. Открой все затронутые файлы ДО правки.
4. Найди текущий source of truth:
   - saved prefs?
   - runtime vars?
   - graph edge?
   - family_member wrapper?
   - heritage house?
   - TGUI data key?
5. Определи тип изменения:
   - config-only
   - UI-only
   - runtime behavior
   - graph / data-model
   - compatibility / savefile
6. Напиши короткий edit-plan.
7. Только потом патчи код.

### After coding

1. Пересмотри все затронутые flow.
2. Поищи старые имена / константы (`rg`).
3. Проверь save / load compatibility.
4. Проверь TGUI data key compatibility.
5. Проверь graph dirty / cache invalidation.
6. Проверь manual / admin / debug paths.
7. Обнови AI_NAVIGATION.md, если архитектура изменилась.
8. Отчёт: список затронутых файлов + явно написать, менялось ли runtime поведение.

## 4. Cross-layer checklist

Перед финальным ответом агент должен ответить:

- Я обновил каждый слой, который потребляет эту value/proc?
- Есть ли saved-preference версия и runtime-mirror версия?
- Эта связь хранится в графе, выведена из графа, или phantom-only?
- Display tree всё ещё работает?
- Royal flow нужна та же правка?
- Manual holy / ritual / debug tools нужна та же правка?
- TGUI ждёт старые data keys?
- Нужно ли пометить кэш dirty?
- Deinclude нужен новый undef?
- Я обновил навигацию, если архитектура изменилась?

## 5. Change recipes

Любая новая фича подсистемы, которая создаёт новое понятие, пересекающее более одного файла, должна получить мини-рецепт в этом файле (AI_NAVIGATION.md).

Примеры понятий:

- новый preference
- новый relation type
- новая family role
- новая royal role
- новая social restriction
- новый graph edge
- новая display section
- новый manual ritual action

Формат:

```text
### Feature: <name>
Source of truth:
Affected files:
Runtime flow:
Save/load impact:
TGUI impact:
Graph/cache impact:
Manual/debug impact:
Gotchas:
```

## 6. Strong rule for this subsystem

Для `familytree_module` "рабочий код в одном файле" — НЕ достаточно.

Правильный change корректен только если согласованы все связанные слои:

- config константы
- saved prefs
- runtime vars
- matching logic
- graph model
- heritage membership
- display output
- TGUI keys
- manual mutation tools
- debug / admin tooling
- navigation docs

Если агент не может проверить соседний слой — он ДОЛЖЕН написать про эту неопределённость в финальном отчёте, а не выдавать задачу за выполненную.

Почти каждая новая настройка, роль, связь или правило имеет минимум 3–6 потребителей. Всегда делай dependency / impact pass по этому файлу перед патчем. Иначе задача считается выполненной неполно.
