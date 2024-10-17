def my_range(start, stop, step=1):
    """
    Naše vlastní implementace range(), chceme, aby se chovala úplně stejně jako range.
    """
    results = []
    i = start
    while i < stop:
        results.append(i)
        i += step
    return results

if __name__ == "__main__":
    seznam = list(range(1,10, 2))
    print(seznam)

    seznam = my_range(1,10,3)
    print(seznam)