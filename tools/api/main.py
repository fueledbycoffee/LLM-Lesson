"""
Marketing Chatbot Tools API
FastAPI + SQLite. Deploy on Railway.
4 businesses: FlowDesk (SaaS), SoundPulse (Audio), Velora (Mode), CloudBox (Cloud)
Endpoints: /leads, /rdv, /produits, /commandes, /paniers
"""

import secrets
import sqlite3
from contextlib import contextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Marketing Chatbot Tools API", version="2.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

DB_PATH = Path(__file__).parent / "data.db"


# ── DB helpers ──────────────────────────────────────────────────────────────

@contextmanager
def get_db():
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def ref():
    return f"QRY-{secrets.token_hex(3).upper()}"


# ── Init DB + seed data ────────────────────────────────────────────────────

def init_db():
    with get_db() as db:
        db.executescript("""
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                telephone TEXT DEFAULT '',
                entreprise TEXT DEFAULT '',
                taille TEXT DEFAULT '',
                source TEXT DEFAULT 'Site web',
                interet TEXT DEFAULT '',
                statut TEXT DEFAULT 'nouveau',
                score INTEGER DEFAULT 50,
                date_creation TEXT DEFAULT (date('now'))
            );

            CREATE TABLE IF NOT EXISTS rdv (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titre TEXT NOT NULL,
                date TEXT NOT NULL,
                heure TEXT NOT NULL,
                duree INTEGER DEFAULT 30,
                client TEXT NOT NULL,
                type TEXT DEFAULT 'visio',
                notes TEXT DEFAULT ''
            );

            CREATE TABLE IF NOT EXISTS produits (
                id TEXT PRIMARY KEY,
                nom TEXT NOT NULL,
                marque TEXT NOT NULL DEFAULT '',
                categorie TEXT NOT NULL,
                prix REAL NOT NULL,
                stock INTEGER DEFAULT 0,
                description TEXT DEFAULT '',
                specs TEXT DEFAULT '',
                best_seller INTEGER DEFAULT 0
            );

            CREATE TABLE IF NOT EXISTS commandes (
                numero TEXT PRIMARY KEY,
                marque TEXT NOT NULL DEFAULT '',
                client TEXT NOT NULL,
                email TEXT NOT NULL,
                date TEXT NOT NULL,
                statut TEXT NOT NULL,
                total REAL NOT NULL,
                livraison TEXT DEFAULT '',
                suivi TEXT DEFAULT ''
            );

            CREATE TABLE IF NOT EXISTS commande_articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero_commande TEXT NOT NULL,
                produit TEXT NOT NULL,
                qte INTEGER DEFAULT 1,
                prix REAL NOT NULL,
                FOREIGN KEY (numero_commande) REFERENCES commandes(numero)
            );

            CREATE TABLE IF NOT EXISTS paniers (
                id TEXT PRIMARY KEY,
                marque TEXT NOT NULL DEFAULT '',
                client TEXT NOT NULL,
                email TEXT DEFAULT '',
                date_abandon TEXT NOT NULL,
                total REAL NOT NULL,
                etape_abandon TEXT NOT NULL,
                relance_envoyee INTEGER DEFAULT 0
            );

            CREATE TABLE IF NOT EXISTS panier_articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_panier TEXT NOT NULL,
                produit TEXT NOT NULL,
                qte INTEGER DEFAULT 1,
                prix REAL NOT NULL,
                FOREIGN KEY (id_panier) REFERENCES paniers(id)
            );
        """)

        # Seed only if empty
        count = db.execute("SELECT COUNT(*) FROM leads").fetchone()[0]
        if count == 0:
            seed_data(db)


