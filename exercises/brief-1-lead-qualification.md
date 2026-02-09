# Brief 1 — Lead Qualification B2B (SaaS)

## "RDV + Lead structure"

### Marque : **FlowDesk**

### Contexte

Vous êtes FlowDesk, une startup SaaS qui vend un outil marketing/CRM aux PME/ETI. Le chatbot est sur le site (landing + pricing). Objectif : transformer des visiteurs en leads qualifiés et générer des RDV.

### Objectif business

- Augmenter le taux de prise de RDV
- Qualifier les leads (prioriser l'équipe sales)
- Réduire les échanges inutiles

### Persona

Responsable marketing / Sales Ops / Dirigeant PME. Pressé. Veut du concret (prix, intégration, ROI).

### Top intents (exemples)

- "C'est combien ?" / "Vous avez une démo ?"
- "Ça s'intègre avec HubSpot/Salesforce/Excel ?"
- "C'est pour une équipe de 10/50/200, possible ?"
- "On veut automatiser X (leads, scoring, nurturing...)"
- "Je peux parler à quelqu'un aujourd'hui ?"

### Contraintes / garde-fous

- Ne jamais inventer un prix : si non fourni, donner une fourchette ou inviter à RDV
- Ne jamais promettre ROI ou délais d'implémentation "garantis"
- Collecte minimale (RGPD) : demander email/téléphone seulement si nécessaire et avec consentement
- Si le prospect est flou, poser max 3 questions de clarification

### Données disponibles (fictives)

- Offre : 3 plans (Starter / Pro / Enterprise) — vous n'avez PAS les prix exacts (c'est volontaire)
- Valeur : intégrations CRM, scoring, dashboards, automatisations
- CTA : "Réserver une démo 30 min" / "Recevoir un mail récap"

### Livrables attendus

1. Prompt système (rôle, ton "consultatif", règles anti-hallucination)
2. Flow conversationnel : Accueil, qualification, proposition RDV, récap
3. Sortie "Fiche de synthèse" structurée :
   - Besoin principal
   - Taille entreprise
   - Outils actuels
   - Urgence
   - Budget (si donné)
   - Décisionnaire (oui/non)
   - Objections
   - Prochaine action
4. KPI proposés : % RDV pris, taux de qualification, conversion lead vers SQL
