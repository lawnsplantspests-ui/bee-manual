# Recipes — things you actually mix, in the order of "what do I put in the pot."
#
# Sources are named on each card so they can be checked against the original.
# The oxalic acid / glycerin numbers come straight from Randy Oliver's current
# write-up (scientificbeekeeping.com, "Extended-release oxalic acid for varroa
# management", updated 27 May 2026): 1:1 by WEIGHT, 50 g oxalic + 50 g glycerin
# per double-deep hive, one full Swedish sponge cut into two pads.
#
# Edit this file, then run build_data.py and assemble.py. Never edit the baked
# DATA blob inside index.html — a rebuild wipes it.

CATS = ["Mite treatment", "Feeding", "Swarms", "From the hive"]

RECIPES = [

# ---------------------------------------------------------------- mite treatment
{"id": "oagly", "cat": "Mite treatment", "open": True,
 "name": "Oxalic acid + glycerin pads",
 "sub": "The “OA/gly” extended-release treatment",
 "what": "Oxalic acid only kills mites riding on adult bees — it does not reach mites sealed in brood "
         "cells. A dribble or a vaporizer is a one-shot: big mite drop, over in about three days. Soak "
         "oxalic acid in glycerin on a cellulose pad and it keeps releasing for two months, so it is "
         "still working as each new batch of mites walks out of the brood. That is why this is the one "
         "oxalic method that works on a hive full of brood. It is slow — figure two months to full "
         "effect — so it goes in ahead of a mite problem, not on top of one.",
 "warn": "Homemade OA/glycerin pads are not an EPA-registered product. EPA has left “own use” up to "
         "each state, so in Pennsylvania it is the Dept. of Agriculture’s call — ask them before you "
         "make a batch, and ask about a Pesticide Research Authorization. You cannot make these for "
         "anyone else, sell them, or haul them to someone else’s hives. The off-the-shelf legal version "
         "of the same idea is VarroxSan. And this is acid: safety glasses and waterproof gloves, and a "
         "jug of baking soda water (1 cup per gallon) sitting next to you the whole time.",
 "need": [
   "Oxalic acid dihydrate — 99.6% wood bleach, or Api-Bioxal / EZ-OX. <b>50 g per hive</b>",
   "Food-grade vegetable glycerin. <b>50 g per hive</b> (50 g is about 40 mL — weigh it, don’t measure it)",
   "Swedish sponge cloths, no moisturizer and no plastic mesh — one full sponge per hive. “If You Care” "
   "brand is the one Oliver uses. Plain chipboard also works (see tips)",
   "A stainless pan and a burner you can hold steady at 160 °F — an induction plate is ideal",
   "Kitchen scale, thermometer, long stainless spoon, tongs",
   "Safety glasses and waterproof gloves (5 mil vinyl is enough)",
   "Baking soda, 1 cup per gallon of water, mixed in a jug before you start",
 ],
 "table": {"cap": "Equal weights of each — 1:1 by weight, not by volume. One double-deep hive gets 50 g + 50 g, "
                  "which is one full Swedish sponge cut into two pads.",
           "cols": ["Hives", "Oxalic acid", "Glycerin", "Pads"],
           "rows": [["2", "100 g", "100 g (80 mL)", "4"],
                    ["5", "250 g", "250 g (200 mL)", "10"],
                    ["10", "500 g", "500 g (400 mL)", "20"],
                    ["20", "1,000 g", "1,000 g (800 mL)", "40"]]},
 "steps": [
   "Cut each sponge in half, into two pads about 3½ × 8 inches. Both halves go in the same hive.",
   "Rub dry baking soda on your hands, then glove up and put the glasses on.",
   "Weigh the oxalic acid into the stainless pan <b>first</b>, then pour the glycerin on top of it. Acid "
   "first, liquid second — that way nothing splashes.",
   "Heat it slowly and stir the entire time. Crystals start dissolving around 110 °F. Keep it under "
   "<b>160 °F</b> and never let it pass 170 °F — past that it bubbles and starts breaking down.",
   "Keep stirring until the liquid goes completely clear. The acid melts into a layer underneath the "
   "glycerin, so if you stop stirring the bottom layer scorches.",
   "With the solution still hot, stand the pads in the pan on edge and let them drink it up, turning them "
   "once with tongs. Hot solution soaks in fast; once it cools it stops soaking in at all, so keep the "
   "heat on at 160 °F while they absorb.",
   "If there is liquid left in the pan, lift and drain the pads before they cool.",
   "Let them sit at least a day before you use them. The acid recrystallizes and they quit dripping. "
   "White crystals on the outside are normal and fine.",
 ],
 "use": [
   "Two pads per hive, laid flat across the top bars between the two brood boxes — one toward the front, "
   "one toward the back. That leaves the middle open for a pollen patty.",
   "They have to sit <b>inside the cluster</b>, where bees walk across both sides of them. Tucked under "
   "the lid, they do nothing at all.",
   "Best timing is the day you put supers on — spring or early summer. This is a get-ahead treatment.",
   "Leave them <b>60–75 days</b>, or until the bees have chewed up most of them.",
   "Spot-check: a pad that is still working feels damp, and tastes sour like lemon juice on a fingertip. "
   "A pad that has gone dry is finished, whatever the calendar says.",
   "Pull them at the end, bag them (they still hold acid), and landfill or compost them. Rinse hands, "
   "hive tool and smoker with the baking soda water.",
   "Once a season, and rotate — next round use a different mode of action (formic, thymol, or amitraz). "
   "Save the dribble or the vaporizer for the winter brood break.",
 ],
 "tips": [
   "It does not build up in wax and does not contaminate honey — but the pad material itself has to be "
   "clean. Plain cellulose, no plastic mesh, no moisturizer, no scent.",
   "Don’t put a pad under a top feeder where syrup can drip on it, or flat against a pollen patty.",
   "Cardboard version: cut plain chipboard into 1.5 × 15 inch strips and hang 3–4 per brood chamber over "
   "the top bars, down between the frames. Each strip takes about 20 g of solution, and 50 strips fit a "
   "500 g + 500 g batch. Cardboard soaks slowly — give it hours or overnight with the pan kept warm. Cut "
   "them a little short of the bottom bar so the queen can walk around them.",
   "A 1:1 mix is supersaturated, so it will crystallize in the pan at room temperature. Just reheat it.",
   "Humid day? Keep a lid on the pan. Glycerin pulls water straight out of the air and the pads turn messy.",
   "Made pads store sealed for about two months, after which the cellulose starts to break down.",
 ],
 "src": "Randy Oliver, ScientificBeekeeping.com — “Extended-release oxalic acid for varroa management,” "
        "updated 27 May 2026."},

{"id": "oadrib", "cat": "Mite treatment",
 "name": "Oxalic acid dribble syrup",
 "sub": "The broodless one-shot",
 "what": "Mix oxalic acid into thin syrup and run it down between the frames. It only touches mites on "
         "adult bees, so it is a late-fall or warm-winter-day treatment, after the brood is gone. On a "
         "truly broodless colony it is excellent. On a colony with brood it is barely worth doing.",
 "warn": "Mix to the label on the package you actually bought — the label is the law, and rates differ by "
         "product. This is the Api-Bioxal rate. One dribble per colony per year: repeat dribbles shorten "
         "bee lifespan. Gloves and eye protection.",
 "need": [
   "Api-Bioxal (or another registered oxalic acid product) — <b>35 g per litre</b>",
   "1 litre of 1:1 sugar syrup (about 1 lb sugar dissolved in 2 cups warm water, then topped up to a litre)",
   "60 mL syringe, gloves, safety glasses",
 ],
 "steps": [
   "Make the 1:1 syrup and let it cool to about body temperature.",
   "Stir in 35 g of Api-Bioxal per litre until it is fully dissolved.",
   "Use it the day you mix it. Oxalic syrup breaks down in storage and gets harder on the bees.",
 ],
 "use": [
   "5 mL trickled down each seam of bees between frames.",
   "<b>50 mL maximum per colony</b> — so ten seams is the most that counts, no matter how big the hive is.",
   "Supers off, and two weeks before supers go back on.",
   "Pick a day above about 37 °F so you can crack the lid without chilling them.",
 ],
 "tips": ["The app’s Oxalic acid calculator under Calculators does this math for a whole yard at once.",
          "One litre of mixed syrup treats about 20 average colonies."],
 "src": "Api-Bioxal US label rate (35 g per litre of 1:1 syrup, 5 mL per seam, 50 mL cap per colony)."},

# ---------------------------------------------------------------------- feeding
{"id": "syrup", "cat": "Feeding",
 "name": "Sugar syrup — 1:1 and 2:1",
 "sub": "Spring build-up and fall stores",
 "what": "1:1 in spring reads like a nectar flow and switches on brood rearing and wax building. 2:1 in "
         "fall is for packing weight into the hive before winter — thicker, so there is less water for "
         "them to fan off. Same sugar either way, different ratio.",
 "table": {"cap": "By weight. A gallon of water weighs 8.3 lb, so 8 lb of sugar to a gallon is close enough to 1:1.",
           "cols": ["Mix", "Sugar", "Water", "Makes"],
           "rows": [["1:1", "8 lb", "1 gallon", "about 1½ gal"],
                    ["1:1 small", "2 lb", "1 quart", "about 1½ qt"],
                    ["2:1", "16 lb", "1 gallon", "about 2¼ gal"],
                    ["2:1 small", "4 lb", "1 quart", "about 2¼ qt"]]},
 "need": ["Plain white granulated sugar — nothing else",
          "Water",
          "Optional: 1 tsp white vinegar per gallon, which holds mold off"],
 "steps": [
   "Heat the water hot but <b>do not boil it with the sugar in it</b>. Boiled sugar makes HMF, which is "
   "toxic to bees.",
   "Take it off the heat, then stir the sugar in until the syrup runs clear. 2:1 needs the water hot to "
   "dissolve at all.",
   "Cool it before you feed it.",
 ],
 "use": [
   "Feed inside the hive. Open feeding in the yard starts robbing and feeds every colony in the "
   "neighborhood but yours.",
   "Supers off. Fed syrup stored in a super is sugar water, not honey.",
   "Once nights sit below about 50 °F they stop taking syrup down. After that it is sugar bricks or dry "
   "sugar.",
 ],
 "tips": ["Mix what they will take in a week. Syrup molds.",
          "1:1 also goes on new packages, new nucs, and any colony being asked to draw foundation."],
 "src": "Standard ratios; the boil/HMF caution is the usual extension guidance."},

{"id": "bricks", "cat": "Feeding",
 "name": "Winter sugar bricks",
 "sub": "Hard feed that sits on the top bars",
 "what": "Sugar cakes you set right on the top bars in winter. The bees can chew them at cluster "
         "temperature long after syrup is out of the question, and they soak up hive moisture while they "
         "sit there — and moisture is what actually kills a winter colony, not cold.",
 "need": ["10 lb white granulated sugar",
          "2 cups (1 pint) water",
          "Optional: ¼ cup white vinegar, which keeps mold down",
          "A sheet pan, or a shallow rim/shim lined with parchment"],
 "steps": [
   "Dump the sugar in a tub. Add the water (and vinegar) a little at a time, mixing with your hands.",
   "You are after <b>damp sand</b> — squeeze a handful and it should hold its shape without dripping. Too "
   "wet and it takes days to dry and can mold.",
   "Press it down hard, about ¾ to 1 inch thick.",
   "Dry it: oven at 170 °F for an hour or two, or just leave it out a day or two until it is solid.",
   "Break it into bricks that fit across the top bars.",
 ],
 "use": ["Brick straight on the top bars over the cluster, an empty rim or shim above it for headroom, "
         "inner cover and lid back on.",
         "Check on a mild day in January or February and add more if it is going fast."],
 "tips": ["Heft the back of the hive first. A hive that is still heavy in December does not need this.",
          "No essential oils and no pollen substitute in winter bricks — you do not want brood rearing yet."],
 "src": "Common winter-feeding practice; the damp-sand texture test is the part that matters."},

{"id": "drysugar", "cat": "Feeding",
 "name": "Mountain camp dry sugar",
 "sub": "Two-minute emergency feed",
 "what": "The no-recipe recipe. When a hive feels light in January and it is too cold to do anything "
         "proper, this goes on with the hive open for under a minute.",
 "need": ["4–5 lb plain granulated sugar per hive", "A sheet of newspaper", "A shim or empty super",
          "A spray bottle of water"],
 "steps": [
   "Put a shim or an empty super on top of the brood box.",
   "Lay newspaper across the top bars, leaving a gap at the front edge so bees can get past.",
   "Pour the sugar on the paper and mound it toward the back.",
   "Mist the top of the mound lightly so it crusts over instead of sifting down.",
   "Inner cover and lid back on.",
 ],
 "use": ["Check monthly through the winter and top it up.",
         "Works as a moisture sponge as well as feed — the sugar takes up condensation that would "
         "otherwise drip back onto the cluster."],
 "src": "Standard “mountain camp” method."},

{"id": "patty", "cat": "Feeding",
 "name": "Pollen substitute patty",
 "sub": "Protein for brood build-up",
 "what": "Sugar keeps bees alive; pollen makes new bees. A patty is for early spring when the colony "
         "wants to build up and nothing is blooming yet, or for a summer dearth.",
 "warn": "Do not mix real trapped pollen into a homemade patty unless it has been irradiated. Pollen from "
         "another apiary is one of the easiest ways to move American foulbrood into your own hives. And "
         "stop feeding pollen substitute in the fall — it pushes brood rearing at exactly the wrong time.",
 "need": ["2 lb dry pollen substitute powder — Ultra Bee, Bee-Pro or MegaBee, or a homemade brewer’s "
          "yeast and soy flour blend",
          "About 1½ cups of 2:1 syrup",
          "Wax paper"],
 "steps": [
   "Stir the syrup into the powder a little at a time until it comes together as a stiff dough — play "
   "dough, not batter.",
   "Press into ½-inch patties between two sheets of wax paper.",
   "Freeze what you are not using this week.",
 ],
 "use": ["One patty on the top bars directly over the brood. Peel the top sheet of wax paper off and "
         "leave the bottom one so it does not weld itself to the frames.",
         "Replace when they have eaten it, roughly every one to two weeks.",
         "Pull any patty they are ignoring — small hive beetles will breed in it."],
 "src": "Standard patty practice; the irradiation warning is the usual state-apiarist guidance."},

{"id": "stim", "cat": "Feeding",
 "name": "Essential-oil feeding stimulant",
 "sub": "The homemade Honey-B-Healthy",
 "what": "A mint concentrate you stir into feeding syrup. It gets bees taking syrup faster, helps a "
         "package or a shaken swarm settle into new equipment, and masks hive smell when you combine two "
         "colonies. It is not a mite treatment and it does not replace real forage.",
 "need": ["5 cups water",
          "2½ lb white sugar",
          "⅛ tsp lecithin granules — the emulsifier; without it the oil just floats on top",
          "15 drops spearmint oil",
          "15 drops lemongrass oil"],
 "steps": [
   "Heat the water, take it off the heat, stir in the sugar until clear.",
   "While it is still warm, stir in the lecithin until it disappears.",
   "Add both oils and stir hard.",
   "Bottle it. It keeps for months at room temperature — shake before each use.",
 ],
 "use": ["1–2 teaspoons of concentrate per quart of feeding syrup.",
         "Not with supers on. The mint comes through into honey."],
 "src": "The widely circulated homemade version of the commercial product."},

# ----------------------------------------------------------------------- swarms
{"id": "lure", "cat": "Swarms",
 "name": "Swarm trap lure",
 "sub": "Lemongrass oil",
 "what": "Lemongrass oil is close enough to the Nasonov pheromone that scout bees use to call a swarm "
         "in. It is free bees, if the box is in the right place — and the box matters more than the lure.",
 "need": ["Lemongrass essential oil", "A cotton ball", "A small zip bag or film canister",
          "An empty deep or any box around 40 litres", "One old dark drawn comb, if you have one"],
 "steps": [
   "Two or three drops on a cotton ball — not more.",
   "Seal it in a zip bag with a pinhole in it, or in a film canister with the lid cracked. You want it "
   "seeping, not blasting.",
   "Set it near the entrance, inside the box.",
 ],
 "use": ["Box around 40 litres (a 10-frame deep is close), entrance 1–2 square inches near the bottom, "
         "10–15 feet up, shaded, facing south, on a woods edge.",
         "One frame of old black comb pulls better than any lure you can buy.",
         "Refresh the oil every 2–3 weeks through May and June.",
         "Check weekly and move them within about three days of moving in, before they build comb."],
 "tips": ["Quarantine every swarm you catch — mite wash and treat it, and watch the brood through a full "
          "cycle before those frames go anywhere near your other hives."],
 "src": "Standard swarm-trap practice (Seeley’s trap dimensions)."},

# ------------------------------------------------------------------ from the hive
{"id": "balm", "cat": "From the hive",
 "name": "Lip balm",
 "sub": "1 : 2 : 1 by weight",
 "what": "Firm enough to hold a tube in a hot truck, soft enough not to drag. Makes about 25 tubes.",
 "need": ["25 g beeswax, grated or pastilles",
          "50 g liquid oil — sweet almond, jojoba or fractionated coconut",
          "25 g shea or cocoa butter",
          "Optional: ½ tsp honey, 15–20 drops flavor oil, 1 capsule vitamin E"],
 "steps": [
   "Double boiler — a Pyrex cup standing in a pan of simmering water. Wax never goes on direct heat.",
   "Melt the beeswax first, then the butter, then stir in the oil.",
   "Off the heat, stir in the honey and flavor oil. Flavor goes in last and below 150 °F or it cooks off.",
   "Test it: drip a little on a cold spoon and feel it. Too hard, add oil. Too soft, add wax.",
   "Pour fast — it sets quickly — and cap after an hour.",
 ],
 "tips": ["Jar or pot balm instead of tubes: go softer, 1 part wax to 4 parts oil.",
          "Devon’s beehive lip balm dispenser holds the standard 0.15 oz tube."],
 "src": "Standard 1:2:1 wax / oil / butter balm ratio."},

{"id": "salve", "cat": "From the hive",
 "name": "Beeswax salve",
 "sub": "1 part wax to 4 parts oil",
 "what": "A hand and skin salve. Same idea as the balm, more oil, poured into tins.",
 "need": ["30 g beeswax",
          "120 g oil — olive, sweet almond, or an herb-infused oil",
          "Optional: 1.5 g (about 30 drops) essential oil",
          "Five 2 oz tins"],
 "steps": ["Melt the wax in a double boiler, stir the oil in.",
           "Off the heat, stir in essential oil if you want scent.",
           "Pour into tins and leave them alone until set."],
 "tips": ["Firmer: 1 to 3. Softer: 1 to 5. Cold-spoon test the same way as lip balm.",
          "Infuse the olive oil with calendula and plantain for a stings-and-scrapes version.",
          "Label it as a cosmetic. The moment the label says it treats something, it is legally a drug."],
 "src": "Standard salve ratio."},

{"id": "propolis", "cat": "From the hive",
 "name": "Propolis tincture",
 "sub": "20% extract",
 "what": "An alcohol extract of propolis scrapings. It is the easiest thing to sell next to honey at a "
         "market, and it costs nothing but the alcohol.",
 "need": ["100 g cleaned propolis scrapings",
          "400 mL of 190-proof food-grade grain alcohol (Everclear)",
          "A glass jar, coffee filters, amber dropper bottles"],
 "steps": [
   "Freeze the propolis first, then break it up. It shatters when cold and smears when warm.",
   "Jar it with the alcohol and seal it.",
   "Shake it daily for two weeks, in a dark cupboard at room temperature.",
   "Strain through a coffee filter.",
   "Bottle in amber glass.",
 ],
 "warn": "Food-grade grain alcohol only — never rubbing alcohol, never denatured alcohol.",
 "tips": ["Alcohol-free version: same ratio in food-grade vegetable glycerin, four weeks, kept warm. It "
          "comes out weaker.",
          "Sell it as propolis extract. No health claims on the label."],
 "src": "Standard 1:4 propolis-to-alcohol tincture."},

{"id": "renderwax", "cat": "From the hive",
 "name": "Rendering beeswax",
 "sub": "Cappings to clean blocks",
 "what": "Turning cappings, burr comb and scrapings into blocks you can actually use.",
 "warn": "Double boiler only. Beeswax catches fire around 400 °F, and you cannot put a wax fire out with "
         "water. Never leave it on direct heat and never walk away from it.",
 "need": ["Cappings and comb scrapings", "A pot of water and a second pot or heavy stainless bowl",
          "Paint strainer bags or a few layers of cheesecloth", "A mold — silicone loaf pan, milk carton, "
          "anything"],
 "steps": [
   "Rinse the cappings in <b>cool</b> water until it runs clear. Warm water sets the honey and makes a "
   "sticky mess.",
   "Melt the wax over water in a double boiler, with an inch of water in the bottom of the melting pot.",
   "The slumgum and dirt sink into the water layer; clean wax floats on top.",
   "Pour it through a strainer bag or cheesecloth into the mold.",
   "Once it is cool, scrape the gunk off the bottom of the block. Re-melt and re-strain if you want it "
   "cleaner still.",
 ],
 "tips": ["Stainless or enamel only. Aluminum, iron and copper all discolor wax.",
          "About 1 lb of wax per 60–100 lb of honey harvested is normal."],
 "src": "Standard rendering practice."},

{"id": "mead", "cat": "From the hive",
 "name": "One-gallon mead",
 "sub": "A starter batch",
 "what": "Three pounds of honey to the gallon lands around 12% alcohol. Start here before you scale up.",
 "need": ["3 lb honey (2½ lb for something drier and lighter)",
          "Spring water to make 1 gallon",
          "1 packet wine yeast — Lalvin 71B or D47",
          "1 tsp yeast nutrient",
          "1 gal carboy, airlock, sanitizer"],
 "steps": [
   "Sanitize everything you are going to touch.",
   "Warm a quart of water — warm, not hot, you are not cooking the honey — and dissolve the honey into it.",
   "Top up to a gallon in the carboy and shake it hard to aerate.",
   "At room temperature, under 75 °F, pitch the yeast and add the nutrient.",
   "Airlock it. It should be bubbling within 24–48 hours.",
   "Rack it off the lees at 3–4 weeks, then again at three months.",
   "Bottle at six months. Drink at a year — it is harsh before that and it is supposed to be.",
 ],
 "tips": ["The Mead calculator under Calculators will do other batch sizes and target strengths."],
 "src": "Standard traditional mead, 3 lb honey per gallon."},

]
