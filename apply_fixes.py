import re, os

filepath = os.path.join(os.environ.get('TEMP', '/tmp'), 'florida-trip-2026', 'index.html')
print(f"Reading: {filepath}")
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
print(f"File size: {len(content)} chars")

# 1. REORDER TABS
content = content.replace("showSection('comparison',this)\">Comparativa</div>\n  <div class=\"tab\" onclick=\"showSection('naples',this)\">Naples (Base 1)",
                          "showSection('naples',this)\">Naples</div>\n  <div class=\"tab\" onclick=\"showSection('east',this)\">Costa Este</div>\n  <div class=\"tab\" onclick=\"showSection('comparison',this)\">Comparativa")
content = content.replace("onclick=\"showSection('east',this)\">Costa Este (Base 2)</div>\n  <div class=\"tab\" onclick=\"showSection('combos',this)\">Combos + Budget</div>\n  <div class=\"tab\" onclick=\"showSection('itinerary',this)\">Itinerario</div>\n  <div class=\"tab\" onclick=\"showSection('restaurants',this)\">Restaurantes</div>\n  <div class=\"tab\" onclick=\"showSection('towns',this)\">Pueblitos Lindos</div>\n  <div class=\"tab\" onclick=\"showSection('trivia',this)\">Trivia Game</div>\n  <div class=\"tab\" onclick=\"showSection('links',this)\">Links + Tips",
                          "onclick=\"showSection('restaurants',this)\">Restaurantes</div>\n  <div class=\"tab\" onclick=\"showSection('itinerary',this)\">Itinerario</div>\n  <div class=\"tab\" onclick=\"showSection('towns',this)\">Pueblitos</div>\n  <div class=\"tab\" onclick=\"showSection('combos',this)\">Budget</div>\n  <div class=\"tab\" onclick=\"showSection('trivia',this)\">Trivia</div>\n  <div class=\"tab\" onclick=\"showSection('links',this)\">Links")

content = content.replace('id="comparison" class="section active"', 'id="comparison" class="section"')
content = content.replace('id="naples" class="section">', 'id="naples" class="section active">')
print("1. Tabs reordered")

# 2. Replace photos
for old, new in {
    'upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Worth_Avenue_into_Via_Mizner_Palm_Beach_FL-1.jpg/600px-Worth_Avenue_into_Via_Mizner_Palm_Beach_FL-1.jpg': 'img/worth-avenue.jpg',
    'upload.wikimedia.org/wikipedia/commons/thumb/5/52/ClematisStWPB500block.JPG/600px-ClematisStWPB500block.JPG': 'img/clematis-street.png',
    'upload.wikimedia.org/wikipedia/commons/thumb/6/67/Lake_Worth_Beach_Street_Painting_Festival.jpg/600px-Lake_Worth_Beach_Street_Painting_Festival.jpg': 'img/lake-worth-beach.png',
    'upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Historic_Naples_FA.JPG/600px-Historic_Naples_FA.JPG': 'img/crayton-cove.png',
    'upload.wikimedia.org/wikipedia/commons/thumb/6/60/Naples_Florida_Historic_District_R01.jpg/600px-Naples_Florida_Historic_District_R01.jpg': 'img/3rd-street-south.png',
}.items():
    if old in content:
        content = content.replace(old, new)
        print(f"  Photo: ...{old[-30:]} -> {new}")
print("2. Photos updated")

# 3. Fix Giuseppe
content = content.replace('Giuseppe and the Lion</a> (italiano, family-friendly) o cocinar algo rico en la suite.',
    'Mediterrano</a> (<a href="https://www.opentable.com/r/mediterrano-naples" target="_blank" style="color:#22d3ee;">RESERVAR</a>) o <a href="https://resy.com/cities/naples-fl/venues/osteria-tulia" target="_blank">Osteria Tulia</a> (<a href="https://resy.com/cities/naples-fl/venues/osteria-tulia" target="_blank" style="color:#22d3ee;">RESERVAR</a>) o cocinar en la suite.')
content = content.replace('q=Giuseppe+and+the+Lion+Naples', 'r/mediterrano-naples')
content = content.replace('Giuseppe and the Lion</span><span class="detail"> - Naples, italiano', 'Mediterrano</span><span class="detail"> - Naples, mediterraneo')
print("3. Giuseppe -> Mediterrano")

# 4. Shell Museum
content = content.replace('Shell Museum</a> - interactivo, touch tanks. Genial para 9 y 11 anos.', 'Shell Museum</a> - Opcional, puede aburrir a chicos 9/11. Mas playa si no les copa.')
print("4. Shell Museum optional")

# 5. Worth Avenue guide
content = content.replace('<h3>Worth Avenue + Palm Beach Island</h3>', '<h3>Worth Avenue + Palm Beach <a href="https://www.luxurytravelmagazine.com/news-articles/worth-avenue-palm-beach-the-ultimate-guide" target="_blank" style="color:#a78bfa;font-size:0.7rem;">(Guia)</a></h3>')
print("5. Worth Ave guide")

# 6. Password gate
pw = '<script>document.addEventListener("DOMContentLoaded",function(){if(sessionStorage.getItem("fta")==="1"){var g=document.getElementById("password-gate");if(g)g.remove();document.body.classList.remove("locked");return;}document.body.classList.add("locked");});function checkPw(){var i=document.getElementById("gi");var e=document.getElementById("ge");if(i.value.replace(/\s/g,"").toLowerCase()==="florida2026"){sessionStorage.setItem("fta","1");document.getElementById("password-gate").remove();document.body.classList.remove("locked");}else{i.classList.add("error");e.style.display="block";setTimeout(function(){i.classList.remove("error");},500);}}</script><style>#password-gate{position:fixed;inset:0;z-index:9999;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#0c4a6e,#0f172a,#164e63);font-family:sans-serif}#password-gate .gb{background:#fff;border-radius:1.5rem;padding:3rem;max-width:420px;width:90%;box-shadow:0 25px 50px rgba(0,0,0,.3);text-align:center}#password-gate h1{color:#0c4a6e;font-size:1.5rem;font-weight:800;margin-bottom:.5rem}#password-gate p{color:#6b7280;font-size:.875rem;margin-bottom:1.5rem}#password-gate input{width:100%;padding:.75rem;border:2px solid #e5e7eb;border-radius:.75rem;font-size:1rem;text-align:center;outline:0}#password-gate input.error{border-color:#ef4444;animation:shake .5s}#password-gate button{margin-top:1rem;width:100%;padding:.75rem;background:#22d3ee;color:#0f172a;font-weight:700;border:0;border-radius:.75rem;font-size:1rem;cursor:pointer}#password-gate .em{color:#ef4444;font-size:.8rem;margin-top:.5rem;display:none}@keyframes shake{0%,100%{transform:translateX(0)}25%{transform:translateX(-8px)}75%{transform:translateX(8px)}}body.locked>*:not(#password-gate){display:none!important}</style>'
pw_html = '<div id="password-gate"><div class="gb"><h1>Florida Family Trip 2026</h1><p>Ingresa el password</p><input type="password" id="gi" placeholder="Password" onkeydown="if(event.key===\'Enter\')checkPw()"><button onclick="checkPw()">Entrar</button><div class="em" id="ge">Password incorrecto</div></div></div>'
content = content.replace('</title>', '</title>\n' + pw)
content = content.replace('<body>', '<body>\n' + pw_html)
print("6. Password gate")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("\nALL DONE!")
