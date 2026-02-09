# Brief 2 — Recommandation produit e-commerce

## "Quiz 5 questions"

### Contexte

Vous etes une marque D2C (tech lifestyle / audio / beaute / sport). Le chatbot aide a choisir le bon produit et a rassurer avant achat.

### Objectif business

- Augmenter conversion + panier moyen
- Reduire retours (mauvais choix)
- Ameliorer l'experience (conseil "vendeur boutique")

### Persona

Client hesitant, compare 2-3 options, peur de se tromper.

### Top intents

- "Je veux le meilleur rapport qualite/prix"
- "Je cherche un cadeau"
- "Je veux quelque chose de simple / premium"
- "Quelle difference entre A et B ?"
- "Livraison / retour / garantie ?"

### Contraintes / garde-fous

- Ne jamais inventer stock/delai : si non fourni, rester vague + renvoyer vers page livraison
- Ne pas etre pushy (pas de dark patterns)
- Toujours verifier le besoin avant de recommander (quiz court)
- Si incertitude, proposer 2 options avec criteres de choix

### Catalogue (fictif, a coller en contexte)

```
PRODUIT 1 : SoundPulse Mini — 49 EUR
Usage : quotidien, transport. Pour qui : etudiants, sportifs.
+ Leger, autonomie 12h, resistant eau. - Pas de reduction bruit.

PRODUIT 2 : SoundPulse Pro — 129 EUR
Usage : travail, musique. Pour qui : professionnels, melomanes.
+ Reduction bruit active, son HD, micro. - Plus lourd.

PRODUIT 3 : SoundPulse Studio — 249 EUR
Usage : studio, gaming. Pour qui : audiophiles, gamers.
+ Son spatial, ultra-basse latence, cable detachable. - Encombrant.

PRODUIT 4 : SoundPulse Sport — 79 EUR
Usage : sport intensif. Pour qui : runners, salle de sport.
+ Ultra-leger, IP67, crochets oreille. - Son correct sans plus.

PRODUIT 5 : SoundPulse Kids — 39 EUR
Usage : enfants 6-12 ans. Pour qui : parents.
+ Volume limite 85dB, resistant, fun. - Pas Bluetooth.

PRODUIT 6 : SoundPulse Travel — 169 EUR
Usage : voyages, avion. Pour qui : voyageurs frequents.
+ ANC top, pliable, etui, autonomie 30h. - Pas pour sport.

POLITIQUE RETOURS : 30 jours, gratuit, produit non utilise.
GARANTIE : 2 ans tous produits.
LIVRAISON : Standard 3-5 jours (gratuit > 50 EUR), Express 24h (9.90 EUR).
```

### Livrables attendus

1. Prompt systeme "conseiller de marque" + ton
2. Quiz 5 questions max (usage, budget, preferences...)
3. Recommandation : 1 choix principal + 1 alternative + justification simple
4. "Note CRM" (si collecte opt-in) : profil client + recommandation + objections
5. KPI : conversion, AOV (panier moyen), taux de retour, CSAT
