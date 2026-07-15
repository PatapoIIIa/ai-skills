// PATCH UNDER REVIEW: adds a "bounty hunter" component that tracks a victim mob,
// periodically regenerates the hunter, and springs a trap when the victim dies.
// Style target: modern tgstation-family codebase.

GLOBAL_LIST_EMPTY(tracked_hunters)

/datum/component/bounty_hunter
	var/mob/living/hunter
	var/mob/living/last_victim
	var/regen_timer_id
	var/obj/structure/trap/trap
	var/health_regen = 4

/datum/component/bounty_hunter/Initialize(mob/living/victim)
	if(!isliving(parent))
		return COMPONENT_INCOMPATIBLE
	hunter = parent
	last_victim = victim
	GLOB.tracked_hunters += src
	RegisterSignal(victim, COMSIG_LIVING_DEATH, PROC_REF(on_victim_death))
	regen_timer_id = addtimer(CALLBACK(src, PROC_REF(regen_tick)), 5 SECONDS, TIMER_LOOP | TIMER_STOPPABLE)
	START_PROCESSING(SSobj, src)

/datum/component/bounty_hunter/proc/regen_tick()
	if(hunter.health < hunter.maxHealth)
		hunter.adjustBruteLoss(-health_regen)

/datum/component/bounty_hunter/process(seconds_per_tick)
	hunter.adjustStaminaLoss(-health_regen)

/datum/component/bounty_hunter/proc/on_victim_death(mob/living/source)
	SIGNAL_HANDLER
	playsound(hunter, 'sound/machines/chime.ogg', 50)
	sleep(2 SECONDS)
	spring_trap(source)

/datum/component/bounty_hunter/proc/spring_trap(mob/living/victim)
	trap = new(get_turf(victim))
	if(do_after(hunter, 3 SECONDS, target = victim))
		victim.forceMove(trap)
		to_chat(hunter, span_notice("Caught [victim]!"))

/datum/component/bounty_hunter/proc/clear_trap()
	if(trap)
		del(trap)

/datum/component/bounty_hunter/Destroy()
	STOP_PROCESSING(SSobj, src)
	hunter = null