def seed_data(db):
    # ══════════════════════════════════════════════════════════════════════
    # BRIEF 1 — FlowDesk (SaaS CRM) → Leads + RDV
    # ══════════════════════════════════════════════════════════════════════
    db.executemany(
        "INSERT INTO leads (nom,email,telephone,entreprise,taille,source,interet,statut,score,date_creation) VALUES (?,?,?,?,?,?,?,?,?,?)", [
        ("Claire Moreau",   "c.moreau@digitalpulse.fr",  "06 12 34 56 78", "DigitalPulse",    "PME 25 pers.",   "Landing page",        "Scoring leads + automatisation", "nouveau",  72, "2025-02-01"),
        ("Antoine Leroy",   "a.leroy@nextstep-rh.com",   "06 98 76 54 32", "NextStep RH",     "ETI 120 pers.",  "Google Ads",          "Pipeline commercial + reporting", "contacte", 45, "2025-01-28"),
        ("Sophie Marchand", "s.marchand@greenlogistic.fr","07 11 22 33 44", "GreenLogistic",   "PME 40 pers.",   "Webinaire FlowDesk",  "Integration Salesforce",          "qualifie", 89, "2025-01-15"),
        ("Thomas Renard",   "t.renard@craftbeer.co",     "06 55 44 33 22", "CraftBeer & Co",  "TPE 8 pers.",    "Salon E-marketing",   "Plan Starter, emailing",          "qualifie", 91, "2025-01-20"),
        ("Nadia Benzema",   "n.benzema@solartek.io",     "07 66 77 88 99", "SolarTek",        "ETI 200 pers.",  "LinkedIn Ads",        "Enterprise, SSO, onboarding",     "nouveau",  60, "2025-02-05"),
    ])

    db.executemany("INSERT INTO rdv (titre,date,heure,duree,client,type,notes) VALUES (?,?,?,?,?,?,?)", [
        ("Demo FlowDesk — scoring & pipelines",     "2025-02-10", "10:00", 30, "Claire Moreau",   "visio",      "PME 25 pers. Interet scoring + automatisation nurturing"),
        ("Presentation Enterprise + SSO",            "2025-02-10", "14:00", 45, "Nadia Benzema",   "visio",      "ETI 200 pers. Besoin SSO SAML + data residency EU"),
        ("Suivi post-demo — integration Salesforce", "2025-02-11", "09:30", 20, "Sophie Marchand", "telephone",  "A teste le plan Pro en trial. Questions sur API + migration"),
        ("Premier contact — plan Starter",           "2025-02-12", "11:00", 30, "Thomas Renard",   "visio",      "TPE 8 pers. Budget serre. Cherche emailing simple"),
    ])

    # ══════════════════════════════════════════════════════════════════════
    # BRIEF 2 — SoundPulse (Audio) → Produits
    # ══════════════════════════════════════════════════════════════════════
    db.executemany(
        "INSERT INTO produits (id,nom,marque,categorie,prix,stock,description,specs,best_seller) VALUES (?,?,?,?,?,?,?,?,?)", [
        ("SP-MINI",   "SoundPulse Mini",   "SoundPulse", "Ecouteurs",  49.00,  312, "Ecouteurs true wireless ultra-legers. Quotidien, transports.",                          "Bluetooth 5.3, 12h autonomie, IPX4, 42g, micro appels",                    0),
        ("SP-PRO",    "SoundPulse Pro",    "SoundPulse", "Casques",   129.00,  187, "Casque supra-auriculaire pliable. Travail, musique, appels video.",                      "ANC 3 niveaux, 35h autonomie, Hi-Res, aptX/LDAC, double micro",           1),
        ("SP-STUDIO", "SoundPulse Studio", "SoundPulse", "Casques",   249.00,   64, "Casque circum-auriculaire premium. Studio, gaming, ecoute critique.",                    "Son spatial 7.1, ANC premium, latence <40ms, micro boom, USB-C audio",     1),
        ("SP-SPORT",  "SoundPulse Sport",  "SoundPulse", "Ecouteurs",  79.00,  245, "Ecouteurs sport avec crochets d'oreille. Running, salle.",                               "IP67, 10h autonomie, 28g, mode transparence, crochets securises",          0),
        ("SP-KIDS",   "SoundPulse Kids",   "SoundPulse", "Casques",    39.00,  156, "Casque filaire pour enfants 6-12 ans. Volume limite 85dB.",                               "Filaire jack 3.5mm, 85dB max OMS, quasi-incassable, stickers inclus",      0),
        ("SP-TRAVEL", "SoundPulse Travel", "SoundPulse", "Casques",   169.00,   89, "Casque pliable ultra-compact pour voyageurs. ANC optimise avion/train.",                  "ANC avion -95%, 30h autonomie, pliable, etui rigide, adaptateur avion",    1),
    ])

    # ══════════════════════════════════════════════════════════════════════
    # BRIEF 3 — Velora (Mode durable) → Produits + Commandes + Paniers
    # ══════════════════════════════════════════════════════════════════════
    db.executemany(
        "INSERT INTO produits (id,nom,marque,categorie,prix,stock,description,specs,best_seller) VALUES (?,?,?,?,?,?,?,?,?)", [
        ("VEL-NOMAD",   "Sac a dos NOMAD",       "Velora", "Sacs",         89.00, 134, "Sac a dos 22L en polyester 100% recycle + cuir vegetal. Laptop 15 pouces.",       "Fabrique au Portugal, certifie GRS, poche anti-vol dorsale",           0),
        ("VEL-STRIDE",  "Sneakers STRIDE",        "Velora", "Chaussures",  129.00, 0,   "Sneakers en cuir de raisin, semelle caoutchouc naturel. Design minimaliste.",     "Fabrique en Italie, bilan carbone -60%, tailles 36-46",               1),
        ("VEL-ESSENT",  "T-shirt ESSENTIEL",      "Velora", "Vetements",    39.00, 423, "T-shirt coton bio GOTS 180g/m2. Coupe moderne, garanti 50 lavages.",              "Fabrique au Portugal, OEKO-TEX 100, XS-XXL, 6 coloris",              1),
        ("VEL-URBAN",   "Veste URBAN",            "Velora", "Vetements",   189.00,  47, "Veste 3-en-1 nylon recycle. Impermeable + coupe-vent + polaire amovible.",         "Fabrique en Roumanie, colonne 10 000mm, poches etanches, XS-XXL",     0),
        ("VEL-COMPACT", "Portefeuille COMPACT",   "Velora", "Accessoires",  49.00, 198, "Portefeuille ultra-fin en cuir de cactus Desserto. 6 cartes + billets.",           "Fabrique en Espagne, <1cm epaisseur, emballage zero-dechet",          0),
        ("VEL-WOOL",    "Bonnet WOOL",            "Velora", "Accessoires",  29.00, 267, "Bonnet laine merinos mulesing-free + doublure coton bio. Unisexe.",                "Fabrique en Ecosse, certifie RWS, thermoregulateur, taille unique",   0),
    ])

    db.executemany("INSERT INTO commandes (numero,marque,client,email,date,statut,total,livraison,suivi) VALUES (?,?,?,?,?,?,?,?,?)", [
        ("VEL-2025-0847", "Velora", "Julie Lambert",     "j.lambert@gmail.com",     "2025-01-22", "livree",              168.00, "Colissimo",  "6A12345678901"),
        ("VEL-2025-0912", "Velora", "Marc Dubois",       "m.dubois@outlook.fr",     "2025-02-03", "en preparation",      228.00, "Chronopost", ""),
        ("VEL-2025-0933", "Velora", "Emma Fournier",     "e.fournier@yahoo.fr",     "2025-02-06", "en cours de livraison", 89.00, "Colissimo",  "6A98765432109"),
    ])
    db.executemany("INSERT INTO commande_articles (numero_commande,produit,qte,prix) VALUES (?,?,?,?)", [
        ("VEL-2025-0847", "T-shirt ESSENTIEL",    2, 78.00),
        ("VEL-2025-0847", "Sac a dos NOMAD",      1, 89.00),
        ("VEL-2025-0912", "Sneakers STRIDE",       1, 129.00),
        ("VEL-2025-0912", "T-shirt ESSENTIEL",    1, 39.00),
        ("VEL-2025-0912", "Portefeuille COMPACT", 1, 49.00),
        ("VEL-2025-0933", "Sac a dos NOMAD",      1, 89.00),
    ])

    db.executemany("INSERT INTO paniers (id,marque,client,email,date_abandon,total,etape_abandon,relance_envoyee) VALUES (?,?,?,?,?,?,?,?)", [
        ("PAN-001", "Velora", "Luc Martin",     "l.martin@gmail.com",    "2025-02-07", 218.00, "page paiement",   0),
        ("PAN-002", "Velora", "Anonyme",        "",                      "2025-02-08",  89.00, "page panier",     0),
        ("PAN-003", "Velora", "Ines Chabane",   "i.chabane@hotmail.fr",  "2025-02-06", 168.00, "choix livraison", 1),
    ])
    db.executemany("INSERT INTO panier_articles (id_panier,produit,qte,prix) VALUES (?,?,?,?)", [
        ("PAN-001", "Veste URBAN",         1, 189.00),
        ("PAN-001", "Bonnet WOOL",         1, 29.00),
        ("PAN-002", "Sac a dos NOMAD",     1, 89.00),
        ("PAN-003", "Sneakers STRIDE",     1, 129.00),
        ("PAN-003", "T-shirt ESSENTIEL",   1, 39.00),
    ])

    # ══════════════════════════════════════════════════════════════════════
    # BRIEF 4 — CloudBox (Cloud SaaS) → Commandes (abonnements)
    # ══════════════════════════════════════════════════════════════════════
    db.executemany("INSERT INTO commandes (numero,marque,client,email,date,statut,total,livraison,suivi) VALUES (?,?,?,?,?,?,?,?,?)", [
        ("CB-2025-1201", "CloudBox", "Pierre Garnier",  "p.garnier@freelance.dev",  "2025-01-05", "active",            47.90,  "Plan Perso annuel",   ""),
        ("CB-2025-1344", "CloudBox", "Startup Hive SAS","contact@startuphive.io",   "2025-01-18", "active",           575.40,  "Plan Team annuel x6", ""),
        ("CB-2025-1402", "CloudBox", "Lea Rousseau",    "l.rousseau@agence-nova.fr","2025-02-01", "en attente paiement", 19.99,"Plan Business mensuel",""),
    ])
    db.executemany("INSERT INTO commande_articles (numero_commande,produit,qte,prix) VALUES (?,?,?,?)", [
        ("CB-2025-1201", "CloudBox Perso (annuel)",       1, 47.90),
        ("CB-2025-1344", "CloudBox Team (annuel x6)",     6, 575.40),
        ("CB-2025-1402", "CloudBox Business (mensuel)",   1, 19.99),
    ])


