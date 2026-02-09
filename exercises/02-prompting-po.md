# Atelier 1 : Prompting PO

## Objectif

Passer de "chat sympa" à "assistant produit" en écrivant un prompt système professionnel, un script d'accueil et une fiche de synthèse.

## Consignes

Temps : 50 minutes. Travail en groupe sur Open WebUI.

> **Donnees contexte** : Les fichiers a coller dans votre chatbot sont dans `data/[votre-scenario]/` (ex: `data/1-lead-qualification/`). Utilisez-les comme base de connaissances.

### Étape 1 : Prompt système (20 min)

Écrivez le prompt système de votre chatbot. Il doit contenir :

1. **Rôle** : qui est le bot, pour quelle entreprise, quel objectif
2. **Ton** : style de communication (formel, consultatif, empathique...)
3. **Périmètre** : ce qu'il fait, ce qu'il ne fait PAS
4. **Règles anti-hallucination** :
   - "Ne réponds que si l'info est dans ton contexte"
   - "Si tu ne sais pas, dis-le clairement"
   - "Ne jamais inventer un prix, un délai ou une politique"
5. **Escalade** : quand et comment transférer à un humain

### Étape 2 : Script d'accueil (10 min)

Écrivez le message d'accueil du bot + les questions de clarification.

- Message d'accueil : 2-3 phrases max, engageantes, orientées action
- Questions de clarification : 3-5 questions que le bot pose pour comprendre le besoin
- Règle : ne pas poser toutes les questions d'un coup, les enchaîner naturellement

### Étape 3 : Format "Fiche de synthèse" (10 min)

Définissez le format de sortie structuré que le bot doit générer à la fin de chaque conversation.

Exemple de structure :

```
--- FICHE DE SYNTHÈSE ---
Date : [date]
Canal : [site / chat / WhatsApp]
Besoin principal : [1 phrase]
[Champs specifiques a votre scenario]
Objections / freins : [liste]
Action suivante : [RDV / devis / escalade / relance]
Priorite : [haute / moyenne / basse]
--- FIN ---
```

### Étape 4 : Tester (10 min)

- Collez votre prompt système dans Open WebUI
- Testez 3-4 conversations différentes
- Vérifiez : le bot respecte-t-il le ton ? Refuse-t-il de répondre quand il ne sait pas ? Produit-il la Fiche de synthèse ?

## Critères de réussite

- Le prompt système couvre les 5 blocs (rôle, ton, périmètre, règles, escalade)
- Le script d'accueil est engageant et naturel
- La Fiche de synthèse est structurée et exploitable
- Le bot a été testé et ajusté

## Aide

> Cette section est masquée par défaut.
> Appuyer sur le bouton AIDE (ou touche A) pour l'afficher.

- Structure de prompt recommandée : commencez chaque section par un commentaire (# Rôle, # Ton, # Règles...)
- Pour le ton : "Tu vouvoies toujours. Tu es professionnel et consultatif. Tu ne fais jamais de promesses."
- Anti-hallucination : ajoutez "Si l'information n'est pas dans ton contexte, réponds : Je n'ai pas cette information, mais je peux vous mettre en relation avec un collègue."
- Pour la Fiche de synthèse : ajoutez dans le prompt "À la fin de chaque conversation, génère une Fiche de synthèse au format suivant : ..."
- Pour l'accueil : évitez le générique "Comment puis-je vous aider ?" — préférez "Bonjour ! Je suis l'assistant de [Marque]. Vous cherchez [besoin principal] ?"
