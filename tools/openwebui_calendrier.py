"""
title: Calendrier Demos FlowDesk
description: Gestion des rendez-vous de démonstration FlowDesk — planifier, consulter et annuler des démos.
author: demo
version: 3.0.0
"""

import requests
from pydantic import BaseModel, Field


API = "https://belle-bio-api-production.up.railway.app"


class Tools:
    class Valves(BaseModel):
        api_url: str = Field(default=API, description="URL de l'API FlowDesk")

    def __init__(self):
        self.valves = self.Valves()

    @property
    def base(self):
        return self.valves.api_url.rstrip("/")

    def liste_rdv(self, date: str = "") -> str:
        """
        Liste les rendez-vous de démonstration FlowDesk, optionnellement filtrés par date.
        :param date: Date au format AAAA-MM-JJ pour filtrer. Laisser vide pour tout voir.
        :return: Liste des démos planifiées
        """
        params = {"date": date} if date else {}
        r = requests.get(f"{self.base}/rdv", params=params, timeout=10)
        data = r.json()
        if not data["rdv"]:
            return f"Aucun rendez-vous trouvé. [{data['ref']}]"
        lines = []
        for rv in data["rdv"]:
            lines.append(
                f"[#{rv['id']}] {rv['date']} à {rv['heure']} ({rv['duree']} min) — {rv['type']}\n"
                f"  {rv['titre']} avec {rv['client']}\n"
                f"  Notes : {rv['notes']}"
            )
        return f"{data['count']} rendez-vous :\n\n" + "\n\n".join(lines) + f"\n\n[{data['ref']}]"

    def voir_disponibilites(self, date: str) -> str:
        """
        Affiche les créneaux disponibles pour planifier une démo FlowDesk à une date donnée.
        :param date: Date au format AAAA-MM-JJ
        :return: Créneaux disponibles pour la démo
        """
        r = requests.get(f"{self.base}/rdv/disponibilites/{date}", timeout=10)
        data = r.json()
        if not data["disponibles"]:
            return f"Aucun créneau disponible le {date}. [{data['ref']}]"
        return f"Créneaux disponibles le {date} :\n" + ", ".join(data["disponibles"]) + f"\n\n[{data['ref']}]"

    def creer_rdv(self, titre: str, date: str, heure: str, client: str, duree: int = 30, type_rdv: str = "visio", notes: str = "") -> str:
        """
        Planifie une nouvelle démonstration FlowDesk avec un prospect.
        :param titre: Objet de la démo (ex: Demo FlowDesk — scoring & pipelines)
        :param date: Date au format AAAA-MM-JJ
        :param heure: Heure au format HH:MM
        :param client: Nom du contact prospect
        :param duree: Durée en minutes (par défaut 30)
        :param type_rdv: Type de rendez-vous (visio, téléphone, présentiel)
        :param notes: Notes complémentaires (taille entreprise, besoins spécifiques, etc.)
        :return: Confirmation de création de la démo
        """
        r = requests.post(f"{self.base}/rdv", json={
            "titre": titre, "date": date, "heure": heure, "client": client,
            "duree": duree, "type_rdv": type_rdv, "notes": notes
        }, timeout=10)
        if r.status_code != 200:
            return f"Erreur : {r.json().get('detail', 'inconnue')}"
        data = r.json()
        rv = data["rdv"]
        return f"Démo planifiée !\n[#{rv['id']}] {rv['titre']}\n{rv['date']} à {rv['heure']} — {rv['type']}\nClient : {rv['client']}\n\n[{data['ref']}]"

    def annuler_rdv(self, id_rdv: int) -> str:
        """
        Annule une démonstration FlowDesk par son numéro.
        :param id_rdv: Numéro du rendez-vous à annuler
        :return: Confirmation d'annulation
        """
        r = requests.delete(f"{self.base}/rdv/{id_rdv}", timeout=10)
        if r.status_code != 200:
            return f"Erreur : {r.json().get('detail', 'inconnue')}"
        data = r.json()
        rv = data["rdv"]
        return f"Démo annulée : {rv['titre']} avec {rv['client']} le {rv['date']}. [{data['ref']}]"
