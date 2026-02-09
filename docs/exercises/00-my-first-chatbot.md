# My First Chatbot (Open WebUI)

## Objectif

Construire en 5-10 minutes un premier chatbot simple, utile et testable, sans coder.

## Consignes

Temps : 10 minutes (démo formateur ou en binôme).

Ce que vous produisez :
- 1 prompt système minimal (rôle + règles + format)
- 1 mini "Fiche de synthèse" en fin de conversation

## Étapes

### 1) Choisir un modèle (1 min)

- Prenez un modèle texte (pas besoin d'image/audio)
- Réglez la **température** basse (0.1-0.3) pour rester factuel (température = curseur de créativité)

### 2) Créer le bot + coller le prompt système (3 min)

Copiez/collez et adaptez :

```text
# Rôle
Tu es un assistant de support pour [Marque].

# Objectif
Aider l'utilisateur à obtenir une réponse fiable ou à escalader vers un humain.

# Règles
- Si l'information n'est pas connue ou pas dans le contexte, dis-le clairement.
- Ne jamais inventer de prix, de délais, de politique.
- Pose au maximum 2 questions de clarification si nécessaire.

# Ton
Professionnel, clair, concis.

# Format
À la fin de la conversation, génère une Fiche de synthèse structurée :
- Besoin
- Contexte
- Réponse donnée
- Points d'incertitude (s'il y en a)
- Action suivante (FAQ, ticket, RDV, escalade)
```

### 3) Tester (3 min)

Testez 3 messages :
- Un cas simple (question directe)
- Un cas flou (manque d'info)
- Un cas hors périmètre (demande impossible)

Notez : le bot refuse-t-il d'inventer ? pose-t-il des questions ? reste-t-il dans le ton ?

### 4) Itérer (3 min)

Améliorations rapides :
- Ajoutez 1 règle de sécurité (ex: pas de données sensibles)
- Ajoutez 1 contrainte produit (ex: quand escalader)
- Rendez la Fiche de synthèse plus exploitable (champs + action)

## Aide

> Cette section est masquée par défaut.
> Appuyer sur le bouton AIDE (ou touche A) pour l'afficher.

- L'objectif ici n'est pas d'avoir "le meilleur bot" mais de voir la mécanique : modèle + prompt + tests.
- Si le bot hallucine : réduisez la température et durcissez la règle "ne pas inventer".
- Vous pourrez ensuite ajouter du contexte (FAQ, catalogue) pour le rendre réellement utile.
