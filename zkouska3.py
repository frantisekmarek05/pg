# Příklad 3: Základy OOP (dědičnost, abstrakce, zapouzdření)
# Zadání:
# Vytvořte třídu `Shape` s abstraktní metodou `area`.
# Vytvořte dvě podtřídy: `Rectangle` a `Circle`.
# - `Rectangle` má atributy `width` a `height` a implementuje metodu `area`.
# - `Circle` má atribut `radius` a implementuje metodu `area`.
import math
from abc import ABC, abstractmethod # Importuje třídy a funkce pro práci s abstraktními třídami

class Shape(ABC): # Definuje abstraktní třídu Shape, která dědí od třídy ABC
    @abstractmethod # Dekorátor, který označuje metodu area jako abstraktní
    def area(self):
        pass

# Třída Rectangle dědí od Shape
class Rectangle(Shape): # / self: Odkazuje na samotný objekt, který je vytvářen; width, height: Jsou parametry, které metoda přijímá
    def __init__(self, width, height): #definování konstruktoru třídy (metoda __init__), který je volán při vytváření nového objektu dané třídy, a inicializuje objekty s hodnotami pro šířku (width) a výšku (height
        self.width = width  # Ukládá šířku obdélníku 
        self.height = height  # Ukládá výšku obdélníku

    # Implementace metody area pro obdélník
    def area(self):
        return self.width * self.height  # Obsah obdélníku je šířka * výška

# Třída Circle dědí od Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # Ukládá poloměr kruhu

    # Implementace metody area pro kruh
    def area(self):
        return math.pi * self.radius ** 2  # Obsah kruhu je π * r^2

from unittest.mock import patch, MagicMock, mock_open

# Pytest testy pro Příklad 3

def test_shapes():
    rect = Rectangle(4, 5)
    assert rect.area() == 20  # Očekáváme výsledek 20 pro obdélník

    circle = Circle(3)
    assert round(circle.area(), 1) == 28.3  # Očekáváme výsledek přibližně 28.3 pro kruh


    with patch("abc.ABC", side_effect=NotImplementedError):
        try:
            shape = Shape()
        except TypeError:
            pass


# Test s vlastními údaji
rect = Rectangle(6, 8)
print(f"Obsah obdélníku: {rect.area()}")

circle = Circle(5)
print(f"Obsah kruhu: {round(circle.area(), 2)}")
