"""
W tym zadaniu zawsze będą poprawne dane.
Nie ma potrzeby obsługiwania sytuacji wyjątkowych.
Napisz klasę MyPolynomial → https://pl.wikipedia.org/wiki/Wielomian
Ta klasa ma reprezentować wielomian.
Ta klasa ma być mutowalna.
Ta klasa ma mieć jedno pole `prywatne`(prywatne przez konwencję). 
Nazwa pola - dowolna


1. Instancję klasy MyPolynomial powinno dać się utworzyć na następujące sposoby
(Po znaku komentarza jest opis, jak należy interpretować wartości wewnątrz):
    MyPolynomial()  # 0
    MyPolynomial(1)  # 1
    MyPolynomial(1, 2)  # 1 + 2x
    MyPolynomial(1, 2, 3)  # 1 + 2x + 3x^2


2. Instancje klasy MyPolynomial powinno dać się rzutować na string, 
zaimplementuj odpowiednie metody, w taki sposób, żeby polecenie str 
na obiekcie MyPolynomial(1,2,3) zwracało '1 + 2x + 3x^2'. Metoda 
reprezentacyjna(repr) dla MyPolynomial, powina zwracać strig w takiej postaci, 
żeby przeklejony do konsoli interpretera (bez '') mógł stworzyć obiekt 
o identycznej strukturze.

Przyklady:
    '1 + 2x^1' == str(MyPolynomial(1, 2))
    '1 + 1x^1 + 2x^2' == str(MyPolynomial(1, 1, 2))
    'MyPolynomial(1, 2)' == repr(MyPolynomial(1, 2))


3. Instancję obiektu klasy MyPolynomial powinniśmy móc wywołać z argumentem x.
Podobnie jak w matematyce piszemy:
w(x) = 1 + 2x  + 2x^2, kiedy podstawimy za x 2 mamy w(2), chcielibyśmy otrzymać wynik:
w(2) = 1 + 2*2 + 2*2^2 = 13

Przykład:
    w = MyPolynomial(1, 2, 2)
    w(2) == 13  # powinno zwrócić True


4. Nasze wielomiany powinno dać się porównywać, tak jak w przykładzie:

    MyPolynomial(5) == MyPolynomial(5, 1)  # powinno zwrócić False
    MyPolynomial() == MyPolynomial(0)  # powinno zwrócić True


5. Tworzenie obiektu MyPolynomial metodą from_iterable(iterable)

Przykłady:
    MyPolynomial.from_iterable([0, 1, 2]) == MyPolynomial(0, 1, 2)
    MyPolynomial.from_iterable((0, 1, 2)) == MyPolynomial(0, 1, 2)


6. Klasa MyPolynomial powinna mieć zaimplementowaną metodę degree, która zwraca stopień wielomianu.

Przykłady:
    MyPolynomial(5, 4).degree() == 1  # powinna zwrócić True
    MyPolynomial().degree() == 0  # powinna zwrócić True


7. Wielomiany powinno dać się do siebie dodać.

Przykłady:
    MyPolynomial(5, 8) == MyPolynomial(2, 4) + MyPolynomial(3, 4)
    mp1 = MyPolynomial(2, 4)
    mp2 = MyPolynomial(3, 4)
    mp3 = MyPolynomial(5, 8)
    mp1 += mp2
    mp3 == mp1


8. Wielomiany powinno dać się pomnożyć(*, *=), zarówno przez wielomian, jak i przez liczbę.
    MyPolynomial(6, 14, 8) == MyPolynomial(2, 2) * MyPolynomial(3, 4)
    MyPolynomial(6, 14, 8) == MyPolynomial(3, 7, 4) * 2
    MyPolynomial(6, 14, 8) == 2 * MyPolynomial(3, 7, 4)

"""
class MyPolynomial:
    pass
