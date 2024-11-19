import sys
import requests
from bs4 import BeautifulSoup

def download_url_and_get_all_hrefs(url):
    """
    Funkce stáhne URL předanou v parametru url pomocí volání response = requests.get(),
    zkontroluje návratový kód response.status_code, který musí být 200,
    pokud ano, najde ve staženém obsahu stránky response.content všechny výskyty
    <a href="url">odkaz</a> a z nich načte url, které vrátí jako seznam pomocí return.
    """

    hrefs = []
    try:
        response = requests.get(url)
        response.raise_for_status()  # zkontroluje návratový kód

        soup = BeautifulSoup(response.text, 'html.parser')

        
        for link in soup.find_all('a', href=True): 
            hrefs.append(link['href'])

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    return hrefs

if __name__ == "__main__":
    try:
        url = "https://www.jcu.cz"
        all_hrefs = download_url_and_get_all_hrefs(url)
        print(all_hrefs)
    except Exception as e:
        print(f"Program skončil chybou: {e}")