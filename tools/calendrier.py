"""
title: Calendrier RDV
description: Gestion de rendez-vous clients — créer, consulter et annuler des rendez-vous.
author: demo
version: 0.1.0
"""

import secrets
from pydantic import BaseModel


class Tools:
    class Valves(BaseModel):
        pass

    def __init__(self):
        self.valves = self.Valves()
        self.rdvs = [
            {
                "id": 1,
                "titre": "Démo produits soins visage",
                "date": "2025-02-10",
                "heure": "10:00",
                "duree": 30,
                "client": "Marie Dupont",
                "type": "visio",
                "notes": "Intéressée par la gamme anti-âge",
            },
            {
                "id": 2,
                "titre": "Présentation coffrets entreprise",
                "date": "2025-02-10",
                "heure": "14:00",
                "duree": 45,
                "client": "Lucas Petit",
                "type": "présentiel",
                "notes": "Commande groupée pour 50 coffrets",
            },
            {
                "id": 3,
                "titre": "Suivi satisfaction client",
                "date": "2025-02-11",
                "heure": "09:30",
                "duree": 20,
                "client": "Sophie Martin",
                "type": "téléphone",
                "notes": "Retour sur commande bio du 15/01",
            },
            {
                "id": 4,
                "titre": "Consultation personnalisée skincare",
                "date": "2025-02-12",
                "heure": "11:00",
                "duree": 30,
                "client": "Camille Roux",
                "type": "visio",
                "notes": "Premier contact — routine anti-âge",
            },
        ]
        self.next_id = 5
        self.creneaux = [
            "09:00", "09:30", "10:00", "10:30", "11:00", "11:30",
            "14:00", "14:30", "15:00", "15:30", "16:00", "16:30",
        ]

    def _ref(self) -> str:
        return f"[REF: QRY-{secrets.token_hex(3).upper()}]"

    def liste_rdv(self, date: str = "") -> str:
        """
        Liste les rendez-vous, optionnellement filtrés par date.
        :param date: Date au format AAAA-MM-JJ pour filtrer. Laisser vide pour tout voir.
        :return: Liste des rendez-vous
        """
        results = self.rdvs
        if date:
            results = [r for r in results if r["date"] == date]
        if not results:
            return f"Aucun rendez-vous trouvé{' pour le ' + date if date else ''}. {self._ref()}"
        lines = []
        for r in results:
            lines.append(
                f"[#{r['id']}] {r['date']} à {r['heure']} ({r['duree']} min) — {r['type']}\n"
                f"  {r['titre']} avec {r['client']}\n"
                f"  Notes : {r['notes']}"
            )
        return f"{len(results)} rendez-vous :\n\n" + "\n\n".join(lines) + f"\n\n{self._ref()}"

    def voir_disponibilites(self, date: str) -> str:
        """
        Affiche les créneaux disponibles pour une date donnée.
        :param date: Date au format AAAA-MM-JJ
        :return: Créneaux disponibles
        """
        pris = [
            r["heure"] for r in self.rdvs if r["date"] == date
        ]
        libres = [c for c in self.creneaux if c not in pris]
        if not libres:
            return f"Aucun créneau disponible le {date}. Journée complète. {self._ref()}"
        return f"Créneaux disponibles le {date} :\n" + ", ".join(libres) + f"\n\n{self._ref()}"

    def creer_rdv(
        self,
        titre: str,
        date: str,
        heure: str,
        client: str,
        duree: int = 30,
        type_rdv: str = "visio",
        notes: str = "",
    ) -> str:
        """
        Crée un nouveau rendez-vous.
        :param titre: Objet du rendez-vous
        :param date: Date au format AAAA-MM-JJ
        :param heure: Heure au format HH:MM
        :param client: Nom du client
        :param duree: Durée en minutes (par défaut 30)
        :param type_rdv: Type de rendez-vous (visio, téléphone, présentiel)
        :param notes: Notes complémentaires
        :return: Confirmation de création
        """
        conflit = [
            r for r in self.rdvs if r["date"] == date and r["heure"] == heure
        ]
        if conflit:
            return f"Conflit : un rendez-vous existe déjà le {date} à {heure} avec {conflit[0]['client']}. Veuillez choisir un autre créneau. {self._ref()}"
        rdv = {
            "id": self.next_id,
            "titre": titre,
            "date": date,
            "heure": heure,
            "duree": duree,
            "client": client,
            "type": type_rdv,
            "notes": notes or "Aucune note",
        }
        self.rdvs.append(rdv)
        self.next_id += 1
        return (
            f"Rendez-vous créé avec succès !\n"
            f"[#{rdv['id']}] {titre}\n"
            f"{date} à {heure} ({duree} min) — {type_rdv}\n"
            f"Client : {client}\n\n{self._ref()}"
        )

    def annuler_rdv(self, id_rdv: int) -> str:
        """
        Annule un rendez-vous par son numéro.
        :param id_rdv: Numéro du rendez-vous à annuler
        :return: Confirmation d'annulation
        """
        for i, r in enumerate(self.rdvs):
            if r["id"] == id_rdv:
                removed = self.rdvs.pop(i)
                return f"Rendez-vous annulé : {removed['titre']} avec {removed['client']} le {removed['date']} à {removed['heure']}. {self._ref()}"
        return f"Aucun rendez-vous trouvé avec l'ID #{id_rdv}. {self._ref()}"
