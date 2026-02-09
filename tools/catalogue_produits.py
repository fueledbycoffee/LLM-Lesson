"""
title: Catalogue Produits
description: Consultation du catalogue produits — rechercher, voir les détails et vérifier les stocks.
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
        self.produits = [
            {
                "id": "SOIN-001",
                "nom": "Sérum Éclat Vitamine C",
                "categorie": "Soins visage",
                "prix": 34.90,
                "stock": 124,
                "description": "Sérum concentré en vitamine C pure pour un teint lumineux et uniforme. Flacon 30ml.",
                "ingredients": "Vitamine C 15%, Acide Hyaluronique, Vitamine E",
                "best_seller": True,
            },
            {
                "id": "SOIN-002",
                "nom": "Crème Hydratante Intense",
                "categorie": "Soins visage",
                "prix": 28.50,
                "stock": 89,
                "description": "Crème riche pour peaux sèches à très sèches. Hydratation 24h. Pot 50ml.",
                "ingredients": "Beurre de karité, Aloe vera, Glycérine végétale",
                "best_seller": False,
            },
            {
                "id": "SOIN-003",
                "nom": "Huile Nuit Régénérante",
                "categorie": "Soins visage",
                "prix": 42.00,
                "stock": 56,
                "description": "Huile sèche de nuit aux 7 huiles précieuses. Régénère et nourrit. Flacon 30ml.",
                "ingredients": "Huile d'argan, Rose musquée, Jojoba, Onagre",
                "best_seller": True,
            },
            {
                "id": "CORPS-001",
                "nom": "Lait Corps Fleur de Coton",
                "categorie": "Soins corps",
                "prix": 19.90,
                "stock": 203,
                "description": "Lait corporel fondant au parfum délicat. Hydrate et adoucit. Flacon 200ml.",
                "ingredients": "Huile de coco, Extrait de coton, Allantoïne",
                "best_seller": False,
            },
            {
                "id": "CORPS-002",
                "nom": "Gommage Sucre & Vanille",
                "categorie": "Soins corps",
                "prix": 22.00,
                "stock": 0,
                "description": "Gommage gourmand au sucre de canne. Exfolie en douceur. Pot 200g.",
                "ingredients": "Sucre de canne, Huile de vanille, Beurre de cacao",
                "best_seller": False,
            },
            {
                "id": "COFFRET-001",
                "nom": "Coffret Rituel Éclat",
                "categorie": "Coffrets",
                "prix": 59.90,
                "stock": 45,
                "description": "Coffret 3 produits : Sérum Vitamine C + Crème Hydratante + Masque Éclat. Idéal pour offrir.",
                "ingredients": "",
                "best_seller": True,
            },
            {
                "id": "COFFRET-002",
                "nom": "Coffret Cocooning",
                "categorie": "Coffrets",
                "prix": 49.90,
                "stock": 32,
                "description": "Coffret détente : Lait Corps + Gommage + Bougie parfumée. Packaging cadeau inclus.",
                "ingredients": "",
                "best_seller": False,
            },
            {
                "id": "BIO-001",
                "nom": "Crème Jour Certifiée Bio",
                "categorie": "Gamme Bio",
                "prix": 32.00,
                "stock": 67,
                "description": "Crème de jour certifiée Cosmos Organic. Protège et hydrate. Pot 50ml.",
                "ingredients": "Aloe vera bio, Huile d'olive bio, Vitamine E naturelle",
                "best_seller": False,
            },
            {
                "id": "BIO-002",
                "nom": "Sérum Anti-âge Bio",
                "categorie": "Gamme Bio",
                "prix": 45.00,
                "stock": 38,
                "description": "Sérum anti-rides certifié bio à l'acide hyaluronique végétal. Flacon 30ml.",
                "ingredients": "Acide hyaluronique végétal, Extrait de rose bio, Squalane olive",
                "best_seller": True,
            },
        ]

    def _ref(self) -> str:
        return f"[REF: QRY-{secrets.token_hex(3).upper()}]"

    def rechercher_produits(self, query: str) -> str:
        """
        Recherche des produits par nom, catégorie ou description.
        :param query: Texte à rechercher (nom de produit, ingrédient, type de soin...)
        :return: Produits correspondants
        """
        q = query.lower()
        results = [
            p
            for p in self.produits
            if q in p["nom"].lower()
            or q in p["categorie"].lower()
            or q in p["description"].lower()
            or q in p["ingredients"].lower()
        ]
        if not results:
            return f"Aucun produit trouvé pour '{query}'. {self._ref()}"
        lines = []
        for p in results:
            stock_info = f"En stock ({p['stock']})" if p['stock'] > 0 else "RUPTURE DE STOCK"
            best = " ★ Best-seller" if p["best_seller"] else ""
            lines.append(f"[{p['id']}] {p['nom']} — {p['prix']:.2f} € | {stock_info}{best}")
        return f"{len(results)} produit(s) trouvé(s) :\n" + "\n".join(lines) + f"\n\n{self._ref()}"

    def details_produit(self, id_produit: str) -> str:
        """
        Affiche les détails complets d'un produit.
        :param id_produit: Référence du produit (ex: SOIN-001, COFFRET-001)
        :return: Fiche produit détaillée
        """
        for p in self.produits:
            if p["id"].upper() == id_produit.upper():
                stock_info = f"En stock ({p['stock']} unités)" if p['stock'] > 0 else "RUPTURE DE STOCK"
                best = "\n★ BEST-SELLER" if p["best_seller"] else ""
                return (
                    f"━━━ {p['nom']} ━━━\n"
                    f"Réf : {p['id']}\n"
                    f"Catégorie : {p['categorie']}\n"
                    f"Prix : {p['prix']:.2f} €\n"
                    f"Stock : {stock_info}\n"
                    f"Description : {p['description']}\n"
                    f"Ingrédients clés : {p['ingredients'] or 'Voir contenu du coffret'}"
                    f"{best}\n\n{self._ref()}"
                )
        return f"Produit '{id_produit}' non trouvé. Vérifiez la référence. {self._ref()}"

    def verifier_stock(self, id_produit: str) -> str:
        """
        Vérifie la disponibilité et le niveau de stock d'un produit.
        :param id_produit: Référence du produit
        :return: Information de stock
        """
        for p in self.produits:
            if p["id"].upper() == id_produit.upper():
                if p["stock"] == 0:
                    return f"{p['nom']} [{p['id']}] : RUPTURE DE STOCK. Réapprovisionnement prévu sous 5-7 jours ouvrés. {self._ref()}"
                elif p["stock"] < 20:
                    return f"{p['nom']} [{p['id']}] : Stock faible — {p['stock']} unités restantes. Commandez rapidement ! {self._ref()}"
                else:
                    return f"{p['nom']} [{p['id']}] : En stock — {p['stock']} unités disponibles. {self._ref()}"
        return f"Produit '{id_produit}' non trouvé. {self._ref()}"

    def produits_par_categorie(self, categorie: str = "") -> str:
        """
        Liste les produits par catégorie.
        :param categorie: Catégorie à afficher (Soins visage, Soins corps, Coffrets, Gamme Bio). Vide = toutes les catégories.
        :return: Produits groupés par catégorie
        """
        if categorie:
            results = [p for p in self.produits if categorie.lower() in p["categorie"].lower()]
            if not results:
                cats = sorted(set(p["categorie"] for p in self.produits))
                return f"Catégorie '{categorie}' non trouvée. Catégories disponibles : {', '.join(cats)} {self._ref()}"
            lines = [f"━━━ {results[0]['categorie']} ━━━"]
            for p in results:
                stock = "✓" if p["stock"] > 0 else "✗ Rupture"
                best = " ★" if p["best_seller"] else ""
                lines.append(f"  [{p['id']}] {p['nom']} — {p['prix']:.2f} € | {stock}{best}")
            return "\n".join(lines) + f"\n\n{self._ref()}"
        else:
            cats = {}
            for p in self.produits:
                cats.setdefault(p["categorie"], []).append(p)
            lines = []
            for cat, prods in cats.items():
                lines.append(f"\n━━━ {cat} ({len(prods)} produits) ━━━")
                for p in prods:
                    stock = "✓" if p["stock"] > 0 else "✗ Rupture"
                    best = " ★" if p["best_seller"] else ""
                    lines.append(f"  [{p['id']}] {p['nom']} — {p['prix']:.2f} € | {stock}{best}")
            return "\n".join(lines) + f"\n\n{self._ref()}"
