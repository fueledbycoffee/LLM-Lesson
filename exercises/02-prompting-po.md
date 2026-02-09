# Atelier 1 : Prompting PO

## Objectif

Passer de "chat sympa" a "assistant produit" en ecrivant un prompt systeme professionnel, un script d'accueil et un format de sortie CRM.

## Consignes

Temps : 50 minutes. Travail en groupe sur Open WebUI.

### Etape 1 : Prompt systeme (20 min)

Ecrivez le prompt systeme de votre chatbot. Il doit contenir :

1. **Role** : qui est le bot, pour quelle entreprise, quel objectif
2. **Ton** : style de communication (formel, consultatif, empathique...)
3. **Perimetre** : ce qu'il fait, ce qu'il ne fait PAS
4. **Regles anti-hallucination** :
   - "Ne reponds que si l'info est dans ton contexte"
   - "Si tu ne sais pas, dis-le clairement"
   - "Ne jamais inventer un prix, un delai ou une politique"
5. **Escalade** : quand et comment transferer a un humain

### Etape 2 : Script d'accueil (10 min)

Ecrivez le message d'accueil du bot + les questions de clarification.

- Message d'accueil : 2-3 phrases max, engageantes, orientees action
- Questions de clarification : 3-5 questions que le bot pose pour comprendre le besoin
- Regle : ne pas poser toutes les questions d'un coup, les enchainer naturellement

### Etape 3 : Format "Note CRM" (10 min)

Definissez le format de sortie structure que le bot doit generer a la fin de chaque conversation.

Exemple de structure :

```
--- NOTE CRM ---
Date : [date]
Canal : [site / chat / WhatsApp]
Besoin principal : [1 phrase]
[Champs specifiques a votre scenario]
Objections / freins : [liste]
Action suivante : [RDV / devis / escalade / relance]
Priorite : [haute / moyenne / basse]
--- FIN ---
```

### Etape 4 : Tester (10 min)

- Collez votre prompt systeme dans Open WebUI
- Testez 3-4 conversations differentes
- Verifiez : le bot respecte-t-il le ton ? Refuse-t-il de repondre quand il ne sait pas ? Produit-il la Note CRM ?

## Criteres de reussite

- Le prompt systeme couvre les 5 blocs (role, ton, perimetre, regles, escalade)
- Le script d'accueil est engageant et naturel
- La Note CRM est structuree et exploitable
- Le bot a ete teste et ajuste

## Aide

> Cette section est masquee par defaut.
> Appuyer sur le bouton AIDE (ou touche A) pour l'afficher.

- Structure de prompt recommandee : commencez chaque section par un commentaire (# Role, # Ton, # Regles...)
- Pour le ton : "Tu vouvoies toujours. Tu es professionnel et consultatif. Tu ne fais jamais de promesses."
- Anti-hallucination : ajoutez "Si l'information n'est pas dans ton contexte, reponds : Je n'ai pas cette information, mais je peux vous mettre en relation avec un collegue."
- Pour la Note CRM : ajoutez dans le prompt "A la fin de chaque conversation, genere une Note CRM au format suivant : ..."
- Pour l'accueil : evitez le generique "Comment puis-je vous aider ?" — preferez "Bonjour ! Je suis l'assistant de [Marque]. Vous cherchez [besoin principal] ?"
