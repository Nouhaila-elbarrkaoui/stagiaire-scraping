import json

# Charger les données JSON à partir du fichier
with open('offres_fusionnees.json', 'r', encoding='utf-8') as f:
    offres = json.load(f)

# Séparer les offres avec et sans lien de candidature
offres_avec_lien = [offre for offre in offres if offre.get('lien_postuler') and offre['lien_postuler'] != "Lien non trouvé"]
offres_sans_lien = [offre for offre in offres if not offre.get('lien_postuler') or offre['lien_postuler'] == "Lien non trouvé"]

# Enregistrer les résultats dans deux fichiers JSON
with open('offres_avec_lien.json', 'w', encoding='utf-8') as f:
    json.dump(offres_avec_lien, f, ensure_ascii=False, indent=4)

with open('offres_sans_lien.json', 'w', encoding='utf-8') as f:
    json.dump(offres_sans_lien, f, ensure_ascii=False, indent=4)

print("Fichiers générés : offres_avec_lien.json et offres_sans_lien.json")
