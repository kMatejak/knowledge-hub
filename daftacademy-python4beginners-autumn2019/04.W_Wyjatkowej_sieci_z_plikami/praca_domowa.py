"""Praca domowa.

Zadanie 1:
Rozszerzyć modelową lub własną implementację klasy MyPolynomial.
Dodać:
    obsługę liczb ujemnych
    odejmowanie z liczbą
    odejmowanie wielomianów klasy MyPolynomial

    '-1 - 2x' == str(MyPolynomial(-1, -2))
    '1x - 2x^2' == str(MyPolynomial(0, 1, -2))
    'MyPolynomial(-1, -2)' == repr(MyPolynomial(-1, -2))

    MyPolynomial(2, 4) == MyPolynomial(5, 8) - MyPolynomial(3, 4)
    MyPolynomial(-1) == MyPolynomial(2, 4) -= MyPolynomial(3, 4)
    MyPolynomial(0, 2, 3) == MyPolynomial(0, 2, 3) - 1


Zadanie 2:
Klasa MyPolynomial powinna też obsługiwać dzielenie przez liczbę
    MyPolynomial(6, 14, 8) == MyPolynomial(12, 28, 16) / 2

Zadanie 3:
Dane wejściowe Tworzenia klasy MyPolynomial mogą nie być poprawne.
Z tego powodu klasa MyPolynomial powinna walidować wejściowe parametry i ich poprawność.
By to osiągnąć zaimplementuj następujące wyjątki:
    InvalidOperandError
    InvalidInputOperandError
    OperationNotSupportedError

Przykład:
    MyPolynomial(5, 4) + "10" #  <- ten test ma rzucić wyjątkiem InvalidOperand
    MyPolynomial(5, [12])     #  <- ten test ma rzucić wyjątkiem InvalidInputOperand
    MyPolynomial(99, 100)**2  #  <- ten test ma rzucić wyjątkiem OperationNotSupported


Pamiętaj jednak że wszystkie dotychczasowej operacje na MyFraction z Zadań 3.1 - 3.8
powinny wciąż działać.
"""

from itertools import zip_longest
from collections import defaultdict


class GenericPolynomialError(Exception):
    """Base exception for all Polynomial exceptions."""

    pass


class InvalidOperandError(GenericPolynomialError):
    """Trhow this exception when Invalid Operand."""

    pass


class InvalidInputOperandError(GenericPolynomialError):
    """Trhow this exception when Invalid Input."""

    pass


class OperationNotSupportedError(GenericPolynomialError):
    """Trhow this exception when Invalid Operation on object."""

    pass


class MyPolynomial:
    """MyPolynomial class definition."""

    pass
