def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    typ = figurka['typ']
    puvodni_pozice = figurka['pozice']

    # Ověření, zda je cílová pozice mimo šachovnici
    if not (1 <= cilova_pozice[0] <= 8 and 1 <= cilova_pozice[1] <= 8):
        return False

    # Ověření, zda je cílová pozice obsazená
    if cilova_pozice in obsazene_pozice:
        return False

    # Ověření pohybu podle typu figurky
    if typ == "pěšec":
        if puvodni_pozice[1] == cilova_pozice[1]:  # Stejný sloupec
            if puvodni_pozice[0] == 2 and cilova_pozice[0] == 4:
                return (4, 2) not in obsazene_pozice  # Dva kroky vpřed z pozice 2
            return cilova_pozice[0] == puvodni_pozice[0] + 1  # Jeden krok vpřed
        return False

    elif typ == "jezdec":
        dx = abs(puvodni_pozice[0] - cilova_pozice[0])
        dy = abs(puvodni_pozice[1] - cilova_pozice[1])
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

    elif typ == "věž":
        if puvodni_pozice[0] == cilova_pozice[0]:  # Horizontálně
            for y in range(min(puvodni_pozice[1], cilova_pozice[1]) + 1, max(puvodni_pozice[1], cilova_pozice[1])):
                if (puvodni_pozice[0], y) in obsazene_pozice:
                    return False
            return True
        elif puvodni_pozice[1] == cilova_pozice[1]:  # Vertikálně
            for x in range(min(puvodni_pozice[0], cilova_pozice[0]) + 1, max(puvodni_pozice[0], cilova_pozice[0])):
                if (x, puvodni_pozice[1]) in obsazene_pozice:
                    return False
            return True
        return False

    elif typ == "střelec":
        if abs(puvodni_pozice[0] - cilova_pozice[0]) == abs(puvodni_pozice[1] - cilova_pozice[1]):
            dx = 1 if cilova_pozice[0] > puvodni_pozice[0] else -1
            dy = 1 if cilova_pozice[1] > puvodni_pozice[1] else -1
            x, y = puvodni_pozice[0] + dx, puvodni_pozice[1] + dy
            while (x, y) != cilova_pozice:
                if (x, y) in obsazene_pozice:
                    return False
                x += dx
                y += dy
            return True
        return False

    elif typ == "dáma":
        if puvodni_pozice[0] == cilova_pozice[0] or puvodni_pozice[1] == cilova_pozice[1]:  # Věž
            return je_tah_mozny({"typ": "věž", "pozice": puvodni_pozice}, cilova_pozice, obsazene_pozice)
        elif abs(puvodni_pozice[0] - cilova_pozice[0]) == abs(puvodni_pozice[1] - cilova_pozice[1]):  # Střelec
            return je_tah_mozny({"typ": "střelec", "pozice": puvodni_pozice}, cilova_pozice, obsazene_pozice)
        return False

    elif typ == "král":
        return abs(puvodni_pozice[0] - cilova_pozice[0]) <= 1 and abs(puvodni_pozice[1] - cilova_pozice[1]) <= 1

    return False

# Testování funkce
if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
