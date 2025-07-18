const escortNames = ["Diana", "Jane", "Mary", "Susan", "Linda", "Rose",];

const vipAds = document.getElementById("vip-ads");
const generalAds = document.getElementById("general-ads");



const cardHTML = `
    <div class="image-wrapper">
      <img src="assets/images/escort.jpg" alt="Card Image" class="card-image">
    </div>
    <div class="transparent-details">
        <div class="escort-name">Diana</div>
        <div class="escort-location">Thika</div>
    </div>
    <div class="escort-phone">
      <span class="phone-icon"></span>
      <a href="tel:+254712345678" class="escort-phone">+254712345678</a>
    </div> 
    `

function createCard(){
  const card = document.createElement("div");
  card.classList.add("card");
  card.innerHTML = cardHTML;
  return card;
}


function insertVIPCards(escortNames) {
  const card = createCard();
  for (let escortName of escortNames) {
    const newCard = card.cloneNode(true);
    newCard.querySelector(".escort-name").textContent = escortName;
    vipAds.appendChild(newCard);
    
  }
}

function insertVerifiedCards(escortNames) {
  const card = createCard();
  const verifiedAds = document.getElementById("verified-ads");
  for (let escortName of escortNames) {
    const newCard = card.cloneNode(true);
    newCard.querySelector(".escort-name").textContent = escortName;
    verifiedAds.appendChild(newCard);
    
  }
}

function insertGeneralCards(escortNames) {
  const card = createCard();
  const generalAds = document.getElementById("general-ads");
  for (let escortName of escortNames) {
    const newCard = card.cloneNode(true);
    newCard.querySelector(".escort-name").textContent = escortName;
    generalAds.appendChild(newCard);
    
  }
}


// insertVIPCards(escortNames);
// insertVerifiedCards(escortNames);
// insertGeneralCards(escortNames);


