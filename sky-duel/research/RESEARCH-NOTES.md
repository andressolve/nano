# Sky Duel — Research Archive

Verified 2026-06-09 via web sources. Every date/number used in the script must trace to a line here.

## Sidewinder origin (China Lake)

- Development began **1946–47** at the Naval Ordnance Test Station (NOTS), China Lake, Mojave Desert, California.
- **William B. McLean** led it as an unofficial side project — "Local Fuze Project 602" — using laboratory discretionary funding and volunteer after-hours help. No official program money until **1951**, when it was mature enough to show Admiral William "Deak" Parsons (Deputy Chief, Bureau of Ordnance).
- Core idea: mate a lead-sulfide proximity-fuze sensor (sensitive to infrared) with a guidance system that homes on the IR source.
- **1950**: McLean names it "Sidewinder" after *Crotalus cerastes*, the desert rattlesnake that hunts warm-blooded prey by sensing infrared with heat-sensitive pits.
- **Sept 3, 1952**: first live firing. **Sept 11, 1953**: first successful air-to-air drone interception. **1955**: production authorized. **1956**: operational with US Navy.
- First combat use: **Sept 24, 1958**, Second Taiwan Strait Crisis — Taiwanese F-86 Sabres with AIM-9Bs downed Communist Chinese MiGs; world's first air-to-air missile kills. (Sources disagree MiG-15 vs MiG-17 — script says "MiG fighters", no number.)
- Sources: Wikipedia AIM-9 Sidewinder; ethw.org William B. McLean; aao9.com Sidewinder History; Westrum, *Sidewinder: Creative Missile Development at China Lake*.

## How the IR seeker works

- Detector: **lead sulfide (PbS)** cell — generates signal from infrared (heat) radiation.
- **Spinning reticle**: a patterned spinning disk chops the incoming IR; the chopping pattern tells the electronics *where* in the field of view the hot spot sits.
- **Gimbal**: seeker head swivels to keep looking at the target as both aircraft maneuver.
- Later versions cool the detector (nitrogen/argon) → far more sensitive → can track skin friction heat, not just exhaust.
- **Rollerons**: small slipstream-spun wheels at the tips of the tail fins; act as air-driven gyroscopes resisting roll — stabilization with zero electronics. (Patented; signature Sidewinder trick.)

## Proportional navigation

- Missile does NOT fly at where the target *is* (tail-chase / pure pursuit) — it keeps the *bearing angle* to the target constant, like a quarterback leading a receiver.
- Sailor's rule: if another ship stays on the same compass bearing and gets closer, you are on a collision course. PN engineers that collision on purpose.

## AIM-9 versions / specs

- AIM-9B (first production): uncooled seeker, rear-aspect only (had to chase the tailpipe), ~4° field of view, could be fooled by the sun, clouds, hot ground.
- Vietnam (1965–73): 454 Sidewinders fired, ~18% kills vs 65% predicted. Real maneuvering targets ≠ test drones.
- **AIM-9L (1977)**: first all-aspect (cooled seeker; attack from any angle). Falklands 1982: Sea Harriers fired 24, ~88% hit rate.
- **AIM-9X (2003)**: imaging IR seeker — **128×128 focal-plane array** (a thermal camera that sees a *picture* of the jet), processor separates target shape from flares (IRCCM); **thrust vectoring** (steerable rocket nozzle, extreme agility); **JHMCS helmet cueing** — pilot locks by looking; ~90° off-boresight; lock-on after launch via datalink.
- Specs (AIM-9): length ~3.0 m (9 ft 11 in), diameter 5 in (127 mm), weight 188 lb (85.3 kg), speed Mach 2.5+, warhead 20.8 lb annular blast-frag, solid-fuel rocket.
- Fun: **Feb 4, 2023** — F-22 used an AIM-9X to down the Chinese spy balloon off South Carolina.

## Flares & the IR arms race

- Flares: magnesium-based pyrotechnics burning **as hot or hotter than engine exhaust**, ~5–10 s of intense IR. Old seekers chase the brightest heat → missile follows the flare.
- Counter-counter: modern seekers tuned to the *spectrum* of a jet engine (CCM); modern flares tuned to mimic that spectrum; imaging seekers (AIM-9X) recognize the *shape* and trajectory of the aircraft and reject point-source flares.
- Source: Wikipedia Flare (countermeasure); GlobalSecurity flares page; EMSOPEDIA.

## M61 Vulcan gun

- GE, **Project Vulcan, 1946**; in service **1959**; principal US fighter cannon since.
- Six rotating 20 mm barrels, Gatling principle revived with external (hydraulic/electric) drive; each barrel fires once per revolution.
- **6,000 rounds/min ≈ 100 rounds/sec.** Six barrels share the heat and wear — one barrel firing that fast would overheat/erode.
- Very reliable: >10,000 rounds mean time between jams.
- Why a gun still matters: missiles have minimum ranges; the gun is the always-loaded close-in weapon. But effective only at short range vs maneuvering jet.

## AIM-120 AMRAAM (radar missile)

- Beyond-visual-range: ~50–70 km class. All-weather, day/night.
- Three guidance phases: (1) **inertial** navigation toward predicted point, (2) **datalink mid-course updates** from launch jet's radar, (3) terminal **active radar homing** — missile's own radar switches on and it guides itself. "Fire and forget."
- Contrast with older Sparrow: launcher had to keep illuminating target with its radar the whole way.

## Radar counters & stealth

- **RWR** (radar warning receiver): listens for enemy radar energy, warns pilot of search/lock/launch — the jet's spider-sense.
- **Chaff**: clouds of tiny metallic strips that bloom into a false radar target.
- **Stealth**: shape the aircraft so radar energy bounces *away* from the sender + radar-absorbing materials. F-22 frontal RCS ≈ 0.0001–0.0002 m² — roughly a **marble-sized** metal sphere on radar. F-35 ≈ golf-ball class.
- Stealth jets carry weapons in **internal bays** (F-22: bays; F-35: 2 internal stations + external pylons when stealth not needed) because hanging missiles outside reflects radar.
- **F-16: 9 hardpoints** (wingtip rails + underwing + centerline), max external load ~17,000 lb.

## Source links

- https://en.wikipedia.org/wiki/AIM-9_Sidewinder
- https://en.wikipedia.org/wiki/William_B._McLean
- https://ethw.org/William_B._McLean
- https://www.aao9.com/sidewinder-history.html
- https://www.smithsonianmag.com/air-space-magazine/sidewinder-57687913/
- https://en.wikipedia.org/wiki/Flare_(countermeasure)
- https://www.globalsecurity.org/military/systems/aircraft/systems/flares.htm
- https://en.wikipedia.org/wiki/M61_Vulcan
- https://www.nationalmuseum.af.mil/Visit/Museum-Exhibits/Fact-Sheets/Display/Article/579640/m61a1-vulcan-cannon/
- https://en.wikipedia.org/wiki/AIM-120_AMRAAM
- https://designation-systems.net/dusrm/m-120.html
- https://www.globalsecurity.org/military/world/stealth-aircraft-rcs.htm
- https://en.wikipedia.org/wiki/Hardpoint
