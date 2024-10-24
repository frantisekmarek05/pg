"""
def jaccardova_vzdalenost_mnozin(mnozina1, mnozina2):
   
    mnozina1 = set(mnozina1)
    mnozina2 = set(mnozina2)

    prunik = mnozina1.intersection(mnozina2)
    sjednoceni = mnozina1.union(mnozina2)

    if len(sjednoceni) == 0:
        return 0.0

    vzdalenost = (len(sjednoceni) - len(prunik)) / len(sjednoceni)
    return round(vzdalenost, 2)

if __name__ == "__main__":
    serp1 = ["https://www.seznam.cz", "https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz", "https://www.google.com"]
    serp2 = ["https://www.seznam.cz", "https://www.google.com", "https://www.novinky.cz", "https://www.idnes.cz", "https://www.zpravy.cz", "https://www.tn.cz"]
    serp3 = ["https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz"]

    print(jaccardova_vzdalenost_mnozin(serp1, serp2))
    print(jaccardova_vzdalenost_mnozin(serp2, serp3))
    print(jaccardova_vzdalenost_mnozin(serp1, serp3))



def levensteinova_vzdalenost(dotaz1, dotaz2):
    # Délky obou řetězců
    m = len(dotaz1)
    n = len(dotaz2)

    # Inicializace matice pro uchování vzdáleností
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicializace první sloupce (vzdálenost od prázdného řetězce k dotaz1)
    for i in range(m + 1):
        dp[i][0] = i

    # Inicializace první řádky (vzdálenost od prázdného řetězce k dotaz2)
    for j in range(n + 1):
        dp[0][j] = j

    # Vyplnění matice podle pravidel Levensteinovy vzdálenosti
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Pokud se znaky shodují, žádná změna není potřeba
            if dotaz1[i - 1] == dotaz2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Pokud se znaky neshodují, vybereme minimum ze tří možností
                dp[i][j] = min(
                    dp[i - 1][j] + 1,      # Odstranění znaku z dotaz1
                    dp[i][j - 1] + 1,      # Vložení znaku do dotaz1
                    dp[i - 1][j - 1] + 1    # Změna znaku na dotaz1
                )

    # Vrátí vzdálenost mezi celými řetězci
    return dp[m][n]

if __name__ == "__main__":
    query1 = "seznam"
    query2 = "seznamka"
    query3 = "sesnam"
    query4 = "seznam"

    # Vytiskne Levensteinovu vzdálenost mezi jednotlivými dotazy
    print(levensteinova_vzdalenost(query1, query2))  
    print(levensteinova_vzdalenost(query2, query3))  
    print(levensteinova_vzdalenost(query1, query3))  
    print(levensteinova_vzdalenost(query1, query4))
"""

from cviceni4_jaccard import jaccardova_vzdalenost_mnozin
from cviceni4_levenstein import levensteinova_vzdalenost


def deduplikace_dotazu(dotazy):
    """
    Tato funkce spočítá Jaccardovu vzdálenost a Levensteinovu vzdálenost
    a vyřadí z seznamu dotazy, které mají Jaccardovu vzdálenost menší než 0.5
    a Levensteinovu vzdálenost <= 1.
    """
    # Vytvoříme nový seznam pro uložení unikátních dotazů
    unikatni_dotazy = []

    # Procházení všech dotazů
    for i, dotaz in enumerate(dotazy):
        je_unikatni = True
        # Porovnáváme aktuální dotaz s ostatními
        for j in range(len(dotazy)):
            if i != j:  # Neporovnávat sám se sebou
                jaccard_vzdalenost = jaccardova_vzdalenost_mnozin(dotaz['serp'], dotazy[j]['serp'])
                levenstein_vzdalenost = levensteinova_vzdalenost(dotaz['dotaz'], dotazy[j]['dotaz'])
                
                # Kontrolujeme, zda splňuje podmínky pro duplicitu
                if jaccard_vzdalenost < 0.5 and levenstein_vzdalenost <= 1:
                    je_unikatni = False
                    break  # Pokud je dotaz duplicitní, můžeme přerušit porovnávání

        if je_unikatni:
            unikatni_dotazy.append(dotaz)

    return unikatni_dotazy


if __name__ == "__main__":
    dotaz1 = {
        "dotaz": "seznam",
                "serp": ["https://www.seznam.cz", "https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz", "https://www.google.com"]
    }
    dotaz2 = {
        "dotaz": "seznamka",
        "serp": ["https://www.seznam.cz", "https://www.google.com", "https://www.novinky.cz", "https://www.idnes.cz", "https://www.zpravy.cz", "https://www.tn.cz"]
    }
    dotaz3 = {
        "dotaz": "sesnam",
        "serp": ["https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz"]
    }
    dotaz4 = {
        "dotaz": "google",
        "serp": ["https://www.google.com", "https://maps.google.com", "https://www.gmail.com"]
    }

    # Zavolání funkce deduplikace a vypsání výsledku
    print(deduplikace_dotazu([dotaz1, dotaz2, dotaz3, dotaz4]))