# ── Startup ─────────────────────────────────────────────────────────────────

@app.on_event("startup")
def startup():
    init_db()


# ── Pydantic models ─────────────────────────────────────────────────────────

class LeadCreate(BaseModel):
    nom: str
    email: str
    telephone: str = ""
    entreprise: str = ""
    taille: str = ""
    source: str = "Site web"
    interet: str = ""

class LeadUpdateStatut(BaseModel):
    statut: str

class RdvCreate(BaseModel):
    titre: str
    date: str
    heure: str
    client: str
    duree: int = 30
    type_rdv: str = "visio"
    notes: str = ""

class RelanceRequest(BaseModel):
    id_panier: str


# ══════════════════════════════════════════════════════════════════════════════
# LEADS
# ══════════════════════════════════════════════════════════════════════════════

@app.get("/leads")
def liste_leads(statut: Optional[str] = None):
    with get_db() as db:
        if statut:
            rows = db.execute("SELECT * FROM leads WHERE statut = ?", (statut,)).fetchall()
        else:
            rows = db.execute("SELECT * FROM leads").fetchall()
    return {"ref": ref(), "count": len(rows), "leads": [dict(r) for r in rows]}


@app.get("/leads/search")
def rechercher_leads(q: str):
    with get_db() as db:
        rows = db.execute(
            "SELECT * FROM leads WHERE LOWER(nom) LIKE ? OR LOWER(email) LIKE ? OR LOWER(interet) LIKE ?",
            (f"%{q.lower()}%",) * 3
        ).fetchall()
    return {"ref": ref(), "count": len(rows), "leads": [dict(r) for r in rows]}


