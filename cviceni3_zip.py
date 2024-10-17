def my_zip(*iterables):

    results = []
    
    min_length = min(len(it) for it in iterables)
    
    for i in range(min_length):
        
        results.append(tuple(it[i] for it in iterables))
    
    return results

if __name__ == "__main__":

    jmena = ["Alice", "Bob", "Karel", "Eva", "Martin"]
    vek =   [    30,     20,     24,     18,     27  ]
    vaha =  [    50,     80,     90,     55,     67  ]
    vysledek = list(zip(jmena,vek, vaha))
    print(vysledek)
    #for jmeno, vek, vaha in vysledek:
    #    print(f"{jmeno} je {vek} a vazi {vaha}kg)

    vysledek = my_zip(jmena, vek, vaha)
    print(vysledek)