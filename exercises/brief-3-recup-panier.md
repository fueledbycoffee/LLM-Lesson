# Brief 3 — Recup panier & objections

## "Conversion sans forcer"

### Contexte

Un utilisateur a ajoute un produit au panier mais n'achete pas. Le chatbot intervient (site / chat) pour lever les objections.

### Objectif business

- Reduire l'abandon panier
- Repondre vite aux objections frequentes
- Orienter vers le bon canal (support / sales) si besoin

### Persona

Acheteur rationnel : prix, delais, confiance, garanties.

### Objections typiques (a traiter)

- "C'est trop cher"
- "Je ne suis pas sur que ca marche pour moi"
- "Delai de livraison incertain"
- "J'ai peur du SAV / des retours"
- "Je compare avec [concurrent]"

### Contraintes / garde-fous

- Pas de remise inventee / pas de faux "stock faible"
- Autorise : proposer un code promo UNIQUEMENT si fourni dans le contexte (sinon : non)
- Comparaison concurrent : rester factuel, ne pas diffamer
- Si client agace, empathie + option humain

### Donnees disponibles (a coller en contexte)

```
POLITIQUE RETOUR : 30 jours, remboursement integral, retour gratuit.
GARANTIE : 2 ans sur tous les produits.
SAV : Reponse sous 24-48h, equipe basee en France.
LIVRAISON : Standard 3-5 jours ouvrables (gratuit > 50 EUR).
            Express 24h disponible (9.90 EUR).

ARGUMENTS DE VALEUR :
1. Fabrique en Europe, materiaux durables
2. Note 4.7/5 sur 2000+ avis clients
3. Utilise par 500+ entreprises (logos sur le site)

CODE PROMO ACTIF : BIENVENUE10 (-10% premiere commande, valable 48h)
```

### Livrables attendus

1. Prompt systeme "conversion helper" (non agressif)
2. Scripts courts pour 3 objections majeures
3. CTA final : finaliser achat / demander callback / email recap
4. "Note CRM" : objection principale + produit + etape suivante
5. KPI : taux de recuperation, conversion, CSAT, taux escalade
