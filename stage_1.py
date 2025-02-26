import requests
from bs4 import BeautifulSoup
import json

def scrape_stagiaires_ma(url, max_pages):
    all_job_offers = []

    for page in range(1, max_pages + 1):
        print(f"Scraping page {page}...")
        page_url = f"{url}?pages={page}"
        response = requests.get(page_url)

        if response.status_code != 200:
            print(f"Erreur lors de l'accès à la page {page} : {response.status_code}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')

        for link_tag in soup.find_all('a', href=True):
            title_tag = link_tag.find('h3', class_='title_card_offre_n')
            if title_tag:
                title_text = title_tag.get_text(strip=True)
                all_job_offers.append({
                    "title": title_text,
                    "link": link_tag['href']
                })

    return all_job_offers

def remove_duplicates(offers):
    unique_offers = []
    seen = set()

    for offer in offers:
        offer_tuple = (offer["title"], offer["link"])
        if offer_tuple not in seen:
            seen.add(offer_tuple)
            unique_offers.append(offer)

    return unique_offers

if __name__ == "__main__":
    base_url = "https://www.stagiaires.ma/offres-de-stages-et-premier-emploi-maroc/"
    max_pages = 34

    offers = scrape_stagiaires_ma(base_url, max_pages)

    unique_offers = remove_duplicates(offers)

    # Sauvegarde des offres uniques dans un fichier JSON
    with open("stagiaires_offres.json", "w", encoding="utf-8") as file:
        json.dump(unique_offers, file, ensure_ascii=False, indent=4)

    print(f"{len(unique_offers)} offres uniques ont été sauvegardées dans 'stagiaires_offres.json'.")
