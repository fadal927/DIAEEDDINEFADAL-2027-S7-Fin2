"""
Analyse des défaillances d'entreprises au Maroc
Projet Data Science & Bases de données

Prérequis :
    pip install pandas openpyxl matplotlib

Le script doit être placé dans :
    script/analyse.py

Le fichier Excel doit être placé dans :
    dataset/dataset_defaillances_entreprises_maroc.xlsx
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Chemins
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(
    BASE_DIR, "dataset", "dataset_defaillances_entreprises_maroc.xlsx"
)
FIG_DIR = os.path.join(BASE_DIR, "figures")
os.makedirs(FIG_DIR, exist_ok=True)

# -----------------------------
# Importation des données
# -----------------------------
df_def = pd.read_excel(DATA_FILE, sheet_name="Defaillances_annuelles")
df_cre = pd.read_excel(DATA_FILE, sheet_name="Creations_OMPIC")
df_evo = pd.read_excel(DATA_FILE, sheet_name="Evolution_2015_2024")
df_sec = pd.read_excel(DATA_FILE, sheet_name="Secteurs_2024")
df_vil = pd.read_excel(DATA_FILE, sheet_name="Villes_2024")
df_taille = pd.read_excel(DATA_FILE, sheet_name="Taille_2024")
df_inf = pd.read_excel(DATA_FILE, sheet_name="Inflation_HCP")

plt.rcParams.update({
    "figure.figsize": (10, 6),
    "axes.titlesize": 14,
    "axes.labelsize": 11,
    "font.size": 10
})

# Fonction pour sauvegarder les graphiques
def save_fig(filename):
    plt.tight_layout()
    plt.savefig(
        os.path.join(FIG_DIR, filename),
        dpi=180,
        bbox_inches="tight"
    )
    plt.close()

# -----------------------------
# GRAPHE 1 : Défaillances 2009-2024
# -----------------------------
plt.figure()
plt.plot(
    df_def["Annee"],
    df_def["Defaillances_entreprises"],
    marker="o",
    linewidth=2
)
plt.title("Évolution des défaillances d'entreprises au Maroc (2009–2024)")
plt.xlabel("Année")
plt.ylabel("Nombre de défaillances")
plt.grid(True, alpha=0.25)
save_fig("01_evolution_defaillances.png")

# -----------------------------
# GRAPHE 2 : Variation annuelle
# -----------------------------
plt.figure()
d = df_def.dropna(subset=["Variation_annuelle_%"])
plt.bar(d["Annee"].astype(str), d["Variation_annuelle_%"])
plt.axhline(0, linewidth=0.8)
plt.title("Variation annuelle des défaillances d'entreprises")
plt.xlabel("Année")
plt.ylabel("Variation (%)")
plt.xticks(rotation=45)
plt.grid(axis="y", alpha=0.25)
save_fig("02_variation_annuelle_defaillances.png")

# -----------------------------
# GRAPHE 3 : Créations vs défaillances
# -----------------------------
plt.figure()
plt.plot(
    df_evo["Annee"],
    df_evo["Defaillances_entreprises"],
    marker="o",
    label="Défaillances"
)
plt.plot(
    df_evo["Annee"],
    df_evo["Creations_entreprises_OMPIC"],
    marker="o",
    label="Créations"
)
plt.title("Créations et défaillances d'entreprises (2015–2024)")
plt.xlabel("Année")
plt.ylabel("Nombre d'entreprises")
plt.legend()
plt.grid(True, alpha=0.25)
save_fig("03_creations_vs_defaillances.png")

# -----------------------------
# GRAPHE 4 : Ratio
# -----------------------------
plt.figure()
plt.plot(
    df_evo["Annee"],
    df_evo["Taux_de_remplacement_creations_sur_defaillances"],
    marker="o",
    linewidth=2
)
plt.axhline(1, linestyle="--", linewidth=1)
plt.title("Ratio créations / défaillances")
plt.xlabel("Année")
plt.ylabel("Créations pour 1 défaillance")
plt.grid(True, alpha=0.25)
save_fig("04_ratio_creations_defaillances.png")

# -----------------------------
# GRAPHE 5 : Secteurs
# -----------------------------
plt.figure()
s = df_sec.sort_values("Part_des_defaillances_%", ascending=True)
plt.barh(s["Secteur"], s["Part_des_defaillances_%"])
plt.title("Répartition sectorielle des défaillances en 2024")
plt.xlabel("Part des défaillances (%)")
plt.grid(axis="x", alpha=0.25)
save_fig("05_repartition_sectorielle_2024.png")

# -----------------------------
# GRAPHE 6 : Villes
# -----------------------------
plt.figure()
v = df_vil.sort_values("Part_des_defaillances_%", ascending=True)
plt.barh(v["Ville"], v["Part_des_defaillances_%"])
plt.title("Répartition des défaillances par ville en 2024")
plt.xlabel("Part des défaillances (%)")
plt.grid(axis="x", alpha=0.25)
save_fig("06_repartition_villes_2024.png")

# -----------------------------
# GRAPHE 7 : Taille
# -----------------------------
plt.figure()
t = df_taille.sort_values("Part_des_defaillances_%", ascending=False)
plt.bar(t["Categorie"], t["Part_des_defaillances_%"])
plt.title("Défaillances selon la taille des entreprises en 2024")
plt.xlabel("Catégorie")
plt.ylabel("Part des défaillances (%)")
plt.ylim(0, 105)
plt.grid(axis="y", alpha=0.25)
save_fig("07_taille_entreprises_2024.png")

# -----------------------------
# GRAPHE 8 : Inflation
# -----------------------------
plt.figure()
plt.plot(
    df_inf["Annee"],
    df_inf["Inflation_IPC_annuelle_%"],
    marker="o",
    linewidth=2
)
plt.title("Évolution de l'inflation au Maroc (2022–2024)")
plt.xlabel("Année")
plt.ylabel("Inflation annuelle moyenne (%)")
plt.grid(True, alpha=0.25)
save_fig("08_inflation_2022_2024.png")

print("Analyse terminée.")
print(f"Les graphiques ont été enregistrés dans : {FIG_DIR}")
