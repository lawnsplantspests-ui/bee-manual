# Replaces the Bee Field Guide's Calculators view with the full set carried over from
# The Bee Bench (bench.allemanapiary.com). Idempotent — safe to re-run.
#   python add_calcs.py
import io, re

PATH = "index.html"
START = "  // ---- Calculators ----"
END = "  // ---- Oral exam prep ----"

NEW = r'''  // ---- Calculators ----
  // Ported from The Bee Bench (bench.allemanapiary.com). One calculator shown at a time;
  // `calcPick` survives re-renders so switching views and coming back keeps your place.
  var calcPick = 'mite';

  const CALCS = [
    {id:'mite',  ic:'🪲', nm:'Mite wash'},
    {id:'syrup', ic:'🍯', nm:'Sugar syrup'},
    {id:'oxalic',ic:'💧', nm:'Oxalic acid'},
    {id:'feed',  ic:'❄️', nm:'Winter feed'},
    {id:'yield', ic:'⚖️', nm:'Honey yield'},
    {id:'moist', ic:'💦', nm:'Moisture'},
    {id:'queen', ic:'📅', nm:'Queen timeline'},
    {id:'color', ic:'👑', nm:'Queen color'},
    {id:'patty', ic:'🥞', nm:'Pollen patty'},
    {id:'mead',  ic:'🍶', nm:'Mead'},
  ];

  function ci(label, id, attrs){ return '<div class="cinput"><label>'+label+'</label><input id="'+id+'" '+attrs+'></div>'; }
  function cs(label, id, opts){ return '<div class="cinput"><label>'+label+'</label><select id="'+id+'" class="qsel">'+opts+'</select></div>'; }
  function num(id){ return parseFloat(document.getElementById(id).value); }
  function val(id){ return document.getElementById(id).value; }
  function out(id, cls, html){ const o=document.getElementById(id); o.className='cout '+(cls||''); o.innerHTML=html; }
  function on(ids, fn){ ids.forEach(id=>{ const el=document.getElementById(id); el.oninput=fn; el.onchange=fn; }); fn(); }

  function renderCalc(){
    app.innerHTML =
      '<p class="lead">Field calculators. Everything runs offline and nothing is saved.</p>'+
      '<div class="cchips">'+CALCS.map(c=>
        '<button class="cchip'+(c.id===calcPick?' on':'')+'" data-c="'+c.id+'">'+c.ic+' '+c.nm+'</button>').join('')+'</div>'+
      '<div id="calcBody"></div>';
    app.querySelectorAll('.cchip').forEach(b=>b.onclick=()=>{ calcPick=b.dataset.c; renderCalc(); });
    ({mite:cMite, syrup:cSyrup, oxalic:cOxalic, feed:cFeed, yield:cYield,
      moist:cMoist, queen:cQueen, color:cColor, patty:cPatty, mead:cMead})[calcPick]();
  }
  function body(html){ document.getElementById('calcBody').innerHTML = html; }

  // --- Varroa mite wash
  function cMite(){
    body('<div class="card"><h3>🪲 Varroa mite wash</h3>'+
      cs('Method','m_meth','<option value="1">Alcohol wash / soapy water</option><option value="0.75">Powdered sugar roll</option>')+
      cs('Sample','m_bees','<option value="300">½ cup — ~300 bees</option><option value="200">⅓ cup — ~200 bees</option><option value="150">¼ cup — ~150 bees</option>')+
      ci('Mites counted','m_mites','type="number" inputmode="numeric" min="0" value="6"')+
      cs('Time of year','m_seas','<option value="2">Spring — building up</option><option value="3" selected>Summer — peak</option><option value="2">Aug–Sep — winter bees</option><option value="1">Late fall — broodless</option>')+
      '<div id="m_out" class="cout"></div>'+
      '<div class="note">Sample from an open brood frame — that is where the mites are. Shake bees into a tub first and make sure the queen is not in there.</div></div>');
    on(['m_meth','m_bees','m_mites','m_seas'], ()=>{
      const m=num('m_mites'), b=num('m_bees'), eff=parseFloat(val('m_meth')), t=parseFloat(val('m_seas'));
      if(!(m>=0)||!(b>0)) return out('m_out','','Enter your wash results above.');
      const pct=m/b*100, adj=pct/eff;
      let v,cls;
      if(adj<t*0.5){ v='Low — recheck in three or four weeks.'; cls='good'; }
      else if(adj<t){ v='Below threshold but climbing. Line up a treatment and recheck in two weeks.'; cls='mid'; }
      else if(adj<t*2){ v='Over the threshold for this time of year — treat.'; cls='low'; }
      else { v='Well over. Treat now and plan a follow-up test.'; cls='low'; }
      out('m_out',cls,'<b>'+pct.toFixed(1)+' mites per 100 bees</b> · threshold now is '+t+'/100<br>'+
        (eff<1?'<i>A sugar roll finds about three quarters of what a wash would — judge against roughly '+adj.toFixed(1)+'/100.</i><br>':'')+v+
        '<br><span style="opacity:.75">About '+Math.round(pct/100*30000).toLocaleString()+' mites on adults in a 30,000-bee colony — and with capped brood, most of the mites are hidden in cells.</span>');
    });
  }

  // --- Sugar syrup
  function cSyrup(){
    body('<div class="card"><h3>🍯 Sugar syrup mixer</h3>'+
      cs('Ratio','s_r','<option value="1">1:1 — spring, stimulates brood</option><option value="2" selected>2:1 — fall, winter stores</option>')+
      cs('Start from','s_mode','<option value="gal">Gallons of syrup I want</option><option value="sugar" selected>Pounds of sugar I have</option>')+
      ci('Amount','s_amt','type="number" inputmode="decimal" min="0" value="10"')+
      '<div id="s_out" class="cout"></div>'+
      '<div class="note">By weight. Dissolve in hot — never boiling — water: scorched syrup makes HMF, which is toxic to bees. Plain white granulated sugar only.</div></div>');
    on(['s_r','s_mode','s_amt'], ()=>{
      const r=parseFloat(val('s_r')), a=num('s_amt'), W=8.345, D=13.24;
      if(!(a>0)) return out('s_out','','Enter an amount above.');
      let sugar, waterLb;
      if(val('s_mode')==='sugar'){ sugar=a; waterLb=sugar/r; }
      else { sugar = a/(1/(r*W)+1/D); waterLb=sugar/r; }
      const waterGal=waterLb/W, yieldGal=waterGal+sugar/D, conc=sugar/(sugar+waterLb)*100;
      out('s_out','good','<b>'+sugar.toFixed(1)+' lb sugar</b> + <b>'+(waterGal*4).toFixed(2)+' quarts water</b> '+
        '('+(waterGal*16).toFixed(1)+' cups)<br>Makes about <b>'+yieldGal.toFixed(2)+' gallons</b>, '+conc.toFixed(0)+'% sugar by weight, '+
        'weighing '+(sugar+waterLb).toFixed(1)+' lb.');
    });
  }

  // --- Oxalic acid
  function cOxalic(){
    body('<div class="card"><h3>💧 Oxalic acid dosing</h3>'+
      cs('Method','o_m','<option value="dribble">Dribble — syringe between seams</option><option value="vapor">Vaporize — heated wand</option><option value="strips">Extended-release strips</option>')+
      ci('Hives','o_h','type="number" inputmode="numeric" min="1" value="4"')+
      ci('Seams or boxes each','o_p','type="number" inputmode="numeric" min="1" value="8"')+
      '<div id="o_out" class="cout"></div>'+
      '<div class="note"><b>The label is the law.</b> Rates here follow the current Api-Bioxal label. Vaporizing needs an acid-gas respirator and sealed goggles — not a dust mask. Oxalic acid only reaches mites riding on adult bees, so it works best on a broodless colony.</div></div>');
    on(['o_m','o_h','o_p'], ()=>{
      const m=val('o_m'), h=num('o_h'), p=num('o_p');
      if(!(h>0)||!(p>0)) return out('o_out','','Enter hives and seams or boxes.');
      if(m==='dribble'){
        const seams=Math.min(p,10), ml=seams*5, tot=ml*h, acid=tot/1000*35;
        out('o_out','good','<b>'+ml+' mL per hive</b> ('+seams+' seams × 5 mL)<br><b>'+tot+' mL total</b>, made with <b>'+acid.toFixed(1)+' g Api-Bioxal</b> in 1:1 syrup at 35 g per litre.'+
          (p>10?'<br><i>Label caps a colony at 50 mL, so 10 seams is the most that counts.</i>':''));
      } else if(m==='vapor'){
        const g=p*4, tot=g*h;
        out('o_out','good','<b>'+g+' g per hive</b> (4 g per brood chamber)<br><b>'+tot+' g total</b> — '+Math.ceil(tot/35)+' × 35 g packet(s). Seal the entrance, vaporize, leave shut about 10 minutes.');
      } else {
        const s=p*4, tot=s*h;
        out('o_out','good','<b>'+s+' strips per hive</b> (4 per brood chamber)<br><b>'+tot+' strips total</b>. Leave in 42–56 days, then pull them — leaving strips past the window breeds resistance.');
      }
    });
  }

  // --- Overwinter feed
  function cFeed(){
    body('<div class="card"><h3>❄️ Overwinter feed</h3>'+
      cs('Your winter','f_c','<option value="45">Mild south — zone 8+</option><option value="60">Upper south — zone 7</option><option value="80" selected>Mid-Atlantic — zone 6</option><option value="90">Northern — zone 5</option><option value="100">Far north — zone 4</option>')+
      ci('Deep frames of honey','f_d','type="number" inputmode="decimal" min="0" value="6"')+
      ci('Medium frames','f_m','type="number" inputmode="decimal" min="0" value="4"')+
      ci('Hives','f_h','type="number" inputmode="numeric" min="1" value="4"')+
      '<div id="f_out" class="cout"></div>'+
      '<div class="note">Feed early. Once nights sit below about 50 °F they stop taking syrup down, and after that it is fondant or dry sugar. Heft the back of the hive every few weeks all winter.</div></div>');
    on(['f_c','f_d','f_m','f_h'], ()=>{
      const t=parseFloat(val('f_c')), have=(num('f_d')||0)*7+(num('f_m')||0)*5, h=num('f_h')||1;
      const short=Math.max(0,t-have);
      if(short<=0) return out('f_out','good','<b>About '+have.toFixed(0)+' lb of stores</b> against a '+t+' lb target — nothing to feed. Keep hefting through the winter anyway.');
      const gal=short/7.38, sugar=gal*h*7.38;
      out('f_out', have/t>=0.75?'mid':'low',
        '<b>'+short.toFixed(0)+' lb short per hive</b> — they have about '+have.toFixed(0)+' lb, they want '+t+' lb.<br>'+
        'That is <b>'+gal.toFixed(1)+' gal of 2:1 syrup per hive</b>, '+(gal*h).toFixed(1)+' gal for '+h+' hive(s), '+
        'made from about <b>'+sugar.toFixed(0)+' lb of sugar</b> ('+Math.ceil(sugar/25)+' × 25 lb bags).');
    });
  }

  // --- Honey yield
  function cYield(){
    body('<div class="card"><h3>⚖️ Honey yield &amp; jars</h3>'+
      ci('Hives','y_h','type="number" inputmode="numeric" min="1" value="4"')+
      ci('Supers each','y_s','type="number" inputmode="numeric" min="0" value="2"')+
      cs('Frame size','y_f','<option value="7">Deep — 7 lb/frame</option><option value="5" selected>Medium — 5 lb/frame</option><option value="3.5">Shallow — 3.5 lb/frame</option>')+
      ci('Frames per super','y_n','type="number" inputmode="numeric" min="1" value="10"')+
      ci('How full, capped (%)','y_p','type="number" inputmode="numeric" min="0" max="100" value="80"')+
      '<div id="y_out" class="cout"></div>'+
      '<div class="note">Frame averages, not a scale. If the number matters, weigh the supers before and after extracting.</div></div>');
    on(['y_h','y_s','y_f','y_n','y_p'], ()=>{
      const lbs=(num('y_h')||0)*(num('y_s')||0)*(num('y_n')||0)*parseFloat(val('y_f'))*((num('y_p')||0)/100);
      if(!(lbs>0)) return out('y_out','','Fill in the boxes above.');
      const gal=lbs/11.85;
      out('y_out','good','<b>'+Math.round(lbs).toLocaleString()+' lb of honey</b> — '+gal.toFixed(1)+' gallons, about '+(gal/5).toFixed(1)+' five-gallon buckets.<br>'+
        'That is '+Math.floor(lbs).toLocaleString()+' one-pound jars, '+Math.floor(lbs/0.75).toLocaleString()+' twelve-ounce, or '+Math.floor(lbs/5).toLocaleString()+' five-pound.<br>'+
        '<span style="opacity:.75">Plus roughly '+(lbs*0.01).toFixed(1)+'–'+(lbs*0.02).toFixed(1)+' lb of cappings wax.</span>');
    });
  }

  // --- Honey moisture
  function cMoist(){
    body('<div class="card"><h3>💦 Honey moisture</h3>'+
      cs('Reading is','w_s','<option value="water" selected>% water (honey refractometer)</option><option value="brix">°Brix</option>')+
      ci('Reading','w_v','type="number" inputmode="decimal" step="0.1" value="17.5"')+
      '<div id="w_out" class="cout"></div>'+
      '<div class="note">Read a well-mixed sample at room temperature. The top of a settled bucket reads wetter than the bucket really is.</div></div>');
    on(['w_s','w_v'], ()=>{
      const v=num('w_v'); if(!(v>0)) return out('w_out','','Enter your reading.');
      const water = val('w_s')==='brix' ? 100-v : v;
      let cls,msg;
      if(water<17.1){ cls='good'; msg='Safe — will not ferment at any yeast count. Jar it and store it as long as you like.'; }
      else if(water<=18.0){ cls='good'; msg='Good. Comfortably normal for well-cured honey.'; }
      else if(water<=18.6){ cls='mid'; msg='Still USDA Grade A, but at the edge. Sell it fresh and keep it cool.'; }
      else if(water<=20){ cls='low'; msg='Below Grade A and a real fermentation risk. Dry it down before jarring, or set it aside for mead.'; }
      else { cls='low'; msg='It will ferment. Do not sell it — mead, or feed it back to your own bees.'; }
      out('w_out',cls,'<b>'+water.toFixed(1)+'% water</b> ('+(100-water).toFixed(1)+'° Brix) · USDA Grade A limit is 18.6%<br>'+msg);
    });
  }

  // --- Split & queen timeline
  function cQueen(){
    body('<div class="card"><h3>📅 Split &amp; queen timeline</h3>'+
      cs('What happened','q_k','<option value="walkaway" selected>Walk-away split</option><option value="swarm">They swarmed</option><option value="cell">Installed a queen cell</option><option value="graft">Grafted larvae</option><option value="mated">Installed a mated queen</option>')+
      ci('Date','q_d','type="date"')+
      '<div id="q_out" class="cout"></div>'+
      '<div class="note">Weather runs this schedule, not the calendar. A queen needs a calm afternoon above about 68 °F to mate — a cold wet spell pushes everything back.</div></div>');
    const d=new Date();
    document.getElementById('q_d').value=[d.getFullYear(),String(d.getMonth()+1).padStart(2,'0'),String(d.getDate()).padStart(2,'0')].join('-');
    const PLAN={
      walkaway:[[0,'Split made — they start emergency cells within hours'],[5,'Queen cells capped'],[12,'Virgin emerges'],[17,'Mating flights begin'],[24,'First eggs — safe to look now'],[31,'Check the brood pattern']],
      swarm:[[0,'Swarm issued, capped cells already in the hive'],[8,'Virgin emerges'],[12,'Mating flights begin'],[19,'First eggs'],[26,'Check the pattern']],
      cell:[[0,'Cell installed — keep it upright and warm'],[2,'Queen emerges if the cell was near due'],[8,'Mating flights begin'],[16,'First eggs'],[23,'Check the pattern']],
      graft:[[0,'Graft 12–36 hour larvae'],[1,'Check acceptance'],[5,'Cells capped'],[10,'MOVE CELLS to mating nucs — today'],[11,'Queens emerge'],[16,'Mating flights'],[24,'First eggs'],[31,'Evaluate and select']],
      mated:[[0,'Queen installed in her cage — colony must be truly queenless'],[3,'Candy plug chewed through, she should be out'],[7,'Quick look: cage empty, queen walking?'],[10,'First eggs'],[17,'Check the pattern']]
    };
    const QUIET={walkaway:[3,24],swarm:[0,19],cell:[0,16],graft:[5,21],mated:[0,7]};
    on(['q_k','q_d'], ()=>{
      const raw=val('q_d'); if(!raw) return out('q_out','','Pick a date.');
      const p=raw.split('-').map(Number), day=n=>new Date(p[0],p[1]-1,p[2]+n);
      const f=x=>x.toLocaleDateString('en-US',{weekday:'short',month:'short',day:'numeric'});
      const k=val('q_k'), rows=PLAN[k], qz=QUIET[k];
      out('q_out','good', rows.map(r=>'<div style="margin:3px 0"><b>'+f(day(r[0]))+'</b> — '+r[1]+'</div>').join('')+
        '<div class="note" style="margin-top:8px"><b>Stay out of the hive '+f(day(qz[0]))+' to '+f(day(qz[1]))+'.</b> Jarring frames damages capped cells, and a virgin out on a mating flight can fail to find her way home.</div>');
    });
  }

  // --- Queen marking color
  function cColor(){
    const C=[{n:'Blue',h:'#3b7dd8'},{n:'White',h:'#f2f2ef'},{n:'Yellow',h:'#f3c53b'},{n:'Red',h:'#d64b3d'},{n:'Green',h:'#4c9a52'}];
    const y=new Date().getFullYear();
    body('<div class="card"><h3>👑 Queen marking color</h3>'+
      ci('Queen from year','k_y','type="number" inputmode="numeric" value="'+y+'"')+
      ci('Looking at her in','k_f','type="number" inputmode="numeric" value="'+y+'"')+
      '<div id="k_out" class="cout"></div>'+
      '<div class="note">Will You Rear Good Bees — white, yellow, red, green, blue for years ending 1·2·3·4·5, then repeating. Use a proper queen marking pen, one dot on the thorax, and let it dry before you release her.</div></div>');
    on(['k_y','k_f'], ()=>{
      const qy=num('k_y'), fy=num('k_f');
      if(!(qy>1900)||!(fy>1900)) return out('k_out','','Enter both years.');
      const c=C[qy%5], age=fy-qy;
      let msg,cls;
      if(age<0){ msg='That is a queen from the future — check the years.'; cls='mid'; }
      else if(age===0){ msg='This season&rsquo;s queen — first year, should be at her peak.'; cls='good'; }
      else if(age===1){ msg='One season on her. Her second year is usually her best laying year.'; cls='good'; }
      else if(age===2){ msg='Two seasons on her. Watch the brood pattern — this is where most beekeepers requeen.'; cls='mid'; }
      else { msg=age+' seasons on her. Well past her prime — expect a spotty pattern and swarm or supersedure pressure.'; cls='low'; }
      out('k_out',cls,'<span style="display:inline-block;width:22px;height:22px;border-radius:50%;background:'+c.h+
        ';border:2px solid rgba(0,0,0,.2);vertical-align:-5px"></span> <b>'+c.n+' dot</b>'+
        (age>=0?' · '+(age===0?'her first season':age+' season'+(age===1?'':'s')+' old'):'')+'<br>'+msg);
    });
  }

  // --- Pollen patty
  function cPatty(){
    body('<div class="card"><h3>🥞 Pollen patty scaler</h3>'+
      ci('Hives','p_h','type="number" inputmode="numeric" min="1" value="6"')+
      ci('Patties each','p_e','type="number" inputmode="numeric" min="1" value="1"')+
      cs('Patty weight','p_w','<option value="0.5">½ lb — nuc or light colony</option><option value="1" selected>1 lb</option><option value="1.5">1½ lb</option><option value="2">2 lb</option>')+
      ci('Dry sub, % by weight','p_d','type="number" inputmode="numeric" min="20" max="80" value="55"')+
      '<div id="p_out" class="cout"></div>'+
      '<div class="note">Mix dry first, then work the syrup in until it is like stiff cookie dough. Press between wax paper, ⅜ inch thick. Lay it right over the brood nest — they will not travel for it in cold weather. Beetles breed in patties, so keep them small if you have beetles.</div></div>');
    on(['p_h','p_e','p_w','p_d'], ()=>{
      const n=(num('p_h')||0)*(num('p_e')||0), total=n*parseFloat(val('p_w')), dry=total*((num('p_d')||55)/100);
      if(!(total>0)) return out('p_out','','Fill in the boxes above.');
      const syrup=total-dry, sug=syrup*(2/3), wat=syrup-sug;
      out('p_out','good','<b>'+total.toFixed(1)+' lb of mix</b> for '+n+' patt'+(n===1?'y':'ies')+':<br>'+
        '• <b>'+dry.toFixed(2)+' lb</b> dry protein substitute<br>'+
        '• <b>'+syrup.toFixed(2)+' lb</b> of 2:1 syrup — that is '+sug.toFixed(2)+' lb sugar and '+(wat*16).toFixed(1)+' oz water');
    });
  }

  // --- Mead
  function cMead(){
    body('<div class="card"><h3>🍶 Mead</h3>'+
      ci('Batch (gallons)','d_g','type="number" inputmode="decimal" min="0.5" step="0.5" value="5"')+
      ci('Target % ABV','d_a','type="number" inputmode="decimal" min="3" max="20" step="0.5" value="12"')+
      cs('Finish','d_f','<option value="1.000">Dry</option><option value="1.010" selected>Semi-sweet</option><option value="1.020">Sweet</option><option value="1.030">Dessert</option>')+
      '<div id="d_out" class="cout"></div>'+
      '<div class="note">Honey has almost no nitrogen — feed staggered nutrient over the first few days or it stalls and tastes hot. Do not boil the honey. Selling any of it needs federal TTB approval and a PA limited winery license.</div></div>');
    on(['d_g','d_a','d_f'], ()=>{
      const g=num('d_g'), a=num('d_a'), fg=parseFloat(val('d_f'));
      if(!(g>0)||!(a>0)) return out('d_out','','Enter a batch size and target strength.');
      const og=fg+a/131.25, lbs=(og-1)*1000/35*g, hg=lbs/11.85;
      out('d_out','good','<b>'+lbs.toFixed(1)+' lb of honey</b> for '+g+' gallons at '+a+'% ABV<br>'+
        'Starting gravity '+og.toFixed(3)+', finishing at '+fg.toFixed(3)+'.<br>'+
        'Top up with about <b>'+(g-hg).toFixed(2)+' gallons of water</b>.');
    });
  }

'''

with io.open(PATH, encoding="utf-8") as f:
    html = f.read()

i = html.index(START)
j = html.index(END)
html = html[:i] + NEW + html[j:]

# Home tile subtitle
html = html.replace(
    "{v:'calc',     ic:'🧮', nm:'Calculators', sub:'Mite wash & sugar syrup'},",
    "{v:'calc',     ic:'🧮', nm:'Calculators', sub:'10 field calculators'},")

# Chip styling for the calculator picker, added once next to the existing .cout rules.
CHIP_CSS = (".cchips{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0 4px}\n"
            ".cchip{background:#fff;border:1px solid var(--line);color:var(--muted);font-size:13px;"
            "font-weight:600;padding:7px 12px;border-radius:20px;cursor:pointer;font-family:inherit}\n"
            ".cchip.on{background:var(--amber);border-color:var(--amber);color:#241a05}\n")
if ".cchips{" not in html:
    anchor = ".cout.good{"
    html = html.replace(anchor, CHIP_CSS + anchor, 1)

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)

print("index.html: Calculators view replaced with %d calculators" % 10)
