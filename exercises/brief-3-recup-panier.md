# Brief 3 — Récup panier & objections

## "Conversion sans forcer"

### Marque : **Velora**

### Contexte

Vous êtes Velora, une marque de mode éco-responsable. Un utilisateur a ajouté un produit au panier mais n'achète pas. Le chatbot intervient (site / chat) pour lever les objections.

### Objectif business

- Réduire l'abandon panier
- Répondre vite aux objections fréquentes
- Orienter vers le bon canal (support / sales) si besoin

### Persona

Acheteur rationnel : prix, délais, confiance, garanties.

### Objections typiques (à traiter)

- "C'est trop cher"
- "Je ne suis pas sûr que ça marche pour moi"
- "Délai de livraison incertain"
- "J'ai peur du SAV / des retours"
- "Je compare avec [concurrent]"

### Contraintes / garde-fous

- Pas de remise inventée / pas de faux "stock faible"
- Autorisé : proposer un code promo UNIQUEMENT si fourni dans le contexte (sinon : non)
- Comparaison concurrent : rester factuel, ne pas diffamer
- Si client agacé, empathie + option humain

### Données disponibles (à coller en contexte)

```
POLITIQUE RETOUR : 30 jours, remboursement intégral, retour gratuit.
GARANTIE : 2 ans sur tous les produits.
SAV : Réponse sous 24-48h, équipe basée en France.
LIVRAISON : Standard 3-5 jours ouvrables (gratuit > 50 EUR).
            Express 24h disponible (9.90 EUR).

ARGUMENTS DE VALEUR :
1. Fabriqué en Europe, matériaux durables
2. Note 4.7/5 sur 2000+ avis clients
3. Utilisé par 500+ entreprises (logos sur le site)

CODE PROMO ACTIF : BIENVENUE10 (-10% première commande, valable 48h)
```

### Livrables attendus

1. Prompt système "conversion helper" (non agressif)
2. Scripts courts pour 3 objections majeures
3. CTA final : finaliser achat / demander callback / email récap
4. "Fiche de synthèse" : objection principale + produit + étape suivante
5. KPI : taux de récupération, conversion, CSAT, taux escalade
