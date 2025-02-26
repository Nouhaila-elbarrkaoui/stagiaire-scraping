import json
import requests
from bs4 import BeautifulSoup

def get_text_or_none(element):
    return element.text.strip() if element else None

def get_href_or_none(element):
    return element['href'] if element and element.has_attr('href') else None

# Charger les données JSON avec les liens
with open('stagiaires_offres.json', 'r', encoding='utf-8') as file:
    offres = json.load(file)

resultats = []

for offre in offres:
    url = offre.get('link')  # Utilise .get() pour éviter KeyError
    
    if not url or not url.startswith(('http://', 'https://')):
        print(f"URL invalide ou manquante : {url}")
        continue

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        try:
            # Extraction des informations principales
            titre = get_text_or_none(soup.find('h2'))
            societe = get_text_or_none(soup.select_one('.societe_name_single_information a'))
            ville = get_text_or_none(soup.select_one('span[data-tooltip="Ville"]'))
            contrat = get_text_or_none(soup.select_one('span[data-tooltip="Type de contrat"]'))
            lieu = get_text_or_none(soup.select_one('span[data-tooltip="Type de lieu de travail"]'))
            date_pub = get_text_or_none(soup.select_one('span[data-tooltip="Date de publication"]'))

            # Détails du poste
            details_section = soup.select_one('.body_card_single_content_offre')
            details = get_text_or_none(details_section.find('p')) if details_section else None

            # Missions principales
            missions = [li.text.strip() for li in details_section.find_all('li')] if details_section else []

            # Profil recherché
            profil_section = details_section.find('p', string=lambda text: text and 'Profil recherché' in text) if details_section else None
            profil = [li.text.strip() for li in profil_section.find_next('ul').find_all('li')] if profil_section else []

            # Lien de postulation
            lien_postuler = get_href_or_none(soup.select_one('.button_postuler_single_offre'))

            # Ajouter les informations extraites
            resultats.append({
                'titre': titre,
                'societe': societe,
                'ville': ville,
                'contrat': contrat,
                'lieu': lieu,
                'date_publication': date_pub,
                'details': details,
                'missions': missions,
                'profil': profil,
                'lien_postuler': lien_postuler,
                'url_source': url
            })

        except Exception as e:
            print(f"Erreur lors de l'extraction de {url}: {e}")

    else:
        print(f"Échec de la récupération de l'URL : {url}")

# Sauvegarder les résultats dans un fichier JSON
with open('offres_detaillees.json', 'w', encoding='utf-8') as outfile:
    json.dump(resultats, outfile, ensure_ascii=False, indent=4)

print("Extraction terminée. Les informations ont été enregistrées dans 'offres_detaillees.json'.")
