# Brief 2 — Recommandation produit e-commerce

## "Quiz 5 questions"

### Contexte

Vous êtes une marque D2C (tech lifestyle / audio / beauté / sport). Le chatbot aide à choisir le bon produit et à rassurer avant achat.

### Objectif business

- Augmenter conversion + panier moyen
- Réduire retours (mauvais choix)
- Améliorer l'expérience (conseil "vendeur boutique")

### Persona

Client hésitant, compare 2-3 options, peur de se tromper.

### Top intents

- "Je veux le meilleur rapport qualité/prix"
- "Je cherche un cadeau"
- "Je veux quelque chose de simple / premium"
- "Quelle différence entre A et B ?"
- "Livraison / retour / garantie ?"

### Contraintes / garde-fous

- Ne jamais inventer stock/délai : si non fourni, rester vague + renvoyer vers page livraison
- Ne pas être pushy (pas de dark patterns)
- Toujours vérifier le besoin avant de recommander (quiz court)
- Si incertitude, proposer 2 options avec critères de choix

### Catalogue (fictif, à coller en contexte)

```
PRODUIT 1 : SoundPulse Mini — 49 EUR
Usage : quotidien, transport. Pour qui : étudiants, sportifs.
+ Léger, autonomie 12h, résistant eau. - Pas de réduction bruit.

PRODUIT 2 : SoundPulse Pro — 129 EUR
Usage : travail, musique. Pour qui : professionnels, mélomanes.
+ Réduction bruit active, son HD, micro. - Plus lourd.

PRODUIT 3 : SoundPulse Studio — 249 EUR
Usage : studio, gaming. Pour qui : audiophiles, gamers.
+ Son spatial, ultra-basse latence, câble détachable. - Encombrant.

PRODUIT 4 : SoundPulse Sport — 79 EUR
Usage : sport intensif. Pour qui : runners, salle de sport.
+ Ultra-léger, IP67, crochets oreille. - Son correct sans plus.

PRODUIT 5 : SoundPulse Kids — 39 EUR
Usage : enfants 6-12 ans. Pour qui : parents.
+ Volume limite 85dB, résistant, fun. - Pas Bluetooth.

PRODUIT 6 : SoundPulse Travel — 169 EUR
Usage : voyages, avion. Pour qui : voyageurs fréquents.
+ ANC top, pliable, étui, autonomie 30h. - Pas pour sport.

POLITIQUE RETOURS : 30 jours, gratuit, produit non utilisé.
GARANTIE : 2 ans tous produits.
LIVRAISON : Standard 3-5 jours (gratuit > 50 EUR), Express 24h (9.90 EUR).
```

### Livrables attendus

1. Prompt système "conseiller de marque" + ton
2. Quiz 5 questions max (usage, budget, preferences...)
3. Recommandation : 1 choix principal + 1 alternative + justification simple
4. "Fiche de synthèse" (si collecte opt-in) : profil client + recommandation + objections
5. KPI : conversion, AOV (panier moyen), taux de retour, CSAT
