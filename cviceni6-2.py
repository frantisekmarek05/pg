import requests

url = "https://db.carnewschina.com/suggest?q="

def download_json_and_parse_brands(prefix):
    
    response = requests.get(url + prefix)
    if response.status_code == 200:
        try:
            data = response.json()
    
            if 'brands' in data:
                result = [brand for brand in data['brands'] if brand['name'].lower().startswith(prefix.lower())]
            else:
                print("Brands key not found in response")
                result = []
        except json.JSONDecodeError:
            print("Error decoding JSON response")
            result = []
    else:
        print(f"Chyba při stahování dat: {response.status_code}")
        result = []
    
    return result

if __name__ == "__main__":
    prefix = input("Zadej prefix: ")
    brands = download_json_and_parse_brands(prefix)
    
    if not brands:
        print("Žádné značky nebyly nalezeny.")
    else:
        for brand in brands:
            print(brand['name'])
 