# RESEARCH NOTES · "The Iron Triangle" (tank explainer)

Every number/claim in the script must trace to a line here. Sourced 2026-06-22.
Where sources disagree or a value is a round generalization, the script hedges ("about", "roughly").

## The iron triangle (organizing idea)
- A tank balances three competing demands: **firepower, protection, mobility**. Adding more of one
  usually costs the others (more armor → heavier → slower; bigger gun → heavier turret). Every tank
  is a compromise among the three. (Widely-stated armor-design framing; "iron/eternal triangle of tank design".)

## The gun
- Modern MBTs use a large **smoothbore** main gun, commonly **120 mm** (NATO: Abrams, Leopard 2, Merkava)
  or 125 mm (Russian). Smoothbore (no rifling) suits fin-stabilized rounds and high muzzle velocity.
- The shell flies very flat and fast — engagements out to ~2–3 km; the round crosses that in a couple of seconds.

## Two ways to kill armor (P5)
- **APFSDS — kinetic "dart":** Armor-Piercing Fin-Stabilized Discarding-Sabot. A long, thin, dense
  rod (tungsten or depleted uranium) fired at very high speed; the outer "sabot" falls away after the
  muzzle. Defeats armor by concentrated kinetic energy — no explosive. ~7–10 MJ of energy for a 120 mm dart.
  Penetration depends on velocity, mass, and impact angle. Going through, it sprays hot fragments (spall) inside.
- **HEAT — shaped charge "jet":** High-Explosive Anti-Tank. On impact a shaped explosive collapses a metal
  cone into a hyper-fast jet of metal that bores through armor and sprays molten metal inside. Needs standoff
  distance to form. ~1 MJ for a 120 mm HEAT jet (less raw energy than the dart, but focused). This is the
  warhead on most rockets, missiles, and FPV drones — which is why it drives the armor arms race.

## Fire control (P6)
- Modern fire-control fuses: **gunner's sight + laser rangefinder + gun/sight stabilization + thermal
  night sight + ballistic computer + sensors** (wind, tilt, ammo type, barrel wear).
- Sequence: gunner lays the reticle on the target → laser measures exact range → computer solves the
  ballistic lead/drop and shifts the aim point → fire. Modern processors do **100+ ballistic updates/sec**.
- **Stabilization** keeps the gun pointed at the target while the hull bounces over rough ground, so the
  tank can **hit while moving**. Thermal sight lets it see and shoot in total darkness / smoke.

## Armor (P7)
- **Sloped armor:** angling the plate makes a shot travel through more steel for the same plate thickness,
  and helps deflect/ricochet rounds. More protection without more weight.
- **Composite (Chobham/Burlington):** layered "sandwich" of steel + ceramic + other materials. Especially
  good at disrupting the HEAT metal jet. Used on Abrams, Leopard 2, Challenger.
- **Spaced armor:** an outer plate held away from the main hull; makes a shaped-charge jet detonate early
  and spread out before it reaches the real armor.

## The arms race: reactive + active protection (P8)
- **ERA — Explosive Reactive Armor:** bricks of explosive sandwiched between metal plates, bolted on the
  outside. When a HEAT jet hits, the brick detonates outward, disrupting the jet. Can cut shaped-charge
  penetration by ~50–70%. (One-shot per brick.)
- **APS — Active Protection System (e.g., Trophy / "Windbreaker"):** small radar watches 360° around the
  tank, tracks an incoming rocket/missile, the computer predicts its path, and the system **fires an
  interceptor (a burst of slugs) to destroy the threat in the air before it hits.** Combat-proven. Being
  upgraded to also counter drones. (Directly echoes the counter-drone turret in the previous book.)

## Mobility (P9)
- Modern MBTs weigh **~60–70 tonnes**. Engine ~**1500 horsepower** (gas turbine on Abrams; diesel on
  Leopard 2 / Merkava / Leclerc). Road speed ~60–70 km/h.
- **Tracks spread the weight:** a 60-tonne machine on tracks has low **ground pressure** (roughly like a
  person's footstep per unit area), so it can cross mud, sand, and broken ground where a wheeled truck
  would sink. Tracks also grip to climb and pivot in place.

## The crew (P10)
- Classic crew of **four**: **commander** (decides, watches all around), **gunner** (aims & fires),
  **loader** (loads the next shell), **driver** (drives, lowest in the hull).
- **Autoloader** (French Leclerc; Russian T-72/T-80/T-90/T-14): a machine loads the gun, dropping the crew
  to **three**. Trade-off: fewer people, but a stored mechanism and (in some designs) ammo near the crew.
  No autoloader on Abrams/Leopard 2 — they keep the human loader.

## History — it's not new (P11)
- First tanks: British **Mark I**, debut **15 September 1916** at Flers-Courcelette, **Battle of the Somme**.
  Rhomboid shape, caterpillar tracks around the whole hull, ~28 tons, top speed ~4 mph.
- Built to cross WWI trenches (~8–9 ft wide) and barbed wire that stopped infantry. Of ~49 readied, ~32
  reached the start line, ~18 went into action — many broke down or ditched. Slow, unreliable, but proved
  the idea: a protected, armed, cross-country machine.

## Where it's going — drones vs. tanks (P14, ties to "The Gun That Aims Itself")
- Cheap **FPV drones (~$400–500)** now destroy tanks worth millions — the same cost-asymmetry from the
  turret book, now aimed AT the tank. The **thin turret-roof / top armor** is the weak spot (top-attack).
- By 2026 FPV drones are estimated the single largest category of armored-vehicle kills in Ukraine.
- Tank survival answer = **layers**: APS (e.g., Trophy upgraded vs. drones), jammers, cope cages/nets,
  and the counter-drone guns from the previous book. The tank isn't obsolete — it's growing a shield, the
  same shield this series already covered.

## Safety / framing
- Machines as subjects. No human casualties depicted. Crew shown operating/standing with the tank for scale.
- History (Somme) framed as the machine crossing trenches/wire, not on what it killed.

## Sources (web, 2026-06-22)
- GlobalSecurity 120 mm ammunition; Military Wiki kinetic penetrator; inetres weapons effects (APFSDS vs HEAT energy).
- Sakhal / military-review fire control systems; GlobalSecurity M1 Abrams (laser rangefinder, ballistic computer, 100+ updates/s).
- Wikipedia Composite armour / Chobham armour; defensefeeds ERA; Wikipedia Trophy (countermeasure); National Defense Magazine (Trophy vs drones).
- Wikipedia Main battle tank; GlobalSecurity M1 Abrams specs (60 tons, 1500 hp, crew 4); Wikipedia continuous track (ground pressure).
- Tank Museum Mark I; History.com (Somme, 15 Sep 1916); Wikipedia Tanks in WWI.
- Military Machine / TS2 / Ukraine War Analytics (FPV cost asymmetry, top-attack, 2024–2026 kill share).
