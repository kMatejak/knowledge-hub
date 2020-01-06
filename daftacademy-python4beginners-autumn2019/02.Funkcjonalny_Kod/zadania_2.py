pan_tadeusz = ""  # do pobrania z projektu Gutenberg

# Zadanie 1
# Napisz funkcję power, która dla danego n i p zwraca w wyniku n 
# podniesione do potęgi p.
# Domyślna wartość argumentu p to 3.
# Niech n i p będą liczbami całkowitymi >= 0.
def power(n, p=3):
    pass


# Zadanie 2
# Napisz funkcję fold.
# Funkcja ma na celu mnożenie kolejnych par elementów zadanej listy i
# zwrócenie listy iloczynów kolejnych par.
# Jeżeli listy wejściowe są nierówne, na ostatnich pozycjach listy wyjściowej
# powinny znaleźć się 0. Tyle 0, ile jest różnicy między listami.

# Tego jak obsłużyć niepoprawny dane, czy to z wejścia, czy też powstawe
# podczas ich przetwarzania, dowiecie się na wykładzie 4
def fold(a=None, b=None):
    pass


# Zadanie 3
# Napisz funkcję word_frequency, która przyjmuje jako argument string.
# Dla podanego stringa funkcja musi zliczyć ile razy wystąpił każdy wyraz.
# Zwróc wynik jako słownik wartości ile razy wystąpił każdy wyraz, gdzie klucz
# to występujący wyraz a wartścią jest liczba wystąpień tego wyrazu.

# Do tego zadania brak testów w pliku źródłowym, są przedstawione różne 
# rozwiązania - optymalne i nadesłane przez studentów [~Krzysztofor].
def word_frequency(text=None):
    pass


# Zadanie 4
# Napisz funkcję hexagonal_list, która dla danego n obliczy n liczb ciągu
# hexagonal number series → https://edublognss.wordpress.com/2013/04/16/famous-mathematical-sequences-and-series/
# Załóż, że n >= 1 i jest liczbą całkowitą

# Do tego zadania brak testów w pliku źródłowym [~Krzysztofor].
def hexagonal_list(n):
    pass


# ZADANIE 5
# Napisz funkcję doskonale, ktora zwraca listę wszystich liczb doskonałych
# mniejszych bądź równych zadanemu n
# Wewnątrz, stwórz funkcję suma_dzielnikow, która zwraca sumę
# dzielników właściwych zadanej liczby

# To rozwiązanie nawiązuje swoją budową (funkcją suma_dzielników w funkcji doskonale)
# do struktury dekoratora:
# https://realpython.com/primer-on-python-decorators/
# Dekoratory są omawiane na drugiej edycji kursu ("Python Level Up", przyp. Krzysztofora(:)

# Do tego zadania brak testów w pliku źródłowym [~Krzysztofor].
def doskonale(n):
    def suma_dzielnikow(k):
        pass
    pass
