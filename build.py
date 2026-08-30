#!/usr/bin/env python3
"""Génère les pages HTML du portfolio à partir du tableau APPS.

Usage : python3 build.py
Produit : index.html, sur-moi.html, contact.html, apps/*.html
"""

import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# Incrémenter à chaque modification de css/style.css pour invalider le cache
# (GitHub Pages sert le CSS avec max-age=600).
CSS_VERSION = "3"

# ---------------------------------------------------------------------------
# Données centrales — une entrée par app, dans l'ordre du carrousel.
# Les chemins d'images sont relatifs à la racine du site (img/...).
# ---------------------------------------------------------------------------

APPS = [
    {
        "slug": "hypetogo",
        "name": "HypeToGo",
        "tagline": "Tous les événements de Paris",
        "accent": "#6C4CF0",
        "category": "Sorties · Événements · 2026",
        "year": "2026",
        "ecran": "img/hypetogo_ecran.png",
        "desc": "HypeToGo regroupe les événements de Paris intra-muros : concerts, expos, soirées, spectacles… Explorez par liste ou par carte autour de vous, gardez vos favoris et organisez vos sorties dans un planning présenté en timeline, avec notifications pour ne rien rater.",
        "features": [
            "Événements Paris intra-muros",
            "Exploration liste & carte autour de soi",
            "Favoris et planning en timeline",
            "Badges Ce soir / Demain",
            "Notifications",
            "Sources officielles agrégées",
        ],
        "stack": ["React Native", "Expo", "TypeScript", "Expo Router", "Zustand", "Supabase", "Cartographie"],
        "gallery": [
            "img/Hypetogo_Acceuil.jpg",
            "img/Hypetogo1.jpg",
            "img/Hypetogo3.jpg",
            "img/Hypetogo5.jpg",
            "img/Hypetogo4.jpg",
        ],
        "store_id": "id6772987346",
    },
    {
        "slug": "grimoa",
        "name": "Grimoa",
        "tagline": "Le patrimoine français autour de vous",
        "accent": "#5B3A6E",
        "category": "Voyage · Culture · 2026",
        "year": "2026",
        "ecran": "img/grimoa_ecran.png",
        "desc": "Grimoa révèle le patrimoine français qui vous entoure : 208 380 lieux (monuments historiques mais aussi lavoirs, croix, menhirs et curiosités locales) affichés sur une carte. Validez vos visites sur place par géolocalisation, collectionnez des badges et remplissez la carte de France département par département.",
        "features": [
            "208 380 lieux référencés",
            "Validation des visites par géolocalisation (< 100 m)",
            "Collection de badges",
            "Carte de France à compléter",
            "Monuments historiques & curiosités locales",
            "100% gratuit, local, sans compte",
        ],
        "stack": ["React Native", "Expo", "TypeScript", "Expo Router", "Zustand", "Cartographie", "Géolocalisation"],
        "gallery": [
            "img/grimoa_Accueil.jpg",
            "img/grimoa-02-fiche.jpg",
            "img/grimoa-03-collection.png",
            "img/grimoa-04-badges.png",
            "img/grimoa-05-journal.jpg",
        ],
        "store_id": "id6793055341",
    },
    {
        "slug": "geodex",
        "name": "Geodex",
        "tagline": "La géographie du monde, hors-ligne",
        "accent": "#1F5FA8",
        "category": "Éducation · Quiz · 2025",
        "year": "2025",
        "ecran": "img/geodex_ecran.png",
        "desc": "Geodex est une app de géographie entièrement hors-ligne, pensée comme un atlas de luxe : explorez le monde sur un globe 3D interactif, testez vos connaissances avec des quiz de placement à plusieurs niveaux de difficulté, et parcourez des fiches pays riches. Tout est embarqué, aucune connexion nécessaire.",
        "features": [
            "Globe 3D interactif",
            "Quiz : pays, capitales, drapeaux, mers",
            "4 niveaux de difficulté",
            "Fiches pays riches (195 pays)",
            "100% hors-ligne, sans compte",
            "Progression et badges",
        ],
        "stack": ["React Native", "Expo", "TypeScript", "Expo Router", "Zustand", "Rendu de globe (d3-geo, TopoJSON)", "RevenueCat"],
        "gallery": [
            "img/Geodex_Accueil.jpg",
            "img/Geodex_modes.jpg",
            "img/Geodex_quiz.jpg",
            "img/geodex_collection.jpg",
            "img/Geodex_profil.jpg",
        ],
        "store_id": "id6779577722",
    },
    {
        "slug": "retour",
        "name": "Retour",
        "tagline": "Le rituel du retour de voyage",
        "accent": "#2B2B2B",
        "category": "Lifestyle · Réflexion · 2026",
        "year": "2026",
        "ecran": "img/retour_ecran.png",
        "desc": "Retour est une app mono-usage au concept unique : elle détecte automatiquement votre retour de voyage et ouvre alors une fenêtre de 24 heures pour poser vos impressions à chaud, avant que le quotidien ne reprenne. Un rituel silencieux, minimaliste, qui transforme chaque voyage en souvenir écrit.",
        "features": [
            "Détection automatique du retour de voyage",
            "Fenêtre de réflexion de 24 heures",
            "Rituel d'écriture guidé",
            "Design silencieux et minimaliste",
            "Souvenirs accumulés voyage après voyage",
        ],
        "stack": ["React Native", "Expo", "TypeScript", "Expo Router", "Zustand", "PocketBase (self-hosted)", "Géolocalisation"],
        "gallery": [
            "img/retour_Accueil.png",
            "img/retour2.png",
            "img/retour3.png",
            "img/retour4.png",
            "img/retour5.png",
        ],
        "store_id": "id6776993896",
    },
    {
        "slug": "monkawa",
        "name": "Mon Kawa",
        "tagline": "Votre compagnon café du quotidien",
        "accent": "#B4633A",
        "category": "Lifestyle · Food · 2026",
        "year": "2026",
        "ecran": "img/monkawa_ecran.png",
        "desc": "Mon Kawa aide les amateurs de café à mieux préparer, suivre et déguster : un coach de préparation étape par étape avec timer, un carnet de cafés avec photos et notes, un suivi de fraîcheur des paquets et des statistiques de palais. 100% local : zéro compte, zéro pub, zéro backend.",
        "features": [
            "Coach de préparation avec timer étape par étape",
            "Ajustements itératifs des recettes",
            "Carnet de cafés avec photos & notes",
            "Suivi de fraîcheur (Frais / À finir / Fatigué)",
            "Statistiques de palais",
            "Aucun compte, aucune pub",
        ],
        "stack": ["React Native", "Expo", "TypeScript", "Expo Router", "Zustand", "AsyncStorage"],
        "gallery": [
            "img/kawa_Accueil.png",
            "img/kawa-2.png",
            "img/kawa-3.png",
            "img/kawa-4.png",
            "img/kawa-5.png",
        ],
        "store_id": "id6789859509",
    },
    {
        "slug": "microcotiz",
        "name": "MicroCotiz",
        "tagline": "Le compagnon des auto-entrepreneurs",
        "accent": "#3A665B",
        "category": "Finance · Productivité · 2026",
        "year": "2026",
        "ecran": "img/microcotiz_ecran.png",
        "desc": "MicroCotiz accompagne les auto-entrepreneurs au quotidien : saisie du chiffre d'affaires, livre des recettes, jauges des seuils micro et TVA en temps réel, simulation des cotisations URSSAF et rappels des échéances de déclaration. L'app fonctionne entièrement hors-ligne, sans compte, et embarque les barèmes officiels à jour.",
        "features": [
            "Suivi du CA et livre des recettes",
            "Jauges seuils micro & TVA en temps réel",
            "Simulateur de cotisations URSSAF",
            "Rappels des échéances de déclaration",
            "Export PDF du livre des recettes (Pro)",
            "Astuces & économies méconnues (ACRE…)",
        ],
        "stack": ["React Native", "Expo", "TypeScript", "Expo Router", "Zustand", "RevenueCat", "Notifications locales"],
        "gallery": [
            "img/Microcotiz_Accueil.jpg",
            "img/Microcotizsaisie-appstore.jpg",
            "img/Microcotizdeclaration-guidee-appstore.jpg",
            "img/Microcotizdeclarations-appstore.jpg",
            "img/Microcotizfiche-conseil-appstore.jpg",
        ],
        "store_id": "id6793455032",
    },
    {
        "slug": "dimanche",
        "name": "Dimanche",
        "tagline": "L'app qui n'ouvre que le dimanche soir",
        "accent": "#17151C",
        "category": "Lifestyle · Réflexion · 2026",
        "year": "2026",
        "ecran": "img/dimanche_ecran.png",
        "desc": "Dimanche est une app mono-usage au concept radical : elle ne s'ouvre que le dimanche, de 18h à 22h. Trois questions par semaine (ce que vous voulez retenir, ce que vous avez laissé filer, ce que vous voulez planter), et vos réponses s'accumulent sur 52 semaines pour former le livre de votre année.",
        "features": [
            "Ouverte uniquement le dimanche 18h–22h",
            "3 questions de réflexion par semaine",
            "52 semaines de réponses accumulées",
            "Votre année transformée en livre",
            "Design sombre, silencieux, sans distraction",
        ],
        "stack": ["React Native", "Expo", "TypeScript", "Expo Router", "Zustand", "PocketBase (self-hosted)", "Notifications"],
        "gallery": [
            "img/dimanche_Accueil.png",
            "img/dimanche-cap-2.png",
            "img/dimanche-cap-3.png",
            "img/dimanche-cap-4.png",
            "img/dimanche-cap-5.png",
        ],
        "store_id": "id6775904530",
    },
    {
        "slug": "risqcheck",
        "name": "RisqCheck",
        "tagline": "Les risques naturels de votre adresse",
        "accent": "#2D5A3D",
        "category": "Utilitaire · Immobilier · 2026",
        "year": "2026",
        "ecran": "img/risqcheck_ecran.png",
        "desc": "RisqCheck établit un diagnostic complet des risques naturels et technologiques pour n'importe quelle adresse en France : inondation, retrait-gonflement des argiles, séismes, radon, sites industriels… Le tout à partir des données publiques officielles Géorisques, présenté simplement et lisiblement.",
        "features": [
            "18 risques analysés par adresse",
            "Données officielles Géorisques",
            "Historique des catastrophes naturelles (CatNat)",
            "Analyse argile au niveau de la parcelle",
            "Comparateur d'adresses",
            "Fonctionne sans compte",
        ],
        "stack": ["React Native", "Expo", "TypeScript", "Expo Router", "Zustand", "API Géorisques", "RevenueCat"],
        "gallery": [
            "img/Risqcheck_Accueil.png",
            "img/Risqcheckdiagnostic.jpg",
            "img/Risqcheckcomparateur.jpg",
            "img/Risqcheckdroits-catnat.jpg",
        ],
        "store_id": "id6790358442",
    },
]


