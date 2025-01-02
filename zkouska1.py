# Příklad 1: Práce s podmínkami a cykly
# Zadání:
# Napište funkci `process_numbers`, která přijme seznam celých čísel. 
# Funkce vrátí nový seznam, který obsahuje pouze čísla větší než 5, vynásobená 2.
# Pokud seznam obsahuje číslo 10, ukončete zpracování seznamu a vraťte dosud vytvořený seznam.

def process_numbers(numbers):
    # Inicializujeme prázdný seznam, kam budeme ukládat výsledky.
    result = []
    
    # Procházíme každý prvek v seznamu 'numbers'.
    for number in numbers:
        # Pokud je aktuální číslo rovno 10, ukončíme cyklus.
        if number == 10:
            break
        
        # Pokud je aktuální číslo větší než 5, přidáme do výsledného seznamu jeho dvojnásobek.
        if number > 5:
            result.append(number * 2)
    
    # Vracíme seznam s čísly splňujícími podmínky.
    return result

#Zkouška:

# Můj seznam
muj_sez = [3, 9, 5, 7, 10, 2]

# Zavolání funkce s vlastním seznamem
result = process_numbers(muj_sez)

# Výsledek
print("Výsledek:", result)

# Pytest testy pro Příklad 1
def test_process_numbers():
    assert process_numbers([1, 6, 3, 10, 8]) == [12]
    assert process_numbers([7, 8, 10, 12]) == [14, 16]
    assert process_numbers([1, 2, 3, 4]) == []
    assert process_numbers([5, 6, 7, 15]) == [12, 14, 30]

test_process_numbers()
print("Všechny testy proběhly úspěšně!")