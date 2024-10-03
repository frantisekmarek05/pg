# funkce která vypise hello world
def hello_world():
    print("hello world")


# funkce ktera vypise pozadovany pocet hvezd
def five_stars(limit):
    i = 0
    while i < limit:
        print("*")
        i += 1

five_stars(10)

#funkce overi zda je number v rozmezi minimum - maximum a vypise textovy vystup
def in_range(number, minimum, maximum):
    if number > minimum and number < maximum:
        print("number", number, "is in range", minimum "-", maximum)
    else:
        print("number", number, "is out of range", minimum "-" maximum)


in_range(1, 100, 1000)
"number 1 is out of range 100 - 500"
in_range(500, 100, 1000)
"number 500 is in range 100-1000"

def max_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

max_number(1,2,3)
3
max_number(100,10,1)
100
max_number(1.1, 1.3, 1.2)
1.3

