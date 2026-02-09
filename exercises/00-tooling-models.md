# Tooling & modèles (repères)

## Objectif

Comprendre comment s'assemble un chatbot : interface, fournisseur, modèle, et options de routage (ex: OpenRouter).

## Le modèle mental (à retenir)

Un chatbot en atelier = 4 briques :
- **UI** : Open WebUI (l'interface)
- **Provider** : où tourne le modèle (local ou cloud)
- **Modèle** : ce qui génère le texte
- **Cadrage** : prompt + contexte + tests + garde-fous

## Où peuvent tourner les modèles ?

### Option A) Local (machine)

- Avantages : contrôle, confidentialité, coût variable
- Limites : puissance/VRAM, modèles plus petits, installation

### Option B) Cloud (API directe)

- Avantages : simple, modèles performants, stable
- Limites : coût à l'usage, politiques de données, dépendance fournisseur

### Option C) Routeur multi-modèles (ex: OpenRouter)

- Idée : un **point d'entrée** pour accéder à plusieurs modèles
- Intérêt : comparer, changer de modèle par use case, optimiser coût/latence
- Attention : gouvernance (clés API, facturation, données envoyées)

## Comment choisir un modèle (sans se perdre)

Posez 5 questions :
1. Quelle qualité attendue (support vs rédaction vs créativité) ?
2. Quelle **latence** acceptable ?
3. Quel budget (coût par requête) ?
4. Quelle taille de contexte (FAQ courte vs docs longs) ?
5. Quelles contraintes de données (PII, secrets, RGPD) ?

## Règles pratiques en atelier

- Par défaut : température basse (0.1-0.3) pour éviter l'invention.
- Ne collez jamais : CB, mot de passe, données sensibles.
- Un bot "pro" sait dire "je ne sais pas" + escalader.

## Aide

> Cette section est masquée par défaut.
> Appuyer sur le bouton AIDE (ou touche A) pour l'afficher.

- Aujourd'hui, on utilise OpenRouter comme provider, mais le principe reste identique : provider + modèle + cadrage + tests.
- Si vous ne savez pas quoi choisir : prenez un modèle texte généraliste, testez, puis changez si besoin.
