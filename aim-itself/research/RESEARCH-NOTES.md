# RESEARCH NOTES — "The Gun That Aims Itself"

Every number used in the script must trace to a fact below. Deliberate simplifications/departures
are logged at the bottom. Researched 2026-06-22.

---

## The threat: cheap attack drones

**FPV (first-person-view) attack drones**
- Cost: as little as **~$300–500** per unit. A ~$300–500 drone can destroy an armored vehicle worth
  **$3 million or more** — the core asymmetry of the whole book.
- Payload: a typical small FPV carries **~2 kg**, often a repurposed anti-tank grenade (RPG-7 / RKG-3 warhead).
- Speed: small FPVs are short-range; mid-range variants reach **~140 km/h** with **~50 km** range, ~60 min flight.
- Scale: Ukraine is reportedly expending **up to ~10,000 drones per month** — a rate only cheap drones make possible.
- **Fiber-optic FPV drones** trail a thin spool of optical fiber instead of using radio — so they **cannot be jammed**.
  This is the turning point that makes a *gun* (hard kill) matter again. (src: ts2.tech, RF Wireless World)

**Shahed-136 / Geran-2 (the bigger "loitering munition")**
- ~**3.5 m** long, **2.5 m** wingspan, ~**200 kg**, pusher propeller, cruise **~185 km/h**.
- Warhead ~**30–50 kg** (Russian Geran-2 variants up to ~90 kg).
- Range estimates **1,000–2,500 km**. Often used point-to-point like a cheap cruise missile rather than truly "loitering."
- These are the slow, droning, mass-launched threat the Ukrainian turrets are scored against.

## The hero: autonomous / semi-autonomous counter-drone turrets

**Sky Sentinel (Ukraine)** — reportedly the first autonomous air-defense turret in active combat in Europe.
- A standard **heavy machine gun** on a robotic mount, fed by **radar + electro-optical sensors + AI targeting**.
- Rotates **360°**, automatically detects, identifies, and calculates firing solutions in real time.
- In early combat testing **reportedly destroyed six Shahed-136 drones**. (src: National Interest, Medium/Marinero)

**Dron ZP turret (Ukraine)** — unveiled **12 January 2025**.
- **12.7 mm machine gun** + night-vision device, **neural-network**-assisted, **semi-autonomous** control. (src: Army Recognition)

**Context:** UK announced (Nov 2025) delivery of **20+ remotely-guided counter-drone turrets** (sourced from Estonia)
to Ukraine as part of a **£600 M** air-defense package; newest automated turrets joined Kyiv Oblast's layered
defense on **2 June 2026**. (src: Euromaidan Press)

## "This isn't brand new" — the history page

**Phalanx CIWS (US Navy)** — autonomous ship-defense gun in service since **1980** (USS Coral Sea; approved for
production 1978).
- **20 mm M61 Vulcan** rotary (Gatling) cannon + **Ku-band fire-control radar**, fully self-contained: it can
  **search, detect, track, engage, and confirm kills on its own** — it can be "turned loose" to fire autonomously.
- Rate of fire: **3,000 rpm** (Block 1) up to **4,500 rpm** (Block 1A+). (src: Wikipedia, NavWeaps)
- The point for kids: a gun that aims and fires itself is **40+ years old** — drones just made it matter on land.

**SGR-A1 (South Korea, DMZ sentry gun)** — Samsung Techwin (now Hanwha) + Korea University.
- Prototypes **2006**, reportedly deployed to the DMZ from ~**2010**.
- **Uncooled IR thermographic camera** + IR illuminator + laser rangefinder. Target ID **up to 4 km day / 2 km night**;
  effective range **~3.2 km**. ~**$200,000** per unit.
- Autonomy **disputed**: a 2008 study called it fully autonomous; Samsung says it keeps a human in the decision. (src: Wikipedia)

## How it sees (the sensing stack)

