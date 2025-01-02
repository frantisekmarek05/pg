# Příklad 2: Práce s externími knihovnami a soubory
# Zadání:
# Napište funkci `fetch_and_save_data`, která:
# 1. Načte data z URL (https://jsonplaceholder.typicode.com/posts).
# 2. Do staženého json souboru přidá klíč `userName` s hodnotou jména uživatele podle klíče `userId` z URL (např. 1 -> "Leanne Graham").
# 3. Data uloží do souboru `data.json` ve formátu JSON.
# Použijte knihovny `requests` a `json`.

import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
user_names = {
    1: "Leanne Graham",
    2: "Ervin Howell",
    3: "Clementine Bauch",
    4: "Patricia Lebsack",
    5: "Chelsey Dietrich",
    6: "Mrs. Dennis Schulist",
    7: "Kurtis Weissnat",
    8: "Nicholas Runolfsdottir V",
    9: "Glenna Reichert",
    10: "Clementina DuBuque"
}

def fetch_and_save_data(): # Definování funkce
    try:
        # Stáhneme data z URL pomocí GET požadavku
        response = requests.get(url)
        print(f"Status kód odpovědi: {response.status_code}")  # Pro ladění
        # Kontrolujeme, zda byl požadavek úspěšný
        if response.status_code != 200: #Tento řádek kontroluje, zda odpověď serveru obsahuje úspěšný stavový kód 200, a pokud ne, vrací hodnotu False
            return False
        
        # Převedeme odpověď na JSON
        data = response.json()
        # Pro každý záznam v datech přidáme klíč 'userName'
        for item in data: # cyklus, který prochází každý prvek (záznam) v seznamu data.
            user_id = item.get("userId")  # získávání hodnoty pro klíč "userId" pomocí metody .get()
            if user_id in user_names: # kontroluje, zda hodnota user_id existuje jako klíč ve slovníku user_names
                item["userName"] = user_names[user_id] # Pokud je user_id nalezeno ve slovníku user_names, přidá se do aktuálního záznamu nový klíč "userName", jehož hodnota je odpovídající jméno uživatele podle user_id
        
        # Uložíme data do souboru 'data.json' ve formátu JSON
        with open("data1.json", "w", encoding="utf-8") as file: # soubor bude otevřen pro zápis, bude otevřen s kódováním UTF-8 (správné podpory pro speciální znaky (diakritika)
            json.dump(data, file, indent=4, ensure_ascii=False) # zapisujeme Python data do souboru ve formátu JSON s odsazením pro lepší čitelnost a zachovává ne-ASCII znaky v původní podobě.
        
        return True
    except Exception as e: # zachytí jakoukoliv výjimku (chybu), která by mohla nastat v bloku try, "e" uchovává popis nebo detail o chybě (výjimce).
        print(f"Chyba při zpracování dat: {e}")
        return False

# Pytest testy pro Příklad 2
from unittest.mock import patch, MagicMock, mock_open

def test_fetch_and_save_data():
    mock_data = [
        {"userId": 1, "id": 1, "title": "Test post", "body": "This is a test."}
    ]
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(ok=True, status_code=200, json=MagicMock(return_value=mock_data), text=json.dumps(mock_data), content=json.dumps(mock_data))

        with patch("builtins.open", mock_open()) as mock_file:
            assert fetch_and_save_data() == True
            mock_file().write.call_args[0][0] == json.dumps([
                {
                    "userId": 1,
                    "id": 1,
                    "title": "Test post",
                    "body": "This is a test.",
                    "userName": "Leanne Graham"
                }
            ])

# Spuštění funkce pro testování
if fetch_and_save_data(): # volání funkce, a vysledek se určí podle True nebo False
    print("Data byla úspěšně uložena do souboru.")
else:
    print("Došlo k chybě při zpracování.")