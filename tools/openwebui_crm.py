"""
title: CRM Leads FlowDesk
description: Gestion de leads B2B pour FlowDesk — ajouter, rechercher, qualifier des prospects entreprises.
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

    def liste_leads(self, statut: str = "") -> str:
        """
        Liste tous les leads B2B du CRM FlowDesk, avec possibilité de filtrer par statut.
        :param statut: Filtrer par statut (nouveau, contacte, qualifie, converti, perdu). Laisser vide pour tout afficher.
        :return: Liste des leads entreprises
        """
        params = {"statut": statut} if statut else {}
        r = requests.get(f"{self.base}/leads", params=params, timeout=10)
        data = r.json()
        if not data["leads"]:
            return f"Aucun lead trouvé. [{data['ref']}]"
        lines = []
        for l in data["leads"]:
            lines.append(
                f"[#{l['id']}] {l['nom']} | {l['email']} | {l['telephone']}\n"
                f"  Entreprise: {l['entreprise']} ({l['taille']})\n"
                f"  Source: {l['source']} | Intérêt: {l['interet']} | Statut: {l['statut']} | Score: {l['score']}/100"
            )
        return f"{data['count']} lead(s) trouvé(s):\n\n" + "\n\n".join(lines) + f"\n\n[{data['ref']}]"

    def rechercher_leads(self, query: str) -> str:
        """
        Recherche des leads B2B par nom, email, entreprise ou intérêt.
        :param query: Texte à rechercher dans le nom, email, entreprise ou intérêt du lead
        :return: Leads correspondants
        """
        r = requests.get(f"{self.base}/leads/search", params={"q": query}, timeout=10)
        data = r.json()
        if not data["leads"]:
            return f"Aucun lead trouvé pour '{query}'. [{data['ref']}]"
        lines = []
        for l in data["leads"]:
            lines.append(
                f"[#{l['id']}] {l['nom']} — {l['entreprise']} ({l['taille']})\n"
                f"  {l['email']} | Statut: {l['statut']} | Score: {l['score']}/100"
            )
        return f"{data['count']} lead(s) trouvé(s):\n" + "\n".join(lines) + f"\n\n[{data['ref']}]"

    def ajouter_lead(self, nom: str, email: str, entreprise: str = "", taille: str = "", telephone: str = "", source: str = "Site web", interet: str = "") -> str:
        """
        Ajoute un nouveau lead B2B dans le CRM FlowDesk.
        :param nom: Nom complet du contact
        :param email: Adresse email professionnelle
        :param entreprise: Nom de l'entreprise du prospect
        :param taille: Taille de l'entreprise (ex: TPE 5 pers., PME 50 pers., ETI 200 pers.)
        :param telephone: Numéro de téléphone
        :param source: Source d'acquisition (Landing page, Google Ads, Webinaire FlowDesk, Salon, LinkedIn, etc.)
        :param interet: Besoin ou fonctionnalité recherchée (ex: Scoring leads, Pipeline commercial, Integration Salesforce)
        :return: Confirmation de l'ajout
        """
        r = requests.post(f"{self.base}/leads", json={
            "nom": nom, "email": email, "telephone": telephone,
            "entreprise": entreprise, "taille": taille,
            "source": source, "interet": interet
        }, timeout=10)
        if r.status_code != 200:
            return f"Erreur : {r.json().get('detail', 'inconnue')}"
        data = r.json()
        l = data["lead"]
        return (
            f"Lead ajouté !\n[#{l['id']}] {l['nom']} ({l['email']})\n"
            f"Entreprise: {l['entreprise']} ({l['taille']})\n"
            f"Source: {l['source']}\n\n[{data['ref']}]"
        )

    def modifier_statut_lead(self, email: str, statut: str) -> str:
        """
        Met à jour le statut d'un lead B2B existant dans FlowDesk.
        :param email: Email du lead à modifier
        :param statut: Nouveau statut (nouveau, contacte, qualifie, converti, perdu)
        :return: Confirmation de la modification
        """
        r = requests.patch(f"{self.base}/leads/{email}/statut", json={"statut": statut}, timeout=10)
        if r.status_code != 200:
            return f"Erreur : {r.json().get('detail', 'inconnue')}"
        data = r.json()
        l = data["lead"]
        return f"Lead mis à jour : {l['nom']} ({l['entreprise']})\nStatut : {l['statut']} | Score : {l['score']}/100\n\n[{data['ref']}]"
