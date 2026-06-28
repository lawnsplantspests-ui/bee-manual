import json
gloss = json.load(open(r"C:\Users\leasy\bee-manual\glossary.json", encoding="utf-8"))
G = [{"t": e["term"], "a": e["alias"], "d": e["def"]} for e in gloss]

QUICKFACTS = [
 ["Bee space", "3/8 inch (9.5 mm). Smaller and bees fill it with propolis; larger and they build burr comb."],
 ["Winter cluster forms", "Below 64°F (18°C). Foraging and water collection stop."],
 ["Brood incubation temp", "91–97°F (33–36°C), maintained by heater bees."],
 ["Healthy brood pattern", "Solid 'rainbow': brood in center, arc of pollen, honey on top. 6–17% empty cells is normal."],
 ["Drones at peak", "About 5% of adult bees in late spring / early summer. Far more late summer = possible drone-laying queen."],
 ["Drone comb (natural)", "About 17–20% of comb — roughly 2 frames in a 10-frame box. Usually along bottom/sides, not the center."],
 ["NE swarm season", "Peaks mid-May to mid-July. Colony starts making drones at about 4,000 bees."],
 ["Queen mating", "1–3 mating flights, mates with an average of 12 drones (range 10–20). Mating flights and swarms are the only times she leaves."],
 ["Frame replacement", "Replace your 2 oldest frames per box each year. Never pull more than 4 frames from a hive at once."],
 ["Brood frames to inspect", "At least 4 frames of brood per box."],
 ["Honey moisture", "Capped at about 17–19% water. Above ~18% it can ferment."],
 ["Sugar syrup mixes", "1:1 (1 sugar : 1 water) to stimulate brood in spring; 2:1 (2 sugar : 1 water) to build winter stores in fall."],
 ["Pollen / bee bread", "1–2 frames per brood box is ideal for brood rearing."],
 ["Good resource flow", "10–20 bees per minute entering with full pollen baskets means lots is coming in."],
 ["AFB rope test", "Insert a toothpick into a suspect cell, twist, and pull. If it 'ropes' out 2 cm+, suspect American Foulbrood. Send samples to the Beltsville Bee Lab (free)."],
 ["Guanine crystals", "Small white crystals on the ceilings of brood cells = high Varroa mite levels."],
]

VARROA = [
 {"name":"Apiguard", "ai":"Thymol", "cls":"Essential oil", "method":"Tray with gel sits on brood frames", "eff":"74–95%", "cost":"$3.30–$6.80", "dur":"28 days (two 14-day applications)", "supers":"No — supers off", "wait":"Can super immediately after treatment ends", "temp":"Needs warmth — roughly 60–105°F to vaporize properly"},
 {"name":"Api Life Var", "ai":"Thymol, eucalyptus oil, menthol", "cls":"Essential oil", "method":"Tablets placed on the corners of the brood nest", "eff":"70–90%", "cost":"$4.48–$7.12", "dur":"21–30 days (3 applications, 7–10 days apart)", "supers":"No — supers off", "wait":"1 month after treatment ends", "temp":"Needs warmth — roughly 60–105°F"},
 {"name":"MiteAway Quick Strips (MAQS)", "ai":"Formic acid", "cls":"Organic acid", "method":"Pads placed on the brood nest", "eff":"61–98%", "cost":"$4.40–$7.25", "dur":"7 days", "supers":"Yes — can be left on during treatment", "wait":"Supers can stay on", "temp":"Moderate temps only — about 50–85°F (too hot can kill brood/queen)"},
 {"name":"Oxalic Acid", "ai":"Oxalic acid dihydrate", "cls":"Organic acid", "method":"Dribble on brood nest, or vaporize at entrance", "eff":"82–99%", "cost":"$0.25–$0.37", "dur":"10 minutes", "supers":"No — supers off", "wait":"2 weeks", "temp":"Best when brood is low/absent (late fall, broodless). Works in cool weather."},
 {"name":"HopGuard II", "ai":"Hops beta acids", "cls":"Organic acid", "method":"Strips inserted in the brood nest", "eff":"75–99%", "cost":"$3.33–$3.80", "dur":"28 days", "supers":"Yes — can be left on during treatment", "wait":"Supers can stay on", "temp":"Wide range"},
 {"name":"Apivar", "ai":"Amitraz", "cls":"Synthetic", "method":"Insert strips into the brood nest", "eff":"95%", "cost":"$5.00–$6.90", "dur":"42–56 days", "supers":"No — supers off", "wait":"2 weeks", "temp":"Wide range"},
]
VARROA_NOTE = "Apistan and CheckMite+ are NOT recommended — they stay in wax for years and mites have developed resistance. Rotate treatments, remove strips promptly, and follow IPM. Resistance to Apivar has also been seen. Always monitor mite levels after treating to confirm it worked. Efficacy figures: Honey Bee Health Coalition, Tools for Varroa Management, 5th ed."