@app.post("/leads")
def ajouter_lead(lead: LeadCreate):
    with get_db() as db:
        try:
            db.execute(
                "INSERT INTO leads (nom, email, telephone, entreprise, taille, source, interet) VALUES (?,?,?,?,?,?,?)",
                (lead.nom, lead.email, lead.telephone, lead.entreprise, lead.taille, lead.source, lead.interet)
            )
            new = db.execute("SELECT * FROM leads WHERE email = ?", (lead.email,)).fetchone()
        except sqlite3.IntegrityError:
            raise HTTPException(400, "Un lead avec cet email existe déjà.")
    return {"ref": ref(), "message": "Lead ajouté", "lead": dict(new)}


@app.patch("/leads/{email}/statut")
def modifier_statut(email: str, body: LeadUpdateStatut):
    valid = ["nouveau", "contacte", "qualifie", "converti", "perdu"]
    if body.statut not in valid:
        raise HTTPException(400, f"Statut invalide. Valeurs : {', '.join(valid)}")
    with get_db() as db:
        row = db.execute("SELECT * FROM leads WHERE LOWER(email) = ?", (email.lower(),)).fetchone()
        if not row:
            raise HTTPException(404, f"Lead {email} non trouvé.")
        new_score = row["score"]
        if body.statut == "qualifie":
            new_score = min(100, new_score + 15)
        elif body.statut == "converti":
            new_score = 100
        db.execute("UPDATE leads SET statut = ?, score = ? WHERE LOWER(email) = ?",
                    (body.statut, new_score, email.lower()))
        updated = db.execute("SELECT * FROM leads WHERE LOWER(email) = ?", (email.lower(),)).fetchone()
    return {"ref": ref(), "message": "Statut mis à jour", "lead": dict(updated)}


