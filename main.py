from fastapi import FastAPI
import json

app = FastAPI()

# Charger les données JSON
def load_json(filename):
    with open(filename, "r", encoding="utf-8") as file:  # Ajout de l'encodage UTF-8
        return json.load(file)

# Fonction pour insérer une ligne vide entre les offres
def add_empty_line_between_jobs(data):
    result = []
    for job in data:
        result.append(job)
        # Ajouter une ligne vide (un dictionnaire vide) entre les offres
        result.append({})
    return result[:-1]  # Retirer le dernier élément vide ajouté

# Endpoints de l'API

@app.get("/jobs_with_links_stagiaire")
def get_jobs_with_links():
    data = load_json("C:/Users/hp/Downloads/STAGIAIRE SCRAPING/offres_avec_lien.json")
    data_with_empty_lines = add_empty_line_between_jobs(data)
    return {"jobs_with_links": data_with_empty_lines}

@app.get("/jobs_without_links_stagiaire")
def get_jobs_without_links():
    data = load_json("C:/Users/hp/Downloads/STAGIAIRE SCRAPING/offres_sans_lien.json")
    data_with_empty_lines = add_empty_line_between_jobs(data)
    return {"jobs_without_links": data_with_empty_lines}