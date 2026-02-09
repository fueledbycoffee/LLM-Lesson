# Brief 4 — Support & fidelisation

## "Pre-triage + ticket parfait"

### Contexte

Chatbot sur la page support. Il doit resoudre les questions simples + creer un ticket "propre" si necessaire.

### Objectif business

- Deflexion (resoudre sans humain)
- Reduire l'effort client
- Tickets plus propres = resolution plus rapide

### Persona

Client frustre ou presse, veut une solution immediate.

### Top intents

- "Ou est ma commande ?"
- "Je veux retourner / echanger"
- "Le produit ne marche plus"
- "Facture / paiement"
- "J'ai un probleme de compte"

### Contraintes / garde-fous

- Ne pas demander d'infos sensibles (CB, mots de passe)
- Collecte minimale : numero de commande / email (si necessaire)
- Escalade immediate si : menace legale, donnees personnelles, harcelement, situation a risque
- Si incertitude, poser 1-2 questions max puis escalader

### Donnees disponibles (a coller en contexte)

```
FAQ SUPPORT :

Q: Ou est ma commande ?
R: Verifiez votre email de confirmation pour le lien de suivi.
   Si pas recu sous 48h apres commande, contactez-nous avec
   votre numero de commande.

Q: Comment retourner un produit ?
R: Connectez-vous > Mes commandes > Demander un retour.
   Delai : 30 jours apres reception. Produit non utilise,
   emballage d'origine. Retour gratuit.

Q: Le produit est defectueux
R: Garantie 2 ans. Contactez le support avec : numero de
   commande + photo du defaut. Echange ou remboursement
   sous 5 jours ouvrables.

Q: Probleme de paiement
R: Verifiez que votre carte n'est pas expiree. Essayez un
   autre moyen de paiement. Si le probleme persiste, contactez
   votre banque ou notre support.

Q: Probleme de compte (connexion, mot de passe)
R: Cliquez sur "Mot de passe oublie" sur la page de connexion.
   Si le probleme persiste, contactez le support avec l'email
   associe a votre compte.

PROCEDURE DE TICKET :
Categories : livraison, produit, paiement, compte, autre
Urgence : haute (commande bloquee, defaut), moyenne (retour,
          echange), basse (question, feedback)
```

### Livrables attendus

1. Prompt systeme "support de marque" + regles de securite
2. Flow : diagnostic, solution base de connaissances, sinon creation ticket
3. "Note CRM / Ticket" structuree :
   - Categorie
   - Description courte
   - Etapes deja testees par le client
   - Numero de commande
   - Urgence
   - Pieces a joindre (si besoin)
4. KPI : deflexion, FCR (First Contact Resolution), AHT (temps de resolution humain), CSAT, taux de recontact
