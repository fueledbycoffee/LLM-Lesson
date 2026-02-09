# Checklist Formateur — IA, Chatbots & Marketing

## Avant le cours

- [ ] Open WebUI fonctionne, comptes etudiants crees
- [ ] Slides servies : `python3 scripts/serve.py` → http://localhost:8000
- [ ] Verifier le projecteur / partage ecran
- [ ] Imprimer les 4 briefs scenario (1 par groupe)
- [ ] Imprimer la checklist Red Team (1 par groupe)
- [ ] Prevoir les groupes (4 groupes de 4-5)
- [ ] Preparer un chatbot demo "sans garde-fous" + un "avec garde-fous" dans Open WebUI
- [ ] Verifier les acces wifi / reseau pour tous

## Matin — 9h30-12h30

### 9h30-9h45 — Intro + objectifs (slides 1-3)
- [ ] Se presenter, tour de table rapide (prenom + attentes en 1 mot)
- [ ] Presenter le programme + les livrables attendus a 18h
- [ ] Poser la question : "Qui a deja utilise ChatGPT ?"

### 9h45-10h30 — IA & LLM : kezako ? (slides 4-10)
- [ ] Chatbot = produit (perimetre, valeur, risques, KPI)
- [ ] 3 familles de chatbots (regles / LLM / agents)
- [ ] C'est quoi un LLM : Large, Language, Model
- [ ] Comment il apprend (milliards de textes → patterns)
- [ ] Un mot a la fois (auto-complete surpuissant)
- [ ] Il ne reflechit pas (pattern matching, pas de raisonnement)
- [ ] Pas de conscience (pas de memoire, pas d'intention)
- [ ] Verifier la comprehension : "Des questions ?"

### 10h30-11h00 — Hallucinations + Demo + Chaine de valeur (slides 11-14)
- [ ] Hallucinations : pourquoi + 4 leviers
- [ ] DEMO LIVE : meme question, sans puis avec garde-fous
- [ ] Chaine de valeur marketing x IA (acquisition → advocacy)
- [ ] 1 exemple concret par etape

### 11h00-11h10 — Pause (slide 15)
- [ ] Rappeler : on reprend a 11h10

### 11h10-11h50 — Architecture chatbot (slides 16-18)
- [ ] Schema : Canal → Orchestrateur → LLM + Contexte → CRM → Humain
- [ ] Les donnees qui alimentent le bot (FAQ, catalogue, regles)
- [ ] CRM-ready : chaque conversation = donnees exploitables
- [ ] Montrer un exemple de Note CRM

### 11h50-12h25 — Atelier Chatbot Canvas (slide 19)
- [ ] Distribuer le template (ou afficher via TP panel)
- [ ] Groupes de 4-5, 35 minutes
- [ ] Circuler entre les groupes, debloquer
- [ ] S'assurer que les 6 blocs sont remplis (persona, intents, ton, donnees, escalade, KPI)

### 12h25-12h30 — Brief apres-midi (slide 20)
- [ ] Assigner les scenarios (1 par groupe)
- [ ] Distribuer les briefs imprimes
- [ ] Rappeler les livrables attendus a 18h
- [ ] "Bon appetit, on se retrouve a 14h"

## Apres-midi — 14h-18h

### 14h00-14h15 — Prise en main Open WebUI (slides 1-3)
- [ ] Demo rapide : ou mettre le prompt systeme, le contexte
- [ ] Astuce : 2 fenetres (config + test client)
- [ ] Grille d'evaluation : precision, ton, questions, format CRM
- [ ] S'assurer que tous les groupes ont acces

### 14h15-15h05 — Atelier 1 : Prompting PO (slides 4-5)
- [ ] 50 minutes
- [ ] Objectif : prompt systeme + script accueil + format Note CRM
- [ ] Montrer l'exemple de prompt systeme (slide 5)
- [ ] Circuler : verifier que le prompt a les 5 blocs (role, ton, perimetre, regles, escalade)
- [ ] Challenger : "Que se passe-t-il si je demande un prix ?"

### 15h05-15h15 — Pause (slide 6)

### 15h15-16h25 — Atelier 2 : Chatbot complet (slide 7)
- [ ] 70 minutes — le gros morceau
- [ ] Objectif : flow complet + version client/interne + plan de mesure
- [ ] Verifier que chaque groupe teste au moins 3 scenarios
- [ ] S'assurer que la Note CRM est structuree (pas un paragraphe)
- [ ] Alerter a 16h00 : "Plus que 25 minutes"

### 16h25-17h05 — Atelier 3 : Red Team croisee (slides 8-9)
- [ ] 40 minutes
- [ ] Rotation : chaque groupe teste le bot d'un AUTRE groupe
- [ ] Distribuer/afficher la checklist Red Team (6 categories)
- [ ] Rappeler : 3 failles + 3 correctifs
- [ ] Ambiance constructive mais exigeante

### 17h05-17h25 — Fix & amelioration (slide 10)
- [ ] 20 minutes
- [ ] Chaque groupe corrige ses failles
- [ ] Stabiliser le format CRM
- [ ] Preparer les 2 echanges de demo pour le pitch

### 17h25-18h00 — Pitch final (slides 11-14)
- [ ] Format : 3 min pitch + 2 min Q&A par groupe
- [ ] Timer visible
- [ ] Grille de scoring /20 (use case /4, prompt /4, demo /4, CRM /4, garde-fous /4)
- [ ] Poser au moins 1 question par groupe
- [ ] Annoncer les resultats
- [ ] Slide "Bravo & merci" — recap des acquis

## Materiels a preparer

| Quoi | Quantite | Format |
|------|----------|--------|
| Briefs scenario | 4 (1/groupe) | Papier A4 |
| Checklist Red Team | 4 (1/groupe) | Papier A4 |
| Comptes Open WebUI | 1 par groupe | Numerique |
| Chatbot demo "sans garde-fous" | 1 | Open WebUI |
| Chatbot demo "avec garde-fous" | 1 | Open WebUI |
| Timer (pitch) | 1 | Telephone / en ligne |
| Grille de scoring | 1 | Papier ou numerique |

## Apres le cours

- [ ] Collecter les prompts systeme des groupes (capitalisation)
- [ ] Envoyer un recap par email (slides + briefs + ressources)
- [ ] Noter les points a ameliorer pour la prochaine session
