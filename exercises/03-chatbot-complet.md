# Atelier 2 : Construire le chatbot complet

## Objectif

Construire un flow conversationnel complet, de l'accueil à la Fiche de synthèse, avec une version client et une version interne.

## Consignes

Temps : 70 minutes. Travail en groupe sur Open WebUI.

> **Données contexte** : Les fichiers à coller dans votre chatbot sont dans `data/[votre-scenario]/` (ex: `data/2-recommandation-produit/`). Utilisez-les comme base de connaissances.

### Étape 1 : Flow conversationnel (30 min)

Construisez le parcours complet de votre chatbot :

1. **Accueil** : message d'ouverture + première question
2. **Intake** : 3-5 questions pour comprendre le besoin (enchaînées naturellement)
3. **Réponse** : recommandation, information ou solution basée sur le contexte
4. **CTA** : call-to-action clair (RDV, achat, callback, ticket...)
5. **Fiche de synthèse** : sortie structurée à la fin

Testez le flow avec au moins 3 scénarios différents :
- Un client "idéal" (répond bien, besoin clair)
- Un client "flou" (vague, hésite, change d'avis)
- Un client "hors périmètre" (demande quelque chose que le bot ne gère pas)

### Étape 2 : Version client vs version interne (20 min)

Votre chatbot doit servir deux publics :

**Version client** (ce que voit l'utilisateur)
- Messages naturels, engageants, orientés solution
- Jamais de jargon interne
- CTA clair à chaque étape

**Version interne** (ce que voit l'équipe marketing/sales)
- Fiche de synthèse structurée avec tous les champs
- Résumé de la conversation
- Indicateurs : urgence, budget, decisionnaire, objections
- Action suivante recommandée

Ajoutez dans votre prompt système une instruction pour générer les deux sorties.

**Technique dual-output** : ajoutez à la fin de votre prompt système une instruction comme :

```
After each conversation, generate two outputs:
1. CLIENT — A natural closing message for the user (in French)
2. INTERNAL — A structured lead/ticket summary with all fields (in French)
Separate the two with "---"
```

Cela permet de produire une réponse utilisateur naturelle ET une fiche exploitable pour l'équipe, dans la même conversation.

### Étape 3 : Mini plan de mesure (20 min)

Définissez comment mesurer le succès de votre chatbot :

- 3-5 KPI clés (choisissez dans la liste ci-dessous)
- Pour chaque KPI : quelle donnée, quel outil, quel objectif chiffré

KPI possibles :
- Taux de conversion (visiteur -> action)
- Taux de qualification (lead -> SQL)
- Panier moyen (AOV)
- Taux de déflexion (résolu sans humain)
- CSAT (satisfaction)
- Taux d'escalade
- Temps de résolution (AHT)
- Taux de recontact
- Taux de récupération panier
- FCR (First Contact Resolution)

## Critères de réussite

- Le flow couvre les 5 étapes (accueil -> intake -> réponse -> CTA -> Fiche de synthèse)
- 3 scénarios testés avec succès
- Les versions client et interne sont différenciées
- Le plan de mesure est réaliste et chiffré

## Aide

> Cette section est masquée par défaut.
> Appuyer sur le bouton AIDE (ou touche A) pour l'afficher.

- Pour le flow : pensez "arbre de décision" mais en langage naturel. Le bot doit savoir quoi faire à chaque étape.
- Pour la version interne : ajoutez dans le prompt "Après chaque conversation, génère un résumé interne avec les champs suivants : ..."
- Pour les KPI : soyez spécifiques. Pas "améliorer la conversion" mais "passer de 2% à 5% de taux de RDV pris via le chatbot en 3 mois"
- Si le bot déraille : vérifiez que votre prompt système est assez explicite. Ajoutez des exemples de réponses attendues.
- Technique : dans Open WebUI, vous pouvez coller du contexte (FAQ, catalogue) dans les instructions ou en pièce jointe.
