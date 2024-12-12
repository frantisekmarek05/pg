import requests  # Načítáme modul requests, který umožňuje stahovat data z internetu.
import json  # Načítáme modul json, který slouží k práci s daty ve formátu JSON.

def download_and_convert_exchange_rates(url):
    response = requests.get(url)  # Stahujeme data z uvedené URL adresy.
    response.encoding = 'utf-8'  # Nastavujeme kódování na UTF-8, aby byla správně zobrazena česká diakritika.

    if response.status_code != 200:  # Kontrolujeme, zda byl požadavek úspěšný.
        raise Exception(f"Failed to fetch data: {response.status_code}")

    lines = response.text.strip().split('\n')  # Rozdělujeme text na jednotlivé řádky.
    exchange_rates = []

    for line in lines[2:]:  # Přeskakujeme první dva řádky, protože obsahují hlavičku a oddělovač.
        parts = line.split('|')  # Rozdělujeme řádky podle oddělovače '|'.
        if len(parts) == 5:  # Kontrolujeme, zda má každý řádek správný počet částí.
            country, currency, amount, code, rate = parts
            exchange_rates.append({
                "zeme": country,
                "mena": currency,
                "mnozstvi": int(amount),  # Převádíme množství na celé číslo.
                "kod": code,  # Přidáváme kód měny.
                "kurz": float(rate.replace(',', '.'))  # Převádíme kurz na desetinné číslo.
            })

    return exchange_rates  # Vracíme seznam zpracovaných kurzů.

url = "https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"  # Definujeme URL adresu pro stažení kurzovního lístku.
output_file = "data.json"  # Určujeme název výstupního souboru.

try:
    rates = download_and_convert_exchange_rates(url)  # Voláme funkci pro stažení a konverzi dat.
    with open(output_file, "w", encoding="utf-8") as file:  # Otevíráme (nebo vytváříme) soubor pro zápis JSON dat.
        json.dump(rates, file, indent=4, ensure_ascii=False)  # Ukládáme data do souboru ve formátu JSON.
    print(f"Data has been saved to {output_file}") 
except Exception as e:  # Zachytáváme chyby, které mohou nastat během procesu.
    print(str(e))  