# ---------------------------------------------------------------------------
# Blocs communs
# ---------------------------------------------------------------------------

def head(title, description, root=""):
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" type="image/png" sizes="32x32" href="{root}favicon.png">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,300..800&family=Inter:wght@400;500&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}css/style.css?v={CSS_VERSION}">
</head>
<body>"""


def header(active, root="", onepage=False):
    if onepage:
        links = [
            ("Projets", "#projets"),
            ("Sur moi", "#sur-moi"),
            ("Contact", "#contact"),
        ]
    else:
        links = [
            ("Projets", f"{root}index.html"),
            ("Sur moi", f"{root}index.html#sur-moi"),
            ("Contact", f"{root}index.html#contact"),
        ]
    active_attr = ' class="active"'
    nav = "\n".join(
        f'    <a href="{href}"{active_attr if label == active else ""}>{label}</a>'
        for label, href in links
    )
    return f"""<header>
  <a class="logo" href="{root}index.html">Portfolio</a>
  <div class="status mono"><span class="dot"></span>Disponible · 2026</div>
  <nav>
{nav}
  </nav>
</header>"""


def phone(app, indent, root=""):
    return (
        f'{indent}<div class="phone">\n'
        f'  <div class="screen"><img class="shot" src="{root}{app["ecran"]}" alt="Écran d\'accueil de {app["name"]}"></div>\n'
        f'</div>'
    )


# ---------------------------------------------------------------------------
# Pages
# ---------------------------------------------------------------------------

def section_projets():
    cards = []
    for app in APPS:
        cards.append(
            f'<a class="card" href="apps/{app["slug"]}.html" aria-label="{app["name"]}">\n'
            f'  <span class="apptitle">{app["name"]}</span>\n'
            f'{phone(app, "  ")}\n'
            f'  <span class="tag">{app["tagline"]}</span>\n'
            f'</a>'
        )
    dashes = "".join(f'<button aria-label="Aller à {app["name"]}"></button>' for app in APPS)
    return f"""<section id="projets">
