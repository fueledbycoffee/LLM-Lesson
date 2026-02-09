# Atelier 2 : Construire le chatbot complet

## Objectif

Construire un flow conversationnel complet, de l'accueil a la Note CRM, avec une version client et une version interne.

## Consignes

Temps : 70 minutes. Travail en groupe sur Open WebUI.

### Etape 1 : Flow conversationnel (30 min)

Construisez le parcours complet de votre chatbot :

1. **Accueil** : message d'ouverture + premiere question
2. **Intake** : 3-5 questions pour comprendre le besoin (enchainees naturellement)
3. **Reponse** : recommandation, information ou solution basee sur le contexte
4. **CTA** : call-to-action clair (RDV, achat, callback, ticket...)
5. **Note CRM** : sortie structuree a la fin

Testez le flow avec au moins 3 scenarios differents :
- Un client "ideal" (repond bien, besoin clair)
- Un client "flou" (vague, hesite, change d'avis)
- Un client "hors perimetre" (demande quelque chose que le bot ne gere pas)

### Etape 2 : Version client vs version interne (20 min)

Votre chatbot doit servir deux publics :

**Version client** (ce que voit l'utilisateur)
- Messages naturels, engageants, orientes solution
- Jamais de jargon interne
- CTA clair a chaque etape

**Version interne** (ce que voit l'equipe marketing/sales)
- Note CRM structuree avec tous les champs
- Resume de la conversation
- Indicateurs : urgence, budget, decisionnaire, objections
- Action suivante recommandee

Ajoutez dans votre prompt systeme une instruction pour generer les deux sorties.

### Etape 3 : Mini plan de mesure (20 min)

Definissez comment mesurer le succes de votre chatbot :

- 3-5 KPI cles (choisissez dans la liste ci-dessous)
- Pour chaque KPI : quelle donnee, quel outil, quel objectif chiffre

KPI possibles :
- Taux de conversion (visiteur -> action)
- Taux de qualification (lead -> SQL)
- Panier moyen (AOV)
- Taux de deflexion (resolu sans humain)
- CSAT (satisfaction)
- Taux d'escalade
- Temps de resolution (AHT)
- Taux de recontact
- Taux de recuperation panier
- FCR (First Contact Resolution)

## Criteres de reussite

- Le flow couvre les 5 etapes (accueil -> intake -> reponse -> CTA -> Note CRM)
- 3 scenarios testes avec succes
- Les versions client et interne sont differenciees
- Le plan de mesure est realiste et chiffre

## Aide

> Cette section est masquee par defaut.
> Appuyer sur le bouton AIDE (ou touche A) pour l'afficher.

- Pour le flow : pensez "arbre de decision" mais en langage naturel. Le bot doit savoir quoi faire a chaque etape.
- Pour la version interne : ajoutez dans le prompt "Apres chaque conversation, genere un resume interne avec les champs suivants : ..."
- Pour les KPI : soyez specifiques. Pas "ameliorer la conversion" mais "passer de 2% a 5% de taux de RDV pris via le chatbot en 3 mois"
- Si le bot deraille : verifiez que votre prompt systeme est assez explicite. Ajoutez des exemples de reponses attendues.
- Technique : dans Open WebUI, vous pouvez coller du contexte (FAQ, catalogue) dans les instructions ou en piece jointe.
