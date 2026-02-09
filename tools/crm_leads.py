"""
title: CRM Leads
description: Gestion de leads et contacts clients — ajouter, rechercher, qualifier des prospects.
author: demo
version: 0.1.0
"""

import secrets
from pydantic import BaseModel
from datetime import datetime


class Tools:
    class Valves(BaseModel):
        pass

    def __init__(self):
        self.valves = self.Valves()
        self.leads = [
            {
                "id": 1,
                "nom": "Marie Dupont",
                "email": "marie.dupont@gmail.com",
                "telephone": "06 12 34 56 78",
                "source": "Instagram Ads",
                "interet": "Soins visage",
                "statut": "nouveau",
                "date_creation": "2025-02-01",
                "score": 72,
            },
            {
                "id": 2,
                "nom": "Thomas Bernard",
                "email": "t.bernard@outlook.fr",
                "telephone": "06 98 76 54 32",
                "source": "Site web",
                "interet": "Coffrets cadeaux",
                "statut": "contacte",
                "date_creation": "2025-01-28",
                "score": 45,
            },
            {
                "id": 3,
                "nom": "Sophie Martin",
                "email": "sophie.m@yahoo.fr",
                "telephone": "07 11 22 33 44",
                "source": "Newsletter",
                "interet": "Cosmétiques bio",
                "statut": "qualifie",
                "date_creation": "2025-01-15",
                "score": 89,
            },
            {
                "id": 4,
                "nom": "Lucas Petit",
                "email": "lucas.petit@gmail.com",
                "telephone": "06 55 44 33 22",
                "source": "Salon professionnel",
                "interet": "Revente boutique",
                "statut": "qualifie",
                "date_creation": "2025-01-20",
                "score": 91,
            },
            {
                "id": 5,
                "nom": "Camille Roux",
                "email": "camille.roux@hotmail.fr",
                "telephone": "07 66 77 88 99",
                "source": "Facebook Ads",
                "interet": "Anti-âge",
                "statut": "nouveau",
                "date_creation": "2025-02-05",
                "score": 60,
            },
        ]
        self.next_id = 6

    def _ref(self) -> str:
        return f"[REF: QRY-{secrets.token_hex(3).upper()}]"

    def liste_leads(self, statut: str = "") -> str:
        """
        Liste tous les leads du CRM, avec possibilité de filtrer par statut.
        :param statut: Filtrer par statut (nouveau, contacte, qualifie, converti, perdu). Laisser vide pour tout afficher.
        :return: Liste des leads
        """
        results = self.leads
        if statut:
            results = [l for l in results if l["statut"] == statut]
        if not results:
            return f"Aucun lead trouvé. {self._ref()}"
        lines = []
        for l in results:
            lines.append(
                f"[#{l['id']}] {l['nom']} | {l['email']} | {l['telephone']}\n"
                f"  Source: {l['source']} | Intérêt: {l['interet']} | Statut: {l['statut']} | Score: {l['score']}/100\n"
                f"  Créé le: {l['date_creation']}"
            )
        return f"{len(results)} lead(s) trouvé(s):\n\n" + "\n\n".join(lines) + f"\n\n{self._ref()}"

    def rechercher_leads(self, query: str) -> str:
        """
        Recherche des leads par nom, email ou intérêt.
        :param query: Texte à rechercher dans le nom, email ou intérêt du lead
        :return: Leads correspondants
        """
        q = query.lower()
        results = [
            l
            for l in self.leads
            if q in l["nom"].lower()
            or q in l["email"].lower()
            or q in l["interet"].lower()
        ]
        if not results:
            return f"Aucun lead trouvé pour '{query}'. {self._ref()}"
        lines = []
        for l in results:
            lines.append(
                f"[#{l['id']}] {l['nom']} | {l['email']} | Statut: {l['statut']} | Intérêt: {l['interet']} | Score: {l['score']}/100"
            )
        return f"{len(results)} lead(s) trouvé(s):\n" + "\n".join(lines) + f"\n\n{self._ref()}"

    def ajouter_lead(
        self,
        nom: str,
        email: str,
        telephone: str = "",
        source: str = "Site web",
        interet: str = "",
    ) -> str:
        """
        Ajoute un nouveau lead dans le CRM.
        :param nom: Nom complet du prospect
        :param email: Adresse email
        :param telephone: Numéro de téléphone
        :param source: Source d'acquisition (Instagram Ads, Facebook Ads, Site web, Newsletter, Salon, etc.)
        :param interet: Centre d'intérêt ou produit recherché
        :return: Confirmation de l'ajout
        """
        lead = {
            "id": self.next_id,
            "nom": nom,
            "email": email,
            "telephone": telephone or "Non renseigné",
            "source": source,
            "interet": interet or "Non précisé",
            "statut": "nouveau",
            "date_creation": datetime.now().strftime("%Y-%m-%d"),
            "score": 50,
        }
        self.leads.append(lead)
        self.next_id += 1
        return f"Lead ajouté avec succès !\n[#{lead['id']}] {nom} ({email}) — Source: {source}, Statut: nouveau\n\n{self._ref()}"

    def modifier_statut_lead(self, email: str, statut: str) -> str:
        """
        Met à jour le statut d'un lead existant.
        :param email: Email du lead à modifier
        :param statut: Nouveau statut (nouveau, contacte, qualifie, converti, perdu)
        :return: Confirmation de la modification
        """
        valid = ["nouveau", "contacte", "qualifie", "converti", "perdu"]
        if statut not in valid:
            return f"Statut invalide. Valeurs possibles : {', '.join(valid)} {self._ref()}"
        for l in self.leads:
            if l["email"].lower() == email.lower():
                old = l["statut"]
                l["statut"] = statut
                if statut == "qualifie":
                    l["score"] = min(100, l["score"] + 15)
                elif statut == "converti":
                    l["score"] = 100
                return f"Lead mis à jour : {l['nom']}\nStatut : {old} → {statut} | Score : {l['score']}/100\n\n{self._ref()}"
        return f"Aucun lead trouvé avec l'email {email}. {self._ref()}"