<div id="stage">
  <div class="rail" id="rail" aria-label="Mes applications">
{chr(10).join(cards)}
  </div>
</div>
<div class="bottombar">
  <div class="who">Tom Soghomonian<br><em>Développeur d'apps</em></div>
  <div class="dashes" id="dashes">{dashes}</div>
  <div id="currentName">{APPS[0]["name"]}</div>
</div>
</section>"""


def section_surmoi():
    applist = "".join(
        f'<a href="apps/{app["slug"]}.html" style="--c:{app["accent"]}">{app["name"]}<i></i></a>'
        for app in APPS
    )
    return f"""<section class="page" id="sur-moi">
  <span class="mono" style="color:var(--muted)">Sur moi</span>
  <h1 class="giant">Tom<br>Soghomonian</h1>
  <p class="big" style="margin-top:30px">Développeur iOS indépendant de <span id="age">32</span> ans, basé à Paris. Je conçois, développe et publie mes propres applications de A à Z : de l'idée au design, du code jusqu'à l'App Store.</p>
  <div class="facts">
    <div><strong>{len(APPS)}</strong><span>apps développées</span></div>
    <div><strong>iOS</strong><span>React Native · Expo · TypeScript</span></div>
    <div><strong>Solo</strong><span>design, dev, publication</span></div>
  </div>
  <span class="mono sec-title">Mon parcours</span>
  <p class="desc">Formé au web design (BTS), je me suis ensuite spécialisé en développement mobile en autodidacte. Aujourd'hui je construis des apps iOS complètes en solo : chaque projet part d'une idée simple, passe par le design, le développement, les tests, puis la publication et le suivi sur l'App Store. Micro-entrepreneur, je gère aussi tout le reste : fiches store, sites vitrines, marketing, support.</p>
  <span class="mono sec-title">Ma façon de travailler</span>
  <p class="desc">Je crois aux apps qui font une chose, et qui la font bien : des interfaces épurées, sans compte quand c'est possible, sans pub, respectueuses des données. Ma stack est la même sur tous mes projets (React Native, Expo, TypeScript), ce qui me permet d'aller vite de l'idée au store. Certaines de mes apps tournent sur mon propre backend auto-hébergé.</p>
  <span class="mono sec-title">Et aussi</span>
  <p class="desc">Je suis disponible pour développer votre application : particulier, indépendant ou petite entreprise, je prends en charge le projet de A à Z, du cahier des charges à la mise en ligne. <a href="#contact" style="border-bottom:2px solid var(--line)">Contactez-moi</a>.</p>
  <span class="mono sec-title">Mes apps</span>
  <div class="applist">{applist}</div>
