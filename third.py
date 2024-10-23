def je_prvocislo(cislo):

    if cislo <= 1:
        return False
    for i in range(2, int(cislo ** 0.5) + 1):
        if cislo % i == 0:
            return False
    return True


def vrat_prvocisla(maximum):

    try:
        maximum = int(maximum)
    except ValueError:
        return []

    return [num for num in range(2, maximum + 1) if je_prvocislo(num)]


if __name__ == "__main__":
    try:
        cislo = int(input("Zadej maximum: "))
        prvocisla = vrat_prvocisla(cislo)
        print(prvocisla)
    except ValueError:
        print("Zadaná hodnota musí být celé číslo.")