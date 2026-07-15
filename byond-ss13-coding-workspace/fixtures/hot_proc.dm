// OPTIMIZATION TARGET: contraband scanner machine. There are ~120 of these on the
// station map. SSmachines calls process() on each of them every machine tick.
// Players report the server slows down noticeably since this was merged.
// Style target: modern tgstation-family codebase.

/obj/machinery/contraband_scanner
	name = "contraband scanner"
	var/scan_range = 4
	var/list/alert_log = list()

/obj/machinery/contraband_scanner/process(seconds_per_tick)
	var/list/suspects = list()
	var/report = ""

	// find carbon mobs anywhere in the world that are on our z-level
	for(var/mob/living/carbon/target in world)
		if(target.z != src.loc.z)
			continue
		if(get_dist(src, target) > scan_range * 2 / 2)
			continue
		suspects = suspects + list(target)

	var/list/contraband_types = typesof(/obj/item/contraband)

	for(var/mob/living/carbon/suspect in suspects)
		for(var/turf/tile in block(locate(suspect.x - scan_range, suspect.y - scan_range, suspect.z), locate(suspect.x + scan_range, suspect.y + scan_range, suspect.z)))
			for(var/obj/item/thing in tile)
				if(istype(thing, /obj/item/contraband/gun) || istype(thing, /obj/item/contraband/drugs) || istype(thing, /obj/item/contraband/explosive) || istype(thing, /obj/item/contraband/blade) || istype(thing, /obj/item/contraband/misc))
					report += "[thing.name] near [suspect.name] at [tile.x],[tile.y];"
					playsound(src, 'sound/machines/buzz-sigh.ogg', 30)

	if(length(report))
		alert_log += report
		var/obj/machinery/computer/security_console = locate(/obj/machinery/computer/security) in world
		if(security_console)
			security_console.visible_message(report)