const counties = [
  {"name": "nairobi", "towns": ["embakasi", "kilimani", "karen", "westlands", "langata", "nairobi central"]},
  {"name": "mombasa", "towns": ["likoni", "nyali", "changamwe", "kisauni", "mtongwe", "shanzu"]},
  {"name": "kisumu", "towns": ["milimani", "nyalenda", "kondele", "mamboleo", "dunga", "kibos"]},
  {"name": "nakuru", "towns": ["naivasha", "gilgil", "rongai", "njoro", "molo", "subukia"]},
  {"name": "kiambu", "towns": ["thika", "ruiru", "githunguri", "limuru", "kikuyu", "kiambu town"]},
  {"name": "machakos", "towns": ["kangundo", "mavoko", "masinga", "matungulu", "machakos town", "yatta"]},
  {"name": "nyeri", "towns": ["karatina", "othaya", "mukurweini", "nyeri town", "kieni", "tetu"]},
  {"name": "meru", "towns": ["timau", "maua", "nkubu", "meru town", "tigania", "igembe"]},
  {"name": "embu", "towns": ["runyenjes", "siakago", "embu town", "kiritiri", "manyatta", "mbeere"]},
  {"name": "kakamega", "towns": ["mumias", "butere", "shinyalu", "malava", "kakamega town", "navakholo"]},
  {"name": "bungoma", "towns": ["webuye", "kimilili", "chwele", "sirisia", "bungoma town", "mt elgon"]},
  {"name": "kisii", "towns": ["nyamache", "suneka", "kisii town", "masimba", "tabaka", "keumbu"]},
  {"name": "nyamira", "towns": ["nyamira town", "keroka", "ekerenyo", "magwagwa", "manga", "gesima"]},
  {"name": "kericho", "towns": ["litein", "kericho town", "sosiot", "kipkelion", "chepseon", "fort tenan"]},
  {"name": "bomet", "towns": ["bomet town", "sotik", "kaplong", "longisa", "silibwet", "chebole"]},
  {"name": "narok", "towns": ["narok town", "kilgoris", "lolgorien", "suswa", "entasekera", "ololulung'a"]},
  {"name": "kajiado", "towns": ["kajiado town", "ngong", "kitengela", "isinya", "loitokitok", "namanga"]},
  {"name": "laikipia", "towns": ["nyahururu", "nanyuki", "rumuruti", "kinamba", "sipili", "wiyumiririe"]},
  {"name": "nyandarua", "towns": ["ol kalou", "njabini", "engineer", "mirangine", "kipipiri", "shamata"]},
  {"name": "murang'a", "towns": ["murang'a town", "kangema", "kandara", "kenol", "maragua", "kiria-ini"]},
  {"name": "tharaka nithi", "towns": ["chuka", "marimanti", "gatunga", "muthambi", "kathwana", "chiakariga"]},
  {"name": "kitui", "towns": ["kitui town", "mwingi", "mutomo", "kyuso", "ikutha", "kabati"]},
  {"name": "makueni", "towns": ["wote", "mtito andei", "makindu", "kibwezi", "sultan hamud", "kathonzweni"]},
  {"name": "taita taveta", "towns": ["voi", "taveta", "wundanyi", "mwatate", "maungu", "ndii"]},
  {"name": "kwale", "towns": ["ukunda", "diani", "kwale town", "kinango", "lunga lunga", "shimba hills"]},
  {"name": "kilifi", "towns": ["malindi", "kilifi town", "watamu", "mtwapa", "kaloleni", "gongoni"]},
  {"name": "lamu", "towns": ["lamu town", "mpeketoni", "kiunga", "faza", "shela", "matondoni"]},
  {"name": "tana river", "towns": ["hola", "bura", "garsen", "madogo", "wenje", "kipini"]},
  {"name": "garissa", "towns": ["garissa town", "dadaab", "masalani", "hulugho", "modogashe", "balambala"]},
  {"name": "wajir", "towns": ["wajir town", "griftu", "habaswein", "eldas", "tarbaj", "bute"]},
  {"name": "mandera", "towns": ["mandera town", "elwak", "lafey", "takaba", "banisa", "rhamu"]},
  {"name": "marsabit", "towns": ["marsabit town", "moyale", "sololo", "loiyangalani", "north horr", "laisamis"]},
  {"name": "isiolo", "towns": ["isiolo town", "garbatulla", "kina", "merti", "kipsing", "oldonyiro"]},
  {"name": "samburu", "towns": ["maralal", "baragoi", "archers post", "wamba", "lodokejek", "south horr"]},
  {"name": "turkana", "towns": ["lodwar", "kalokol", "lokichoggio", "kakuma", "lokitaung", "lorugum"]},
  {"name": "west pokot", "towns": ["kapenguria", "chepareria", "ortum", "lomut", "sigor", "alale"]},
  {"name": "elgeyo marakwet", "towns": ["itens", "kapsowar", "chebiemit", "tambach", "chesoi", "kapcherop"]},
  {"name": "nandi", "towns": ["kapsabet", "nandi hills", "mosoriot", "kabiyet", "chepterit", "lessos"]},
  {"name": "uasin gishu", "towns": ["eldoret", "moiben", "ziwa", "kesses", "turbo", "kapseret"]},
  {"name": "trans nzoia", "towns": ["kitale", "kiminini", "endebess", "cherangany", "saboti", "kesogon"]},
  {"name": "bungoma", "towns": ["bungoma town", "webuye", "kimilili", "chwele", "sirisia", "mt elgon"]},
  {"name": "busia", "towns": ["busia town", "malaba", "nambale", "butula", "funyula", "port victoria"]},
  {"name": "siaya", "towns": ["siaya town", "bondo", "ugenya", "gem", "rarieda", "alego usonga"]},
  {"name": "homabay", "towns": ["homabay town", "mbita", "kendu bay", "oyugis", "rangwe", "ndhiwa"]},
  {"name": "migori", "towns": ["migori town", "awendo", "rongo", "kuria", "nyatike", "uriri"]},
  {"name": "vihiga", "towns": ["mbale", "luanda", "hamisi", "sabatia", "emuhaya", "tiriki"]},
  {"name": "tharaka nithi", "towns": ["chuka", "marimanti", "gatunga", "muthambi", "kathwana", "chiakariga"]}
]

const caretSVG = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512" class="caret" color="white" fill="#f799d6">
    <!--!Font Awesome Free 6.6.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.-->
    <path d="M137.4 374.6c12.5 12.5 32.8 12.5 45.3 0l128-128c9.2-9.2 11.9-22.9 6.9-34.9s-16.6-19.8-29.6-19.8L32 192c-12.9 0-24.6 7.8-29.6 19.8s-2.2 25.7 6.9 34.9l128 128z"/></svg>`

const heartSVG = `<svg width="18" height="24" viewBox="0 0 24 24" fill="#f799d6" xmlns="http://www.w3.org/2000/svg" class="caret">
<path d="M12 21.35L10.55 20.03C5.4 15.36 2 12.28 2 8.5C2 5.41 4.42 3 7.5 3C9.24 3 10.91 3.79 12 5.05C13.09 3.79 14.76 3 16.5 3C19.58 3 22 5.41 22 8.5C22 12.28 18.6 15.36 13.45 20.03L12 21.35Z"/>
</svg>`


const countiesContainer = document.getElementById('counties');

counties.forEach(county => {
    const countyElement = document.createElement('div');
    countyElement.classList.add('county');
    countyElement.innerHTML = `
        <div class="county-name">
            ${county.name.charAt(0).toUpperCase() + county.name.slice(1)}
            ${heartSVG}
        </div>
        <ul class="towns" style="display: none;">
            ${county.towns.map(town => `<li class="town">${town.charAt(0).toUpperCase() + town.slice(1)}</li>`).join('')}
        </ul>
    `;
    countiesContainer.appendChild(countyElement);
});