- **Radar** — bounces radio waves, detects a small fast-moving return; works in darkness/weather but small plastic drones have a tiny radar signature.
- **Electro-optical (daylight cameras)** — high-zoom visual ID.
- **Infrared / thermal** — sees the heat of motor/battery; works at night.
- **Acoustic** — microphones that recognize the **buzz** of propellers; cheap, short-range, good for tiny drones radar misses.
- **Sensor fusion** — combine them, because none alone is reliable against a small low-slow drone.
- **Recognition** — a neural network / computer vision tells a **drone from a bird from a passenger plane**; this is the "AI" part.

## The other ways to stop a drone (the counter spectrum)

| Method | Type | How | Limit |
|---|---|---|---|
| **RF jamming** | soft kill | Blast noise on the drone's control band (2.4 / 5.8 GHz) or GPS (L1) so it loses its link | Useless vs. fiber-optic/autonomous drones; can jam friendly radios too |
| **GPS spoofing** | soft kill | Feed fake navigation signals so the drone flies the wrong way | Defeated by drones not relying on GPS |
| **Gun / kinetic** | hard kill | Shoot it down (turret, CIWS) | Needs precise aim & lead; ammo/airspace safety |
| **Interceptor drone/missile** | hard kill | Fly a drone or small missile into it (e.g., Coyote Block 2C ~**$100,000/shot**) | Expensive vs. a $400 target |
| **High-energy laser** | hard kill | Burn a hole in a critical part with a focused beam | Power, cost, line-of-sight, weather |
| **Net** | hard kill | Net-gun (handheld or drone-launched) tangles the props | Very short range |

The cost asymmetry is the throughline: a **few hundred dollars** of threat vs. expensive defenses → a **gun firing
cheap bullets** is one of the few cost-effective hard kills, which is exactly why the auto-turret is back.

## The kill chain (the assembled-system page)

**Detect → Identify → Track → (decide) → Fire**, compressed into **seconds**. Radar/acoustic detects, camera+AI
identifies drone-vs-bird, the computer predicts the lead point, fire-control lays the gun, it fires a burst.
(Note: most fielded systems keep a human pressing "engage" — "human in the loop" — though Phalanx and others
*can* run fully auto. We state this plainly without making it the book's theme.)

---

## DELIBERATE SIMPLIFICATIONS / DEPARTURES (logged)

1. **"~$500 drone vs. $3,000,000 vehicle"** — sources give FPV unit cost ~$300–500; using "a few hundred dollars"
   or "$500" as the round figure. The $3M+ vehicle figure is sourced (defence-blog). Honest order-of-magnitude.
2. **Sky Sentinel "six Shahed-136 destroyed"** — reported from early combat testing; script will hedge with
   "reportedly" / "in its first tests."
3. **"Nobody pulled the trigger" hook (P1)** — autonomous engagement is real (Phalanx "turned loose"; Sky Sentinel
   auto-calculates firing solutions), but many fielded turrets keep a human approving the shot. The hook is dramatized
   on a system running in auto-track/auto-fire; P12 states plainly that a human is often still in the loop. Not false,
   but it is the most dramatized line — logged.
4. **SGR-A1 autonomy** — disputed in the open literature; script says it *can* detect and aim on its own and that its
   full autonomy is debated, rather than asserting it fires unsupervised.
5. **Rate of fire / specs** rounded to the sourced figures (Phalanx 4,500 rpm; 12.7 mm Dron ZP; SGR-A1 ranges).
6. **No system named as a "kill people" weapon.** The book's targets are drones. SGR-A1 (an anti-personnel sentry
   gun) is framed strictly as the historical "gun that watches and aims by itself," not by what it shoots.

## SOURCES
- National Interest — Ukraine Sky Sentinel turret
- United24 Media / cuashub — Ukraine AI anti-drone turret (neural network)
- Euromaidan Press — automated turrets in Kyiv Oblast, UK/Estonia £600M package
- Army Recognition — Dron ZP semi-autonomous FPV turret (12.7mm, 12 Jan 2025)
- defence-blog.com — what Ukraine's drones really cost; Kyiv Independent — mid-range drone specs
- Wikipedia: Phalanx CIWS, HESA Shahed-136, SGR-A1; NavWeaps — Phalanx
- ts2.tech / RF Wireless World / robinradar — counter-drone method families, fiber-optic FPV limitation
