import json

# Charger le fichier JSON
with open('offres_sans_lien.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Parcourir chaque offre et supprimer les attributs spécifiques
for offre in data:
    # Supprimer "lien_postuler" s'il existe
    offre.pop("lien_postuler", None)
    
    # Supprimer "profil" si c'est une liste vide
    if "profil" in offre and offre["profil"] == []:
        del offre["profil"]

# Enregistrer les modifications dans le fichier
with open('offres_sans_lien.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Les attributs 'lien_postuler' et les 'profil' vides ont été supprimés.")
