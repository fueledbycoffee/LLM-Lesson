"""
title: Catalogue Produits SoundPulse & Velora
description: Consultation du catalogue produits SoundPulse (casques, écouteurs, enceintes) et Velora (mode, accessoires) — rechercher, voir les détails et vérifier les stocks.
author: demo
version: 3.0.0
"""

import requests
from pydantic import BaseModel, Field


API = "https://belle-bio-api-production.up.railway.app"


class Tools:
    class Valves(BaseModel):
        api_url: str = Field(default=API, description="URL de l'API catalogue")

    def __init__(self):
        self.valves = self.Valves()

    @property
    def base(self):
        return self.valves.api_url.rstrip("/")

    def rechercher_produits(self, query: str, marque: str = "") -> str:
        """
        Recherche des produits SoundPulse ou Velora par nom, catégorie ou description.
        :param query: Texte à rechercher (nom de produit, type, caractéristique...)
        :param marque: Filtrer par marque (SoundPulse ou Velora). Laisser vide pour chercher dans les deux marques.
        :return: Produits correspondants
        """
        params = {"q": query}
        if marque:
            params["marque"] = marque
        r = requests.get(f"{self.base}/produits/search", params=params, timeout=10)
        data = r.json()
        if not data["produits"]:
            return f"Aucun produit trouvé pour '{query}'. [{data['ref']}]"
        lines = []
        for p in data["produits"]:
            stock = f"En stock ({p['stock']})" if p["stock"] > 0 else "RUPTURE"
            best = " ★" if p["best_seller"] else ""
            lines.append(f"[{p['id']}] {p['marque']} — {p['nom']} — {p['prix']:.2f} € | {stock}{best}")
        return f"{data['count']} produit(s) :\n" + "\n".join(lines) + f"\n\n[{data['ref']}]"

    def details_produit(self, id_produit: str) -> str:
        """
        Affiche les détails complets d'un produit SoundPulse ou Velora.
        :param id_produit: Référence du produit (ex: SP-PRO, VEL-STRIDE, CB-STARTER)
        :return: Fiche produit détaillée
        """
        r = requests.get(f"{self.base}/produits/{id_produit}", timeout=10)
        if r.status_code != 200:
            return f"Produit '{id_produit}' non trouvé."
        data = r.json()
        p = data["produit"]
        stock = f"En stock ({p['stock']})" if p["stock"] > 0 else "RUPTURE DE STOCK"
        best = "\n★ BEST-SELLER" if p["best_seller"] else ""
        return (
            f"━━━ {p['nom']} ━━━\nRéf : {p['id']}\nMarque : {p['marque']}\nCatégorie : {p['categorie']}\n"
            f"Prix : {p['prix']:.2f} €\nStock : {stock}\n"
            f"Description : {p['description']}\nSpecs : {p['specs'] or 'Voir fiche'}"
            f"{best}\n\n[{data['ref']}]"
        )

    def verifier_stock(self, id_produit: str) -> str:
        """
        Vérifie la disponibilité et le niveau de stock d'un produit SoundPulse ou Velora.
        :param id_produit: Référence du produit
        :return: Information de stock
        """
        r = requests.get(f"{self.base}/produits/{id_produit}/stock", timeout=10)
        if r.status_code != 200:
            return f"Produit '{id_produit}' non trouvé."
        data = r.json()
        status_map = {"rupture": "RUPTURE DE STOCK", "stock_faible": f"Stock faible — {data['stock']} unités", "disponible": f"En stock — {data['stock']} unités"}
        return f"{data['nom']} [{data['id']}] : {status_map[data['status']]} [{data['ref']}]"

    def produits_par_categorie(self, categorie: str = "", marque: str = "") -> str:
        """
        Liste les produits par catégorie, avec filtre optionnel par marque.
        :param categorie: Catégorie (Casques, Ecouteurs, Enceintes, Sneakers, Accessoires...). Vide = tout.
        :param marque: Filtrer par marque (SoundPulse ou Velora). Vide = toutes les marques.
        :return: Produits groupés par catégorie
        """
        params = {}
        if categorie:
            params["categorie"] = categorie
        if marque:
            params["marque"] = marque
        r = requests.get(f"{self.base}/produits", params=params, timeout=10)
        data = r.json()
        if not data["produits"]:
            return f"Aucun produit trouvé. [{data['ref']}]"
        lines = []
        current_cat = ""
        for p in data["produits"]:
            if p["categorie"] != current_cat:
                current_cat = p["categorie"]
                lines.append(f"\n━━━ {current_cat} ━━━")
            stock = "✓" if p["stock"] > 0 else "✗ Rupture"
            best = " ★" if p["best_seller"] else ""
            lines.append(f"  [{p['id']}] {p['marque']} — {p['nom']} — {p['prix']:.2f} € | {stock}{best}")
        return "\n".join(lines) + f"\n\n[{data['ref']}]"