INSPECT = [
 {"h":"Before you open", "items":[
   "Set your objective for this visit — why are you in the hive today?",
   "Tool kit ready: smoker lit, hive tool, notebook/phone, gear for what you plan to do.",
   "Weather OK? Calm, mild, ideally sunny mid-day when foragers are out.",
 ]},
 {"h":"Outside the hive (before opening)", "items":[
   "Predator signs: skunk scratch marks at the entrance or on the ground? Elevate the hive on a stand if so.",
   "Fecal matter: a little on the front is normal; heavy orange/brown streaks signal trouble (dysentery/disease).",
   "Guard bees: wave a hand slowly across the entrance. If a guard follows it, use smoke to break her attention.",
 ]},
 {"h":"Population status", "items":[
   "Population: enough adult bees for the season? Strong = bees nearly cover both sides of each brood frame.",
   "Queen status: worker eggs present? Signs of supersedure or swarm prep? Laying-worker signs (multiple eggs per cell)?",
   "Brood: solid or spotty? Enough for the time of year? All ages present — eggs, larvae, capped brood?",
   "Trend: does the population seem to be growing or shrinking for this time of year?",
   "Drones: seasonally appropriate amount? (~5% at peak. Lots of capped drone late summer = possible drone-layer.)",
 ]},
 {"h":"Nutrition", "items":[
   "Floral sources: what's blooming now? Any drought or long bad weather hurting forage?",
   "Foraging: enough bees flying? 10–20 bees/min entering with full pollen = good flow.",
   "Stores: how much pollen/bee bread and nectar/honey? Right amount for the season?",
   "Larval nutrition: young larvae floating in abundant white royal jelly? (Thin/no jelly = consider protein.)",
 ]},
 {"h":"Pests, parasites & disease", "items":[
   "Brood disease signs? Discolored, twisted, melted, cannibalized larvae, or punctured/perforated cappings.",
   "Adult bees: deformities or odd behavior? Visible Varroa, hive beetles, wax moths, or their larvae?",
   "Pests in the honey supers or elsewhere in the hive?",
   "Are the bees more defensive than usual?",
 ]},
 {"h":"In the brood nest", "items":[
   "Inspect at least 4 brood frames per box.",
   "Adults: look for hairlessness, greasiness, deformed wings, twitching.",
   "Brood health: hold frame with sun at your back, angled so light fills the cells. Look for a solid 'rainbow' pattern.",
   "Brood pattern & sex: eggs near center working outward; one egg per cell. Multiple eggs/cell = laying workers.",
   "Queen cups & cells: a few empty cups is normal. Many cups + eggs/larvae along the BOTTOM = swarm prep. A few near the CENTER = supersedure/emergency.",
   "Brood nutrition: 1–2 frames of pollen per box ideal; abundant royal jelly around larvae.",
   "Comb condition: replace 2 oldest frames per box per year — but never pull more than 4 frames at once.",
 ]},
 {"h":"Wrap up", "items":[
   "Return every frame in the same order and orientation so the brood nest stays intact.",
   "Decide management: more honey-storage room? Swarm prevention? Treatment?",
   "Note when to come back and anything to follow up on. Photograph anything unusual.",
 ]},
]

