"""
title: Commandes & Paniers Velora / CloudBox
description: Suivi des commandes Velora et CloudBox, détection des paniers abandonnés Velora — statut, historique, relance.
author: demo
version: 3.0.0
"""

import requests
from pydantic import BaseModel, Field


API = "https://belle-bio-api-production.up.railway.app"


class Tools:
    class Valves(BaseModel):
        api_url: str = Field(default=API, description="URL de l'API commandes")

    def __init__(self):
        self.valves = self.Valves()

    @property
    def base(self):
        return self.valves.api_url.rstrip("/")

    def statut_commande(self, numero: str) -> str:
        """
        Vérifie le statut d'une commande Velora ou CloudBox par son numéro.
        :param numero: Numéro de commande (ex: VEL-2025-0933, CB-2025-1402)
        :return: Détails et statut de la commande
        """
        r = requests.get(f"{self.base}/commandes/{numero}", timeout=10)
        if r.status_code != 200:
            return f"Commande '{numero}' non trouvée."
        data = r.json()
        c = data["commande"]
        articles = "\n".join(f"  • {a['produit']} x{a['qte']} — {a['prix']:.2f} €" for a in c["articles"])
        suivi = f"\nN° suivi : {c['suivi']}" if c["suivi"] else ""
        return (
            f"━━━ Commande {c['numero']} ({c['marque']}) ━━━\n"
            f"Client : {c['client']} ({c['email']})\nDate : {c['date']}\n"
            f"Statut : {c['statut'].upper()}\nArticles :\n{articles}\n"
            f"Total : {c['total']:.2f} €\nLivraison : {c['livraison']}{suivi}\n\n[{data['ref']}]"
        )

    def historique_commandes(self, email: str, marque: str = "") -> str:
        """
        Affiche l'historique de commandes d'un client par email, avec filtre optionnel par marque.
        :param email: Email du client
        :param marque: Filtrer par marque (Velora ou CloudBox). Vide = toutes les marques.
        :return: Liste des commandes passées
        """
        r = requests.get(f"{self.base}/commandes/client/{email}", timeout=10)
        if r.status_code != 200:
            return f"Aucune commande trouvée pour {email}."
        data = r.json()
        commandes = data["commandes"]
        if marque:
            commandes = [c for c in commandes if c.get("marque", "").lower() == marque.lower()]
        if not commandes:
            return f"Aucune commande {marque} trouvée pour {email}. [{data['ref']}]"
        lines = []
        for c in commandes:
            nb = sum(a["qte"] for a in c["articles"])
            lines.append(f"[{c['numero']}] {c['marque']} | {c['date']} | {c['statut']} | {nb} article(s) | {c['total']:.2f} €")
        total = sum(c["total"] for c in commandes)
        return (
            f"Historique ({email}) :\n" + "\n".join(lines)
            + f"\n\nTotal dépensé : {total:.2f} €\n\n[{data['ref']}]"
        )

    def liste_commandes(self, marque: str = "") -> str:
        """
        Liste toutes les commandes récentes, avec filtre optionnel par marque.
        :param marque: Filtrer par marque (Velora ou CloudBox). Vide = toutes les marques.
        :return: Liste des commandes
        """
        params = {}
        if marque:
            params["marque"] = marque
        r = requests.get(f"{self.base}/commandes", params=params, timeout=10)
        data = r.json()
        if not data["commandes"]:
            return f"Aucune commande trouvée. [{data['ref']}]"
        lines = []
        for c in data["commandes"]:
            nb = sum(a["qte"] for a in c["articles"])
            lines.append(f"[{c['numero']}] {c['marque']} | {c['client']} | {c['date']} | {c['statut']} | {nb} art. | {c['total']:.2f} €")
        return f"{data['count']} commande(s) :\n" + "\n".join(lines) + f"\n\n[{data['ref']}]"

    def panier_abandonne(self, email: str) -> str:
        """
        Recherche un panier abandonné Velora par email client.
        :param email: Email du client
        :return: Détails du panier abandonné
        """
        r = requests.get(f"{self.base}/paniers/client/{email}", timeout=10)
        if r.status_code != 200:
            return f"Aucun panier abandonné pour {email}."
        data = r.json()
        lines = []
        for p in data["paniers"]:
            articles = ", ".join(f"{a['produit']} x{a['qte']}" for a in p["articles"])
            relance = "Oui" if p["relance_envoyee"] else "Non — relance possible"
            lines.append(
                f"[{p['id']}] {p['marque']} — Abandonné le {p['date_abandon']} — étape : {p['etape_abandon']}\n"
                f"  Articles : {articles}\n  Total : {p['total']:.2f} € | Relance : {relance}"
            )
        return "\n\n".join(lines) + f"\n\n[{data['ref']}]"

    def liste_paniers_abandonnes(self, marque: str = "") -> str:
        """
        Liste tous les paniers abandonnés Velora récents, triés par valeur.
        :param marque: Filtrer par marque (ex: Velora). Vide = tous les paniers.
        :return: Paniers abandonnés avec potentiel de récupération
        """
        params = {}
        if marque:
            params["marque"] = marque
        r = requests.get(f"{self.base}/paniers", params=params, timeout=10)
        data = r.json()
        lines = []
        for p in data["paniers"]:
            relance = "✓ Relancé" if p["relance_envoyee"] else "✗ À relancer"
            client = p["client"] if p["email"] else "Visiteur anonyme"
            lines.append(f"[{p['id']}] {p['marque']} | {client} | {p['total']:.2f} € | {p['etape_abandon']} | {relance}")
        return (
            f"{data['count']} panier(s) abandonné(s) :\n" + "\n".join(lines)
            + f"\n\nPotentiel récupération : {data['potentiel_recuperation']:.2f} €\n\n[{data['ref']}]"
        )

    def envoyer_relance(self, id_panier: str) -> str:
        """
        Envoie un email de relance pour un panier abandonné Velora, avec le code promo BIENVENUE10.
        :param id_panier: Identifiant du panier (ex: PAN-001)
        :return: Confirmation d'envoi avec code promo BIENVENUE10
        """
        r = requests.post(f"{self.base}/paniers/{id_panier}/relance", timeout=10)
        if r.status_code != 200:
            return f"Erreur : {r.json().get('detail', 'inconnue')}"
        data = r.json()
        p = data["panier"]
        articles = ", ".join(a["produit"] for a in p["articles"])
        return (
            f"Relance envoyée !\nDestinataire : {p['client']} ({p['email']})\n"
            f"Panier : {articles}\nMontant : {p['total']:.2f} €\n"
            f"Code promo : {data['code_promo']}\n\n[{data['ref']}]"
        )
