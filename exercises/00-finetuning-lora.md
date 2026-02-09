# Ouverture : fine-tuning & LoRA (repères)

## Objectif

Comprendre la différence entre :
- Ajouter des informations (RAG)
- Changer le comportement du modèle (fine-tuning / LoRA)

## Définitions simples

- **RAG** : le modèle reste le même, mais on lui donne le bon contexte au bon moment.
- **Fine-tuning** : on adapte un modèle avec vos exemples pour qu'il se comporte mieux (format, ton, tâches).
- **LoRA** : une technique "légère" de fine-tuning (plus rapide/moins coûteuse) pour adapter un modèle sans tout ré-entraîner.

## Quand c'est pertinent (exemples)

- Vous voulez un **format de sortie strict** et stable (JSON, ticket, fiche CRM).
- Vous avez **beaucoup d'exemples** homogènes (classement, extraction, QA interne).
- Vous voulez un **style** très spécifique (ton de marque) qui ne passe pas bien via le prompt.

## Quand ce n'est PAS la solution

- Vous voulez que le bot connaisse vos prix/CGV/FAQ : c'est du **RAG**.
- Vous avez peu de données d'entraînement, ou pas de données "propres" et validées.
- Vous n'avez pas de **jeu de test** et de critères (risque de casser le bot ailleurs).

## Règle pratique (en cours)

Commencez par :
1. Un bon prompt système
2. Du RAG avec vos documents
3. Des tests (checklist + red team)

Puis seulement ensuite : fine-tuning / LoRA si vous avez un besoin clair et mesurable.

## Aide

> Cette section est masquée par défaut.
> Appuyer sur le bouton AIDE (ou touche A) pour l'afficher.

- Fine-tuning/LoRA est un sujet "niveau 2" : utile pour savoir que ça existe, pas obligatoire pour réussir l'atelier.
