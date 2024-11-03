def podziel_paczki(wagi, max_waga):
    kursy = []
    obecny_kurs = []
    suma_wag = 0

    for waga in wagi:
        if suma_wag + waga <= max_waga:
            obecny_kurs.append(waga)
            suma_wag += waga
        else:
            kursy.append(obecny_kurs)
            obecny_kurs = [waga]
            suma_wag = waga

    if obecny_kurs:
        kursy.append(obecny_kurs)

    return len(kursy), kursy


wagi_paczek = [2, 3, 5, 7, 1, 4, 2]
max_waga = 10

liczba_kursow, podzial = podziel_paczki(wagi_paczek, max_waga)
print("Minimalna liczba kursów:", liczba_kursow)
print("Podział paczek w kursach:", podzial)

# Zadanie 2
from collections import deque

def bfs_najkrotsza_sciezka(graf, start, cel):
    kolejka = deque([(start, [start])])
    odwiedzone = set()

    while kolejka:
        (wierzcholek, sciezka) = kolejka.popleft()
        if wierzcholek in odwiedzone:
            continue
        odwiedzone.add(wierzcholek)
        for sasiad in graf[wierzcholek]:
            if sasiad == cel:
                return sciezka + [cel]
            else:
                kolejka.append((sasiad, sciezka + [sasiad]))
    return None


graf = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
cel = 'F'
sciezka = bfs_najkrotsza_sciezka(graf, start, cel)
print("Najkrótsza ścieżka z {} do {}: {}".format(start, cel, sciezka))

# Zadanie 3
def optymalizuj_zadania_proceduralnie(zadania):
    zadania.sort(key=lambda x: x[1])
    czas_oczekiwania = 0
    czas_biezacy = 0
    for zadanie in zadania:
        czas_biezacy += zadanie[0]
        czas_oczekiwania += czas_biezacy
    return czas_oczekiwania


zadania = [(3, 10), (1, 5), (2, 8)]  
czas_oczekiwania = optymalizuj_zadania_proceduralnie(zadania)
print("Całkowity czas oczekiwania (proceduralnie):", czas_oczekiwania)


def optymalizuj_zadania_funkcyjnie(zadania):
    posortowane_zadania = sorted(zadania, key=lambda x: x[1])
    czas_oczekiwania = sum(sum(z[0] for z in posortowane_zadania[:i+1]) for i in range(len(posortowane_zadania)))
    return czas_oczekiwania

czas_oczekiwania_funkcyjnie = optymalizuj_zadania_funkcyjnie(zadania)
print("Całkowity czas oczekiwania (funkcyjnie):", czas_oczekiwania_funkcyjnie)

# Zadanie 4
def plecak_proceduralny(pojemnosc, przedmioty):
    n = len(przedmioty)
    dp = [[0 for _ in range(pojemnosc + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(pojemnosc + 1):
            if przedmioty[i-1][1] <= w:
                dp[i][w] = max(przedmioty[i-1][0] + dp[i-1][w-przedmioty[i-1][1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][pojemnosc]


przedmioty = [(60, 10), (100, 20), (120, 30)]  
pojemnosc = 50
maks_wartosc = plecak_proceduralny(pojemnosc, przedmioty)
print("Maksymalna wartość (proceduralnie):", maks_wartosc)


def plecak_funkcyjny(pojemnosc, przedmioty):
    if not przedmioty or pojemnosc == 0:
        return 0
    wartosc, waga = przedmioty[0]
    if waga > pojemnosc:
        return plecak_funkcyjny(pojemnosc, przedmioty[1:])
    else:
        return max(wartosc + plecak_funkcyjny(pojemnosc - waga, przedmioty[1:]), plecak_funkcyjny(pojemnosc, przedmioty[1:]))

maks_wartosc_funkcyjnie = plecak_funkcyjny(pojemnosc, przedmioty)
print("Maksymalna wartość (funkcyjnie):", maks_wartosc_funkcyjnie)

# Zadanie 5
def harmonogram_proceduralny(zadania):
    zadania.sort(key=lambda x: x[1])
    wybrane_zadania = []
    czas_zakonczenia = 0

    for zadanie in zadania:
        if zadanie[0] >= czas_zakonczenia:
            wybrane_zadania.append(zadanie)
            czas_zakonczenia = zadanie[1]

    return wybrane_zadania


zadania = [(1, 4, 3), (3, 5, 2), (0, 6, 8), (5, 7, 6), (8, 9, 4)] 
wybrane_zadania = harmonogram_proceduralny(zadania)
print("Wybrane zadania (proceduralnie):", wybrane_zadania)


def harmonogram_funkcyjny(zadania):
    posortowane_zadania = sorted(zadania, key=lambda x: x[1])
    return list(filter(lambda zadanie: zadanie[0] >= sum(z[1] for z in posortowane_zadania if z[1] <= zadanie[0]), posortowane_zadania))

wybrane_zadania_funkcyjnie = harmonogram_funkcyjny(zadania)
print("Wybrane zadania (funkcyjnie):", wybrane_zadania_funkcyjnie)
