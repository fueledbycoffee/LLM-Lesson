# Brief 1 — Lead Qualification B2B (SaaS)

## "RDV + Lead CRM-ready"

### Contexte

Vous etes une startup SaaS qui vend un outil marketing/CRM aux PME/ETI. Le chatbot est sur le site (landing + pricing). Objectif : transformer des visiteurs en leads qualifies et generer des RDV.

### Objectif business

- Augmenter le taux de prise de RDV
- Qualifier les leads (prioriser l'equipe sales)
- Reduire les echanges inutiles

### Persona

Responsable marketing / Sales Ops / Dirigeant PME. Presse. Veut du concret (prix, integration, ROI).

### Top intents (exemples)

- "C'est combien ?" / "Vous avez une demo ?"
- "Ca s'integre avec HubSpot/Salesforce/Excel ?"
- "C'est pour une equipe de 10/50/200, possible ?"
- "On veut automatiser X (leads, scoring, nurturing...)"
- "Je peux parler a quelqu'un aujourd'hui ?"

### Contraintes / garde-fous

- Ne jamais inventer un prix : si non fourni, donner une fourchette ou inviter a RDV
- Ne jamais promettre ROI ou delais d'implementation "garantis"
- Collecte minimale (RGPD) : demander email/telephone seulement si necessaire et avec consentement
- Si le prospect est flou, poser max 3 questions de clarification

### Donnees disponibles (fictives)

- Offre : 3 plans (Starter / Pro / Enterprise) — vous n'avez PAS les prix exacts (c'est volontaire)
- Valeur : integrations CRM, scoring, dashboards, automatisations
- CTA : "Reserver une demo 30 min" / "Recevoir un mail recap"

### Livrables attendus

1. Prompt systeme (role, ton "consultatif", regles anti-hallucination)
2. Flow conversationnel : Accueil, qualification, proposition RDV, recap
3. Sortie "Note CRM" structuree :
   - Besoin principal
   - Taille entreprise
   - Outils actuels
   - Urgence
   - Budget (si donne)
   - Decisionnaire (oui/non)
   - Objections
   - Prochaine action
4. KPI proposes : % RDV pris, taux de qualification, conversion lead vers SQL
