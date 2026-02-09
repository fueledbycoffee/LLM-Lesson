"""
title: Commandes & Paniers
description: Suivi des commandes et détection des paniers abandonnés — statut, historique, relance.
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
        self.commandes = [
            {
                "numero": "CMD-2025-0412",
                "client": "Sophie Martin",
                "email": "sophie.m@yahoo.fr",
                "date": "2025-01-15",
                "statut": "livrée",
                "total": 77.90,
                "articles": [
                    {"produit": "Sérum Éclat Vitamine C", "qte": 1, "prix": 34.90},
                    {"produit": "Crème Jour Certifiée Bio", "qte": 1, "prix": 32.00},
                    {"produit": "Échantillons offerts", "qte": 3, "prix": 0.00},
                ],
                "livraison": "Colissimo",
                "suivi": "6A12345678901",
            },
            {
                "numero": "CMD-2025-0498",
                "client": "Marie Dupont",
                "email": "marie.dupont@gmail.com",
                "date": "2025-02-03",
                "statut": "en préparation",
                "total": 59.90,
                "articles": [
                    {"produit": "Coffret Rituel Éclat", "qte": 1, "prix": 59.90},
                ],
                "livraison": "Chronopost",
                "suivi": "",
            },
            {
                "numero": "CMD-2025-0501",
                "client": "Lucas Petit",
                "email": "lucas.petit@gmail.com",
                "date": "2025-02-06",
                "statut": "en cours de livraison",
                "total": 2495.00,
                "articles": [
                    {"produit": "Coffret Rituel Éclat", "qte": 25, "prix": 1497.50},
                    {"produit": "Coffret Cocooning", "qte": 20, "prix": 998.00},
                ],
                "livraison": "Transporteur pro",
                "suivi": "PRO-98765",
            },
        ]
        self.paniers_abandonnes = [
            {
                "id": "PAN-001",
                "client": "Camille Roux",
                "email": "camille.roux@hotmail.fr",
                "date_abandon": "2025-02-07",
                "articles": [
                    {"produit": "Sérum Anti-âge Bio", "qte": 1, "prix": 45.00},
                    {"produit": "Crème Jour Certifiée Bio", "qte": 1, "prix": 32.00},
                ],
                "total": 77.00,
                "etape_abandon": "page paiement",
                "relance_envoyee": False,
            },
            {
                "id": "PAN-002",
                "client": "Anonyme",
                "email": "",
                "date_abandon": "2025-02-08",
                "articles": [
                    {"produit": "Huile Nuit Régénérante", "qte": 2, "prix": 84.00},
                ],
                "total": 84.00,
                "etape_abandon": "page panier",
                "relance_envoyee": False,
            },
            {
                "id": "PAN-003",
                "client": "Thomas Bernard",
                "email": "t.bernard@outlook.fr",
                "date_abandon": "2025-02-06",
                "articles": [
                    {"produit": "Coffret Cocooning", "qte": 1, "prix": 49.90},
                    {"produit": "Lait Corps Fleur de Coton", "qte": 2, "prix": 39.80},
                ],
                "total": 89.70,
                "etape_abandon": "choix livraison",
                "relance_envoyee": True,
            },
        ]

    def _ref(self) -> str:
        return f"[REF: QRY-{secrets.token_hex(3).upper()}]"

    def statut_commande(self, numero: str) -> str:
        """
        Vérifie le statut d'une commande par son numéro.
        :param numero: Numéro de commande (ex: CMD-2025-0412)
        :return: Détails et statut de la commande
        """
        for c in self.commandes:
            if c["numero"].upper() == numero.upper():
                articles = "\n".join(
                    f"  • {a['produit']} x{a['qte']} — {a['prix']:.2f} €"
                    for a in c["articles"]
                )
                suivi = f"\nN° suivi : {c['suivi']}" if c["suivi"] else ""
                return (
                    f"━━━ Commande {c['numero']} ━━━\n"
                    f"Client : {c['client']} ({c['email']})\n"
                    f"Date : {c['date']}\n"
                    f"Statut : {c['statut'].upper()}\n"
                    f"Articles :\n{articles}\n"
                    f"Total : {c['total']:.2f} €\n"
                    f"Livraison : {c['livraison']}{suivi}\n\n{self._ref()}"
                )
        return f"Commande '{numero}' non trouvée. Vérifiez le numéro (format : CMD-2025-XXXX). {self._ref()}"

    def historique_commandes(self, email: str) -> str:
        """
        Affiche l'historique de commandes d'un client par email.
        :param email: Email du client
        :return: Liste des commandes passées
        """
        results = [c for c in self.commandes if c["email"].lower() == email.lower()]
        if not results:
            return f"Aucune commande trouvée pour {email}. {self._ref()}"
        lines = []
        for c in results:
            nb_articles = sum(a["qte"] for a in c["articles"])
            lines.append(
                f"[{c['numero']}] {c['date']} | {c['statut']} | {nb_articles} article(s) | {c['total']:.2f} €"
            )
        total_global = sum(c["total"] for c in results)
        return (
            f"Historique de {results[0]['client']} ({email}) :\n"
            + "\n".join(lines)
            + f"\n\nTotal dépensé : {total_global:.2f} € sur {len(results)} commande(s)\n\n{self._ref()}"
        )

    def panier_abandonne(self, email: str) -> str:
        """
        Recherche un panier abandonné par email client.
        :param email: Email du client
        :return: Détails du panier abandonné
        """
        results = [p for p in self.paniers_abandonnes if p["email"].lower() == email.lower()]
        if not results:
            return f"Aucun panier abandonné trouvé pour {email}. {self._ref()}"
        lines = []
        for p in results:
            articles = ", ".join(f"{a['produit']} x{a['qte']}" for a in p["articles"])
            relance = "Oui" if p["relance_envoyee"] else "Non — relance possible"
            lines.append(
                f"[{p['id']}] Abandonné le {p['date_abandon']} à l'étape : {p['etape_abandon']}\n"
                f"  Articles : {articles}\n"
                f"  Total : {p['total']:.2f} €\n"
                f"  Relance envoyée : {relance}"
            )
        return f"Panier(s) abandonné(s) pour {results[0]['client']} :\n\n" + "\n\n".join(lines) + f"\n\n{self._ref()}"

    def liste_paniers_abandonnes(self) -> str:
        """
        Liste tous les paniers abandonnés récents, triés par valeur décroissante.
        :return: Tableau des paniers abandonnés avec potentiel de récupération
        """
        sorted_paniers = sorted(self.paniers_abandonnes, key=lambda p: p["total"], reverse=True)
        lines = []
        total_potentiel = 0
        for p in sorted_paniers:
            relance = "✓ Relancé" if p["relance_envoyee"] else "✗ À relancer"
            client = p["client"] if p["email"] else "Visiteur anonyme"
            lines.append(
                f"[{p['id']}] {client} | {p['total']:.2f} € | Étape : {p['etape_abandon']} | {relance}"
            )
            if not p["relance_envoyee"]:
                total_potentiel += p["total"]
        return (
            f"{len(sorted_paniers)} panier(s) abandonné(s) :\n"
            + "\n".join(lines)
            + f"\n\nPotentiel de récupération (non relancés) : {total_potentiel:.2f} €\n\n{self._ref()}"
        )

    def envoyer_relance(self, id_panier: str) -> str:
        """
        Simule l'envoi d'un email de relance pour un panier abandonné.
        :param id_panier: Identifiant du panier (ex: PAN-001)
        :return: Confirmation d'envoi de la relance
        """
        for p in self.paniers_abandonnes:
            if p["id"].upper() == id_panier.upper():
                if not p["email"]:
                    return f"Impossible de relancer {p['id']} : visiteur anonyme, pas d'email disponible. {self._ref()}"
                if p["relance_envoyee"]:
                    return f"Une relance a déjà été envoyée à {p['client']} ({p['email']}) pour le panier {p['id']}. {self._ref()}"
                p["relance_envoyee"] = True
                articles = ", ".join(a["produit"] for a in p["articles"])
                return (
                    f"Email de relance envoyé !\n"
                    f"Destinataire : {p['client']} ({p['email']})\n"
                    f"Panier : {articles}\n"
                    f"Montant : {p['total']:.2f} €\n"
                    f"Offre incluse : -10% avec le code RETOUR10\n\n{self._ref()}"
                )
        return f"Panier '{id_panier}' non trouvé. {self._ref()}"
