# Brief 4 — Support & fidélisation

## "Pré-triage + ticket parfait"

### Marque : **CloudBox**

### Contexte

Vous êtes CloudBox, un service de stockage cloud français. Chatbot sur la page support. Il doit résoudre les questions simples + créer un ticket "propre" si nécessaire.

### Objectif business

- Déflexion (résoudre sans humain)
- Réduire l'effort client
- Tickets plus propres = résolution plus rapide

### Persona

Client frustré ou pressé, veut une solution immédiate.

### Top intents

- "Où est ma commande ?"
- "Je veux retourner / échanger"
- "Le produit ne marche plus"
- "Facture / paiement"
- "J'ai un problème de compte"

### Contraintes / garde-fous

- Ne pas demander d'infos sensibles (CB, mots de passe)
- Collecte minimale : numéro de commande / email (si nécessaire)
- Escalade immédiate si : menace légale, données personnelles, harcèlement, situation à risque
- Si incertitude, poser 1-2 questions max puis escalader

### Données disponibles (à coller en contexte)

```
FAQ SUPPORT :

Q: Où est ma commande ?
R: Vérifiez votre email de confirmation pour le lien de suivi.
   Si pas reçu sous 48h après commande, contactez-nous avec
   votre numéro de commande.

Q: Comment retourner un produit ?
R: Connectez-vous > Mes commandes > Demander un retour.
   Délai : 30 jours après réception. Produit non utilisé,
   emballage d'origine. Retour gratuit.

Q: Le produit est défectueux
R: Garantie 2 ans. Contactez le support avec : numéro de
   commande + photo du défaut. Échange ou remboursement
   sous 5 jours ouvrables.

Q: Problème de paiement
R: Vérifiez que votre carte n'est pas expirée. Essayez un
   autre moyen de paiement. Si le problème persiste, contactez
   votre banque ou notre support.

Q: Problème de compte (connexion, mot de passe)
R: Cliquez sur "Mot de passe oublié" sur la page de connexion.
   Si le problème persiste, contactez le support avec l'email
   associé à votre compte.

PROCÉDURE DE TICKET :
Catégories : livraison, produit, paiement, compte, autre
Urgence : haute (commande bloquée, défaut), moyenne (retour,
          échange), basse (question, feedback)
```

### Livrables attendus

1. Prompt système "support de marque" + règles de sécurité
2. Flow : diagnostic, solution base de connaissances, sinon création ticket
3. "Fiche de synthèse / Ticket" structurée :
   - Catégorie
   - Description courte
   - Étapes déjà testées par le client
   - Numéro de commande
   - Urgence
   - Pièces à joindre (si besoin)
4. KPI : déflexion, FCR (First Contact Resolution), AHT (temps de résolution humain), CSAT, taux de recontact
