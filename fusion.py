import json

# Charger le premier fichier JSON (resultats_offres_3.json)
with open('resultats_offres_3.json', 'r', encoding='utf-8') as file:
    resultats_offres = json.load(file)

# Charger le deuxième fichier JSON (offres_detaillees.json)
with open('offres_detaillees.json', 'r', encoding='utf-8') as file:
    offres_detaillees = json.load(file)

# Créer un dictionnaire pour stocker les liens de candidature par URL
liens_candidature_par_url = {offre['url_source']: offre['lien_candidature'] for offre in resultats_offres}

# Fusionner les données
for offre in offres_detaillees:
    url_source = offre['url_source']
    if url_source in liens_candidature_par_url:
        offre['lien_postuler'] = liens_candidature_par_url[url_source]
    else:
        offre['lien_postuler'] = "Lien non trouvé"

# Enregistrer le résultat dans un nouveau fichier JSON
with open('offres_fusionnees.json', 'w', encoding='utf-8') as output_file:
    json.dump(offres_detaillees, output_file, ensure_ascii=False, indent=4)

print("✅ Fusion terminée ! Résultats enregistrés dans 'offres_fusionnees.json'")