# ══════════════════════════════════════════════════════════════════════════════
# CALENDRIER
# ══════════════════════════════════════════════════════════════════════════════

CRENEAUX = ["09:00","09:30","10:00","10:30","11:00","11:30","14:00","14:30","15:00","15:30","16:00","16:30"]

@app.get("/rdv")
def liste_rdv(date: Optional[str] = None):
    with get_db() as db:
        if date:
            rows = db.execute("SELECT * FROM rdv WHERE date = ?", (date,)).fetchall()
        else:
            rows = db.execute("SELECT * FROM rdv ORDER BY date, heure").fetchall()
    return {"ref": ref(), "count": len(rows), "rdv": [dict(r) for r in rows]}


@app.get("/rdv/disponibilites/{date}")
def voir_disponibilites(date: str):
    with get_db() as db:
        pris = [r["heure"] for r in db.execute("SELECT heure FROM rdv WHERE date = ?", (date,)).fetchall()]
    libres = [c for c in CRENEAUX if c not in pris]
    return {"ref": ref(), "date": date, "disponibles": libres, "occupes": pris}


@app.post("/rdv")
def creer_rdv(rdv: RdvCreate):
    with get_db() as db:
        conflit = db.execute("SELECT * FROM rdv WHERE date = ? AND heure = ?", (rdv.date, rdv.heure)).fetchone()
        if conflit:
            raise HTTPException(409, f"Conflit : créneau {rdv.date} {rdv.heure} pris par {conflit['client']}")
        db.execute(
            "INSERT INTO rdv (titre, date, heure, duree, client, type, notes) VALUES (?,?,?,?,?,?,?)",
            (rdv.titre, rdv.date, rdv.heure, rdv.duree, rdv.client, rdv.type_rdv, rdv.notes)
        )
        new = db.execute("SELECT * FROM rdv WHERE date = ? AND heure = ?", (rdv.date, rdv.heure)).fetchone()
    return {"ref": ref(), "message": "RDV créé", "rdv": dict(new)}