DISEASE = [
 {"name":"Varroa / Parasitic Mite Syndrome", "type":"Mite + virus complex", "look":"Spotty brood, perforated or chewed-down cappings, twisted larvae. White guanine crystals on cell ceilings. Deformed wings and K-wing on adults. Reddish-brown mites visible on bees or in drone brood.", "do":"Monitor with an alcohol wash / sugar roll. Treat per the Varroa page when over threshold. The #1 colony killer — stay ahead of it."},
 {"name":"American Foulbrood (AFB)", "type":"Bacteria (Paenibacillus larvae)", "look":"Sunken, greasy, perforated cappings. Brown, goopy pupae that ROPE OUT 2 cm or more on a toothpick. Hard black scale stuck to the cell that will NOT scrape off. Foul smell.", "do":"⚠️ Highly infectious and serious. Don't share equipment. Send samples to the Beltsville Bee Lab (free) and contact your state apiarist. Often requires burning infected equipment."},
 {"name":"European Foulbrood (EFB)", "type":"Bacteria (Melissococcus plutonius)", "look":"Twisted, melted-looking larvae that turn brown/yellow and die BEFORE capping. Goopy but ropes less than AFB (up to ~1.5 cm). Often a sour smell.", "do":"Often clears with a strong nectar flow, requeening, or comb rotation. Confirm vs AFB — when unsure, send a sample."},
 {"name":"Chalkbrood", "type":"Fungus (Ascosphaera apis)", "look":"Larvae turn into hard, chalky white (sometimes black/blue-spotted) 'mummies' that rattle in cells or show up on the bottom board / at the entrance. Larvae stand up in the cell; easily scraped out, doesn't rope.", "do":"Usually stress-related. Improve ventilation, requeen for hygienic stock, keep colonies strong."},
 {"name":"Sacbrood", "type":"Virus", "look":"Fluid-filled, sac-like larvae lying flat. Larvae turn brown and settle to the bottom of the cell, head often dark and curled ('canoe' / Chinese-slipper shape).", "do":"Usually self-limiting in a strong colony. Requeen if persistent."},
 {"name":"Nosema", "type":"Gut fungus (N. apis / N. ceranae)", "look":"Dysentery — brown streaks on/around the hive (N. apis especially). Crawling bees unable to fly, decreased adult population, dwindling.", "do":"Reduce stress, improve ventilation, replace old comb. Confirm by spore count if needed."},
 {"name":"Tracheal mite", "type":"Mite (Acarapis woodi)", "look":"K-wing (wings held at odd angles), crawling bees that can't fly, discolored tracheae under magnification.", "do":"Less common now. Grease patties and resistant stock help."},
 {"name":"Wax moth", "type":"Pest (Galleria / Achroia)", "look":"Silk webbing and tunnels through comb, especially in weak colonies or stored comb. Larvae burrow under cappings (bald-brood trails).", "do":"A symptom of a weak colony — strengthen or combine. Protect stored comb (freeze frames, store cool & airy)."},
 {"name":"Small hive beetle", "type":"Pest (Aethina tumida)", "look":"Small fast black beetles running on frames; slimy, fermented 'sliming' of comb; larvae in the honey.", "do":"Keep colonies strong, reduce open space, use beetle traps. Worse in warm, humid conditions."},
 {"name":"Deformed Wing Virus (DWV)", "type":"Virus (Varroa-vectored)", "look":"Adults emerge with crumpled, stubby, useless wings; bloated abdomens; shortened lifespan.", "do":"A red flag for high Varroa. Get mites under control — DWV rides with them."},
]

LIBRARY = [
 {"mod":"Quick Reference (field)", "files":["Hive Inspection Guide","Varroa Treatment Guide","Disease & Pest Symptom Chart","Beekeeping Calendar for the Northeast","Treatment Hierarchy diagram","Full Glossary (1–4)"]},
 {"mod":"1 · Evolution, Biology & Behavior", "files":["Course transcript","Bee anatomy","Egg/development timeline","Kin selection","Worker polyethism","Glossary","Module quizzes"]},
 {"mod":"2 · The Science & Art of Beekeeping", "files":["Course transcript","Bee subspecies & stock traits","Queen-rearing schedule (Doolittle)","Amino acids / pollen resources","Record sheets (apiary, hive, Varroa)","Module quizzes"]},
 {"mod":"3 · Managing Pests & Diseases", "files":["Course transcript","Glossary","Varroa / Nosema / virus / brood-disease quizzes","Bee health: the big picture"]},
 {"mod":"4 · Rewards & Contributions", "files":["Course transcript","Marketing small-scale honey","Pollination contracts & opportunities","Hive stocking rates","Equipment & startup costs","Inventory workbook","Pesticides & neonics"]},
 {"mod":"Exam prep", "files":["Full syllabus","Oral topic list","Oral exam rubric","Field exam rubrics","Field exam video outline"]},
]

DATA = {"glossary": G, "quickfacts": QUICKFACTS, "varroa": VARROA, "varroaNote": VARROA_NOTE,
        "inspect": INSPECT, "disease": DISEASE, "library": LIBRARY}
out = json.dumps(DATA, ensure_ascii=False, separators=(",",":"))
open(r"C:\Users\leasy\bee-manual\data.json","w",encoding="utf-8").write(out)
print("data.json:", len(out), "bytes |", len(G), "glossary terms")