</section>"""


def section_contact():
    return """<section class="page" id="contact">
  <span class="mono" style="color:var(--muted)">Contact</span>
  <h1 class="giant">Parlons-en</h1>
  <p class="big" style="margin-top:30px">Un projet d'app, une question, une collaboration ? Écrivez-moi.</p>
  <div class="contactlinks">
    <a href="mailto:soghomoniantom@gmail.com">soghomoniantom@gmail.com</a>
    <a href="https://github.com/Paprika92" target="_blank" rel="noopener">github.com/Paprika92</a>
    <a href="https://www.malt.fr/profile/tomsoghomoniantom" target="_blank" rel="noopener">malt.fr · freelance</a>
    <a href="https://www.codeur.com/-tomsogho" target="_blank" rel="noopener">codeur.com · freelance</a>
  </div>
  <p class="mono" style="color:var(--muted);margin-top:40px">Basé à Paris · Réponse sous 24h</p>
</section>"""


def build_index():
    names = ", ".join(f"'{app['name']}'" for app in APPS)
    return head(
        "Portfolio · Tom Soghomonian, développeur d'apps",
        "Portfolio de Tom Soghomonian, développeur d'apps iOS indépendant. 8 applications publiées.",
    ) + "\n" + header("Projets", onepage=True) + f"""
