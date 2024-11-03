# Zadanie 1
from collections import Counter
import string

def analiza_tekstu(tekst, stop_words):

    tekst = tekst.translate(str.maketrans('', '', string.punctuation)).lower()
    slowa = tekst.split()

 
    liczba_slow = len(slowa)
    liczba_zdan = tekst.count('.')
    liczba_akapitow = tekst.count('\n') + 1


    slowa_bez_stop = [slowo for slowo in slowa if slowo not in stop_words]
    najczestsze_slowa = Counter(slowa_bez_stop).most_common(5)


    transformowane_slowa = [slowo[::-1] if slowo.startswith('a') else slowo for slowo in slowa]

    return liczba_slow, liczba_zdan, liczba_akapitow, najczestsze_slowa, transformowane_slowa


tekst = "Apple is amazing. An apple a day keeps the doctor away. Amazing!\nAnother paragraph."
stop_words = ["is", "a", "the", "an"]

liczba_slow, liczba_zdan, liczba_akapitow, najczestsze_slowa, transformowane_slowa = analiza_tekstu(tekst, stop_words)
print("Liczba słów:", liczba_slow)
print("Liczba zdań:", liczba_zdan)
print("Liczba akapitów:", liczba_akapitow)
print("Najczęściej występujące słowa:", najczestsze_slowa)
print("Transformowane słowa:", transformowane_slowa)

# Zadanie 2
class Macierz:
    def __init__(self, macierz):
        self.macierz = macierz

    def dodaj(self, inna):
        if len(self.macierz) != len(inna.macierz) or len(self.macierz[0]) != len(inna.macierz[0]):
            raise ValueError("Nieprawidłowe wymiary macierzy do dodawania.")
        return Macierz([[self.macierz[i][j] + inna.macierz[i][j] for j in range(len(self.macierz[0]))] for i in range(len(self.macierz))])

    def mnoz(self, inna):
        if len(self.macierz[0]) != len(inna.macierz):
            raise ValueError("Nieprawidłowe wymiary macierzy do mnożenia.")
        return Macierz([[sum(self.macierz[i][k] * inna.macierz[k][j] for k in range(len(inna.macierz))) for j in range(len(inna.macierz[0]))] for i in range(len(self.macierz))])

    def transponuj(self):
        return Macierz([[self.macierz[j][i] for j in range(len(self.macierz))] for i in range(len(self.macierz[0]))])

    def __str__(self):
        return '\n'.join([' '.join(map(str, wiersz)) for wiersz in self.macierz])


macierz1 = Macierz([[1, 2], [3, 4]])
macierz2 = Macierz([[5, 6], [7, 8]])

try:
    wynik_dodawania = macierz1.dodaj(macierz2)
    print("Wynik dodawania macierzy:\n", wynik_dodawania)
except ValueError as e:
    print(e)

try:
    wynik_mnozenia = macierz1.mnoz(macierz2)
    print("Wynik mnożenia macierzy:\n", wynik_mnozenia)
except ValueError as e:
    print(e)

wynik_transponowania = macierz1.transponuj()
print("Wynik transponowania macierzy:\n", wynik_transponowania)

# Zadanie 3
def znajdz_ekstrema(dane):
    liczby = list(filter(lambda x: isinstance(x, (int, float)), dane))
    napisy = list(filter(lambda x: isinstance(x, str), dane))
    krotki = list(filter(lambda x: isinstance(x, tuple), dane))

    najwieksza_liczba = max(liczby) if liczby else None
    najdluzszy_napis = max(napisy, key=len) if napisy else None
    krotka_najwiecej_elementow = max(krotki, key=len) if krotki else None

    return najwieksza_liczba, najdluzszy_napis, krotka_najwiecej_elementow


dane = [42, "Hello", (1, 2), 3.14, "World", (3, 4, 5), "Python"]
najwieksza_liczba, najdluzszy_napis, krotka_najwiecej_elementow = znajdz_ekstrema(dane)
print("Największa liczba:", najwieksza_liczba)
print("Najdłuższy napis:", najdluzszy_napis)
print("Krotka o największej liczbie elementów:", krotka_najwiecej_elementow)

# Zadanie 4
from functools import reduce

def zlacz_macierze(macierze, operacja):
    if operacja == 'dodawanie':
        return reduce(lambda x, y: x.dodaj(y), macierze)
    elif operacja == 'mnożenie':
        return reduce(lambda x, y: x.mnoz(y), macierze)
    return None


macierze = [
    Macierz([[1, 2], [3, 4]]),
    Macierz([[5, 6], [7, 8]]),
    Macierz([[9, 10], [11, 12]])
]
operacja = 'dodawanie'
wynik = zlacz_macierze(macierze, operacja)
print("Wynik złożonej operacji na macierzach:\n", wynik)