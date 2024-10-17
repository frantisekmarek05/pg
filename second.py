def cislo_text(cislo):
    # Seznamy s textovými názvy čísel
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    teens = ["jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    desitky = ["", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]

    try:
        cislo = int(cislo)
    except:
        return "Zadaná hodnota není číslo"

    if cislo < 0 or cislo > 100:
        return "Číslo je mimo rozsah 0 až 100"
    if cislo == 100:
        return "sto"
    if 0 <= cislo < 10:
        return jednotky[cislo]
    if 10 < cislo < 20:
        return teens[cislo - 11]
    if cislo == 10:
        return "deset"
    if 20 <= cislo < 100:
        desitka = desitky[cislo // 10]
        jednotka = jednotky[cislo % 10]
        if cislo % 10 == 0:
            return desitka
        return desitka + " " + jednotka

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