<main>
{section_projets()}
{section_surmoi()}
{section_contact()}
</main>
<script>
const NAMES = [{names}];
""" + """const rail = document.getElementById('rail');
const dashes = document.getElementById('dashes');
const currentName = document.getElementById('currentName');
[...dashes.children].forEach((b,i)=>b.addEventListener('click',()=>{
  rail.children[i].scrollIntoView({behavior:'smooth', inline:'center', block:'nearest'});
}));
function syncActive(){
  const mid = rail.scrollLeft + rail.clientWidth/2;
  let best=0, bd=Infinity;
  [...rail.children].forEach((el,i)=>{
    const c = el.offsetLeft + el.offsetWidth/2;
    const d = Math.abs(c-mid);
    if(d<bd){bd=d;best=i;}
  });
  currentName.textContent = NAMES[best];
  [...dashes.children].forEach((el,i)=>el.classList.toggle('on', i===best));
}
rail.addEventListener('scroll', ()=>requestAnimationFrame(syncActive), {passive:true});
window.addEventListener('resize', syncActive);
syncActive();
document.getElementById('age').textContent = (function(){
  const b = new Date(1994, 1, 16); // 16 février 1994
  const n = new Date();
  let a = n.getFullYear() - b.getFullYear();
  if (n.getMonth() < 1 || (n.getMonth() === 1 && n.getDate() < 16)) a--;
  return a;
})();
</script>
</body>
</html>"""


def build_redirect(anchor, title):
    url = f"index.html#{anchor}"
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="refresh" content="0; url={url}">
<title>{title}</title>
<meta name="robots" content="noindex">
<link rel="canonical" href="https://paprika92.github.io/{url}">
<script>location.replace('{url}');</script>
</head>
<body>
<p><a href="{url}">Cette page a déménagé : cliquez ici si la redirection ne se fait pas.</a></p>
</body>
</html>"""


def build_app(i):
    app = APPS[i]
    prev_app = APPS[(i - 1) % len(APPS)]
    next_app = APPS[(i + 1) % len(APPS)]
    feat = "".join(f"<li>{f}</li>" for f in app["features"])
    stack = "".join(f"<span>{s}</span>" for s in app["stack"])
    gallery = "".join(
        f'<div class="shot"><img src="../{src}" alt="Capture {app["name"]}" loading="lazy"></div>'
        for src in app["gallery"]
    )
    return head(
        f'{app["name"]} · Portfolio',
        app["tagline"],
        root="../",
    ) + "\n" + header("Projets", root="../") + f"""
<main class="page" style="--accent:{app["accent"]}">
  <a class="crumb mono" href="../index.html">← Projets</a>
  <div class="hero-app">
    <div>
      <span class="mono" style="color:{app["accent"]}">{app["category"]}</span>
      <h1 class="giant">{app["name"]}</h1>
      <p class="tagline">{app["tagline"]}</p>
    </div>
{phone(app, "    ", root="../")}
  </div>
  <div class="meta">
    <div><span>Plateforme</span><b>iOS</b></div>
    <div><span>Rôle</span><b>Design & développement</b></div>
    <div><span>Année</span><b>{app["year"]}</b></div>
    <div><span>Statut</span><b>Sur l'App Store</b></div>
  </div>
  <span class="mono sec-title">L'app</span>
  <p class="desc">{app["desc"]}</p>
  <span class="mono sec-title">Ce qu'elle fait</span>
  <ul class="feat">{feat}</ul>
  <span class="mono sec-title">Outils utilisés</span>
  <div class="stack">{stack}</div>
  <span class="mono sec-title">Captures</span>
  <div class="gallery">{gallery}</div>
  <a class="store" href="https://apps.apple.com/fr/app/{app["store_id"]}" target="_blank" rel="noopener">Voir sur l'App Store ↗</a>
  <div class="pagenav">
    <a href="{prev_app["slug"]}.html">← {prev_app["name"]}</a>
    <a href="{next_app["slug"]}.html">{next_app["name"]} →</a>
  </div>
</main>

</body>
</html>"""


# ---------------------------------------------------------------------------
# Écriture
# ---------------------------------------------------------------------------

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="") as f:
        f.write(content)
    print(f"  {path}")


def main():
    print("Build :")
    write("index.html", build_index())
    write("sur-moi.html", build_redirect("sur-moi", "Sur moi · Tom Soghomonian"))
    write("contact.html", build_redirect("contact", "Contact · Tom Soghomonian"))
    for i, app in enumerate(APPS):
        write(f"apps/{app['slug']}.html", build_app(i))
    print(f"OK — {3 + len(APPS)} fichiers générés.")


if __name__ == "__main__":
    main()