@app.delete("/rdv/{id_rdv}")
def annuler_rdv(id_rdv: int):
    with get_db() as db:
        row = db.execute("SELECT * FROM rdv WHERE id = ?", (id_rdv,)).fetchone()
        if not row:
            raise HTTPException(404, f"RDV #{id_rdv} non trouvé.")
        db.execute("DELETE FROM rdv WHERE id = ?", (id_rdv,))
    return {"ref": ref(), "message": "RDV annulé", "rdv": dict(row)}


# ══════════════════════════════════════════════════════════════════════════════
# PRODUITS
# ══════════════════════════════════════════════════════════════════════════════

@app.get("/produits")
def liste_produits(categorie: Optional[str] = None, marque: Optional[str] = None):
    with get_db() as db:
        clauses, params = [], []
        if categorie:
            clauses.append("LOWER(categorie) LIKE ?"); params.append(f"%{categorie.lower()}%")
        if marque:
            clauses.append("LOWER(marque) = ?"); params.append(marque.lower())
        where = " WHERE " + " AND ".join(clauses) if clauses else ""
        rows = db.execute(f"SELECT * FROM produits{where} ORDER BY marque, categorie, nom", params).fetchall()
    return {"ref": ref(), "count": len(rows), "produits": [dict(r) for r in rows]}


@app.get("/produits/search")
def rechercher_produits(q: str, marque: Optional[str] = None):
    with get_db() as db:
        base = "SELECT * FROM produits WHERE (LOWER(nom) LIKE ? OR LOWER(description) LIKE ? OR LOWER(specs) LIKE ? OR LOWER(categorie) LIKE ?)"
        params = [f"%{q.lower()}%"] * 4
        if marque:
            base += " AND LOWER(marque) = ?"
            params.append(marque.lower())
        rows = db.execute(base, params).fetchall()
    return {"ref": ref(), "count": len(rows), "produits": [dict(r) for r in rows]}


@app.get("/produits/{id_produit}")
def details_produit(id_produit: str):
    with get_db() as db:
        row = db.execute("SELECT * FROM produits WHERE UPPER(id) = ?", (id_produit.upper(),)).fetchone()
    if not row:
        raise HTTPException(404, f"Produit {id_produit} non trouvé.")
    return {"ref": ref(), "produit": dict(row)}


@app.get("/produits/{id_produit}/stock")
def verifier_stock(id_produit: str):
    with get_db() as db:
        row = db.execute("SELECT id, nom, stock FROM produits WHERE UPPER(id) = ?", (id_produit.upper(),)).fetchone()
    if not row:
        raise HTTPException(404, f"Produit {id_produit} non trouvé.")
    d = dict(row)
    if d["stock"] == 0:
        d["status"] = "rupture"
    elif d["stock"] < 20:
        d["status"] = "stock_faible"
    else:
        d["status"] = "disponible"
    return {"ref": ref(), **d}


# ══════════════════════════════════════════════════════════════════════════════
# COMMANDES
# ══════════════════════════════════════════════════════════════════════════════

def _commande_with_articles(db, cmd):
    d = dict(cmd)
    articles = db.execute("SELECT produit, qte, prix FROM commande_articles WHERE numero_commande = ?", (d["numero"],)).fetchall()
    d["articles"] = [dict(a) for a in articles]
    return d


@app.get("/commandes")
def liste_commandes(marque: Optional[str] = None):
    with get_db() as db:
        if marque:
            rows = db.execute("SELECT * FROM commandes WHERE LOWER(marque) = ? ORDER BY date DESC", (marque.lower(),)).fetchall()
        else:
            rows = db.execute("SELECT * FROM commandes ORDER BY date DESC").fetchall()
        commandes = [_commande_with_articles(db, r) for r in rows]
    return {"ref": ref(), "count": len(commandes), "commandes": commandes}


