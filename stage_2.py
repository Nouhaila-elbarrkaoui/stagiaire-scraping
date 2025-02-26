import json
import requests
from bs4 import BeautifulSoup
import time

# Charger le fichier JSON avec les liens
with open('stagiaires_offres.json', 'r', encoding='utf-8') as file:
    offres = json.load(file)

resultats = []

# En-têtes HTTP
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Parcourir chaque lien et extraire les informations
for offre in offres:
    url = offre['link']
    
    # Vérifier si l'URL est valide
    if not url or not (url.startswith('http://') or url.startswith('https://')):
        print(f"URL invalide ignorée : {url}")
        continue
    
    print(f"Traitement de : {url}")
    
    # Gestion des erreurs de connexion
    max_retries = 3
    retry_delay = 5  # seconds
    response = None

    for _ in range(max_retries):
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                break
        except requests.exceptions.RequestException as e:
            print(f"Erreur de connexion : {e}. Réessai dans {retry_delay} secondes...")
            time.sleep(retry_delay)
    else:
        print(f"Échec après {max_retries} tentatives pour : {url}")
        continue
    
    # Parser le HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extraire le titre (h2)
    titre = soup.find('h2')
    titre = titre.text.strip() if titre else "Titre non trouvé"

    # Localiser la section principale avec la classe spécifique
    section_principale = soup.find('div', class_='section_single_content_offre')
    
    # Initialiser le lien de candidature
    lien_candidature = "Lien non trouvé"
    
    # Si la section principale est trouvée, naviguer vers le bouton de candidature
    if section_principale:
        footer_card = section_principale.find('div', class_='footer_card_single_content_offre')
        if footer_card:
            buttons_footer = footer_card.find('div', class_='buttons_footer_card_single_information_offre')
            if buttons_footer:
                bouton = buttons_footer.find('a', class_='button_postuler_single_offre')
                if bouton and bouton.has_attr('href'):
                    lien_candidature = bouton['href']
    
    # Ajouter les informations extraites
    resultats.append({
        "titre": titre,
        "lien_candidature": lien_candidature,
        "url_source": url
    })

    # Délai entre les requêtes pour éviter de surcharger le serveur
    time.sleep(2)

# Enregistrer les résultats dans un nouveau fichier JSON
with open('resultats_offres_3.json', 'w', encoding='utf-8') as output_file:
    json.dump(resultats, output_file, ensure_ascii=False, indent=4)

print("✅ Extraction terminée ! Résultats enregistrés dans 'resultats_offres_3.json'")