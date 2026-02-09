# Checklist Formateur — IA & Chatbot

## Avant le cours

- [ ] Open WebUI fonctionne, comptes étudiants créés
- [ ] Slides servies : `python3 scripts/serve.py` → http://localhost:8000
- [ ] Vérifier le projecteur / partage écran
- [ ] Imprimer les 4 briefs scenario (1 par groupe)
- [ ] Imprimer la checklist Red Team (1 par groupe)
- [ ] Prévoir les groupes (4 groupes de 4-5)
- [ ] Préparer un chatbot démo "sans garde-fous" + un "avec garde-fous" dans Open WebUI
- [ ] Vérifier les accès wifi / réseau pour tous

## Matin — 9h30-12h30

### 9h30-9h45 — Intro + objectifs (hero + programme + objectifs)
- [ ] Se présenter, tour de table rapide (prénom + attentes en 1 mot)
- [ ] Présenter le programme + les livrables attendus à 18h
- [ ] Poser la question : "Qui a déjà utilisé ChatGPT ?"

### 9h45-10h30 — IA & LLM : kezako ? (fondations + modèle mental)
- [ ] Chatbot = produit (périmètre, valeur, risques, KPI)
- [ ] 3 familles de chatbots (règles / LLM / agents)
- [ ] C'est quoi un LLM : Large, Language, Model
- [ ] Comment il apprend (milliards de textes → patterns)
- [ ] Un mot à la fois (auto-complete surpuissant)
- [ ] Il ne réfléchit pas (pattern matching, pas de raisonnement)
- [ ] Pas de conscience (pas de mémoire, pas d'intention)
- [ ] Panorama modèles : fermés vs open-weight + critères de choix
- [ ] OpenRouter (aujourd'hui) : routeur multi-modèles (1 minute, pas plus)
- [ ] Démo : My First Chatbot (5-10 min)
- [ ] Vérifier la compréhension : "Des questions ?"

### 10h30-11h00 — Hallucinations + Démo + Chaîne de valeur
- [ ] Hallucinations : pourquoi + 4 leviers
- [ ] DÉMO LIVE : même question, sans puis avec garde-fous
- [ ] Chaîne de valeur marketing x IA (acquisition → advocacy)
- [ ] 1 exemple concret par étape

### 11h00-11h10 — Pause
- [ ] Rappeler : on reprend à 11h10

### 11h10-11h50 — Architecture chatbot (canal → orchestrateur → LLM)
- [ ] Schéma : Canal → Orchestrateur → LLM + Contexte → CRM → Humain
- [ ] Les données qui alimentent le bot (FAQ, catalogue, règles)
- [ ] Données structurées : chaque conversation = données exploitables
- [ ] Montrer un exemple de Fiche de synthèse
- [ ] Ouverture : fine-tuning & LoRA (repères, 3 minutes)

### 11h50-12h25 — Atelier Chatbot Canvas
- [ ] Distribuer le template (ou afficher via TP panel)
- [ ] Groupes de 4-5, 35 minutes
- [ ] Circuler entre les groupes, débloquer
- [ ] S'assurer que les 6 blocs sont remplis (persona, intents, ton, données, escalade, KPI)

### 12h25-12h30 — Brief après-midi
- [ ] Assigner les scénarios (1 par groupe)
- [ ] Distribuer les briefs imprimés
- [ ] Rappeler les livrables attendus à 18h
- [ ] "Bon appétit, on se retrouve à 14h"

## Après-midi — 14h-18h

### 14h00-14h15 — Tooling + prise en main Open WebUI
- [ ] Tooling : local vs cloud vs routeur (rappel 5-10 min)
- [ ] Démo rapide : provider, modèle, prompt système, contexte
- [ ] Astuce : 2 fenêtres (config + test client)
- [ ] Grille d'évaluation : précision, ton, questions, fiche de synthèse
- [ ] S'assurer que tous les groupes ont accès

### 14h15-15h05 — Atelier 1 : Prompting PO
- [ ] 50 minutes
- [ ] Objectif : prompt système + script accueil + fiche de synthèse
- [ ] Montrer l'exemple de prompt système (anatomie)
- [ ] Circuler : vérifier que le prompt a les 5 blocs (rôle, ton, périmètre, règles, escalade)
- [ ] Challenger : "Que se passe-t-il si je demande un prix ?"

### 15h05-15h15 — Pause

### 15h15-16h25 — Atelier 2 : Chatbot complet
- [ ] 70 minutes — le gros morceau
- [ ] Objectif : flow complet + version client/interne + plan de mesure
- [ ] Vérifier que chaque groupe teste au moins 3 scénarios
- [ ] S'assurer que la fiche de synthèse est structurée (pas un paragraphe)
- [ ] Alerter à 16h00 : "Plus que 25 minutes"

### 16h25-17h05 — Atelier 3 : Red Team croisée
- [ ] 40 minutes
- [ ] Rotation : chaque groupe teste le bot d'un AUTRE groupe
- [ ] Distribuer/afficher la checklist Red Team (6 catégories)
- [ ] Rappeler : 3 failles + 3 correctifs
- [ ] Ambiance constructive mais exigeante

### 17h05-17h25 — Fix & amélioration
- [ ] 20 minutes
- [ ] Chaque groupe corrige ses failles
- [ ] Stabiliser la fiche de synthèse
- [ ] Tester les corrections (2-3 échanges)

### 17h25-18h00 — Débrief collectif
- [ ] Tour de table : chaque groupe partage ses choix clés
- [ ] Poser 2-3 questions par groupe (prompt, failles, fiche de synthèse)
- [ ] Slide "Bravo & merci" — récap des acquis

## Matériels à préparer

| Quoi | Quantité | Format |
|------|----------|--------|
| Briefs scénario | 4 (1/groupe) | Papier A4 |
| Checklist Red Team | 4 (1/groupe) | Papier A4 |
| Comptes Open WebUI | 1 par groupe | Numérique |
| Chatbot démo "sans garde-fous" | 1 | Open WebUI |
| Chatbot démo "avec garde-fous" | 1 | Open WebUI |

## Après le cours

- [ ] Collecter les prompts système des groupes (capitalisation)
- [ ] Envoyer un récap par email (slides + briefs + ressources)
- [ ] Noter les points à améliorer pour la prochaine session
