# Program do analizy tekstu

def analiza_tekstu(tekst):
    # Liczba słów
    slowa = tekst.split()
    liczba_slow = len(slowa)

    # Liczba zdań (zakładamy, że kończą się na . ! ?)
    liczba_zdan = tekst.count('.') + tekst.count('!') + tekst.count('?')

    # Najczęściej występujące słowa
    slownik_slow = {}
    for slowo in slowa:
        slowo = slowo.lower().strip(".,!?;:")
        if slowo in slownik_slow:
            slownik_slow[slowo] += 1
        else:
            slownik_slow[slowo] = 1

    najczestsze_slowo = max(slownik_slow, key=slownik_slow.get)

    # Liczba znaków specjalnych
    znaki_specjalne = 0
    for znak in tekst:
        if not znak.isalnum() and not znak.isspace():
            znaki_specjalne += 1

    # Liczba liter
    liczba_liter = sum(1 for znak in tekst if znak.isalpha())

    # Wyświetlenie wyników
    print("Liczba słów:", liczba_slow)
    print("Liczba zdań:", liczba_zdan)
    print("Najczęściej występujące słowo:", najczestsze_slowo, "(wystąpiło", slownik_slow[najczestsze_slowo], "razy)")
    print("Liczba znaków specjalnych:", znaki_specjalne)
    print("Liczba liter:", liczba_liter)

# Wprowadzenie tekstu przez użytkownika
tekst_uzytkownika = input("Podaj tekst do analizy: ")
analiza_tekstu(tekst_uzytkownika)