@app.get("/commandes/{numero}")
def statut_commande(numero: str):
    with get_db() as db:
        row = db.execute("SELECT * FROM commandes WHERE UPPER(numero) = ?", (numero.upper(),)).fetchone()
        if not row:
            raise HTTPException(404, f"Commande {numero} non trouvée.")
        return {"ref": ref(), "commande": _commande_with_articles(db, row)}


@app.get("/commandes/client/{email}")
def historique_commandes(email: str):
    with get_db() as db:
        rows = db.execute("SELECT * FROM commandes WHERE LOWER(email) = ? ORDER BY date DESC", (email.lower(),)).fetchall()
        if not rows:
            raise HTTPException(404, f"Aucune commande pour {email}.")
        commandes = [_commande_with_articles(db, r) for r in rows]
    total = sum(c["total"] for c in commandes)
    return {"ref": ref(), "count": len(commandes), "total_depense": total, "commandes": commandes}


# ══════════════════════════════════════════════════════════════════════════════
# PANIERS ABANDONNES
# ══════════════════════════════════════════════════════════════════════════════

def _panier_with_articles(db, pan):
    d = dict(pan)
    articles = db.execute("SELECT produit, qte, prix FROM panier_articles WHERE id_panier = ?", (d["id"],)).fetchall()
    d["articles"] = [dict(a) for a in articles]
    return d


@app.get("/paniers")
def liste_paniers(marque: Optional[str] = None):
    with get_db() as db:
        if marque:
            rows = db.execute("SELECT * FROM paniers WHERE LOWER(marque) = ? ORDER BY total DESC", (marque.lower(),)).fetchall()
        else:
            rows = db.execute("SELECT * FROM paniers ORDER BY total DESC").fetchall()
        paniers = [_panier_with_articles(db, r) for r in rows]
    potentiel = sum(p["total"] for p in paniers if not p["relance_envoyee"])
    return {"ref": ref(), "count": len(paniers), "potentiel_recuperation": potentiel, "paniers": paniers}


@app.get("/paniers/client/{email}")
def panier_client(email: str):
    with get_db() as db:
        rows = db.execute("SELECT * FROM paniers WHERE LOWER(email) = ?", (email.lower(),)).fetchall()
        if not rows:
            raise HTTPException(404, f"Aucun panier abandonné pour {email}.")
        paniers = [_panier_with_articles(db, r) for r in rows]
    return {"ref": ref(), "paniers": paniers}


@app.post("/paniers/{id_panier}/relance")
def envoyer_relance(id_panier: str):
    with get_db() as db:
        row = db.execute("SELECT * FROM paniers WHERE UPPER(id) = ?", (id_panier.upper(),)).fetchone()
        if not row:
            raise HTTPException(404, f"Panier {id_panier} non trouvé.")
        if not row["email"]:
            raise HTTPException(400, "Visiteur anonyme — pas d'email.")
        if row["relance_envoyee"]:
            raise HTTPException(409, f"Relance déjà envoyée à {row['client']}.")
        db.execute("UPDATE paniers SET relance_envoyee = 1 WHERE UPPER(id) = ?", (id_panier.upper(),))
        updated = db.execute("SELECT * FROM paniers WHERE UPPER(id) = ?", (id_panier.upper(),)).fetchone()
        panier = _panier_with_articles(db, updated)
    return {
        "ref": ref(),
        "message": "Relance envoyée",
        "code_promo": "BIENVENUE10 (-10%)",
        "panier": panier,
    }


# ── Reset endpoint (for demos) ──────────────────────────────────────────────

@app.post("/reset")
def reset_data():
    """Remet toutes les données à leur état initial. Utile entre deux démos."""
    if DB_PATH.exists():
        DB_PATH.unlink()
    init_db()
    return {"ref": ref(), "message": "Base de données réinitialisée."}


# ── Dashboard ────────────────────────────────────────────────────────────────

DASHBOARD_PATH = Path(__file__).parent / "dashboard.html"

@app.get("/dashboard")
def dashboard():
    return FileResponse(DASHBOARD_PATH, media_type="text/html")
