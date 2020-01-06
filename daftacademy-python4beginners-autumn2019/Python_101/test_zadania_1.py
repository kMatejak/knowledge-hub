import unittest
import zadania_1 as z


class TestZadania1(unittest.TestCase):
    @staticmethod
    def test_zadanie_1():
        # ZADANIE 1
        # Stwórz listę liczb od 0 do 999.
        # Liczby podzielne przez 5 zastąp słowem '❤️'.
        # Liczby podzielne przez 7 zastąp słowem '🐍'.
        # Liczby podzielne przez 11 zastąp słowem '🐕'.
        # Liczby podzielne jednocześnie przez 11 i 5 zastąp słowem '🐕❤️'.
        # Liczby podzielne jednocześnie przez 5 i 7 zastąp słowem '❤️🐍'.
        # Liczby podzielne jednocześnie przez 11 i 7 zastąp słowem '🐕🐍'.
        # Liczby podzielne jednocześnie przez 11,5,7 zastąp słowem '🐕❤️🐍'.
        # Wynikową listę zwróć na końcu fukcji zadanie_1.
        z1 = z.zadanie_1()
        assert type(z1) is list, "result is not a list"
        assert len(z1) == 1000, "result list is too small"
        assert z1[11 * 5 * 7 * 2] == "🐕❤️🐍"

    @staticmethod
    def test_zadanie_2():
        # ZADANIE 2
        # Napisać kod tworzący listę krotek kolejnych elementów nieparzystych < 100 według
        # schematu: [(1,), (3,), ... , (99,)]. Wynikową listę zwróć na końcu funkcji zadanie_2.
        z2 = z.zadanie_2()
        assert type(z2) is list, "result is not a list"
        assert len(z2) == 50, "result list is too small"
        assert z2[1] == (2,)
        for x in z2:
            assert type(x) is tuple, f"{x} is not a tuple!"
            assert len(x) == 1, f"Tuple is too small: {x}"
            assert x[0] % 2 == 0, f"This value is even: {x[0]}"

    @staticmethod
    def test_zadanie_3():
        # ZADANIE 3
        # Napisz kod transformujący podany słownik:
        # {
        #     1: 'Mateusz',
        #     2: 'Marcin',
        #     3: 'Wojciech',
        #     4: 'Marcin',
        #     5: 'Michał',
        #     6: 'Antonii',
        #     7: 'Katarzyna',
        #     8: 'Agata'
        # }
        # do postaci:
        # {
        #     'Mateusz': 1,
        #     'Marcin': 2,
        #     ...
        #     'Agata': 8
        # }
        # (Zamiana klucza z wartością).
        # Wynik przypisz do zmiennej result
        names = {
            1: "Mateusz",
            2: "Marcin",
            3: "Wojciech",
            4: "Marcin",
            5: "Michał",
            6: "Antonii",
            7: "Katarzyna",
            8: "Agata",
        }
        z3 = z.zadanie_3()
        assert type(z3) is dict, f"{z3} is not a dict!"
        assert len(z3) == len(names) - 1, f"{z3} is too big!"
        assert "Mateusz" in z3, f"There is not Mateusz in your result: {z3}"

    def test_zadanie_4(self):
        # ZADANIE 4
        # Napisz program tworzący ze zbioru U = {'👻', '🕵', '🔺', '🐉', '🐍', '🦂', '🔥', '🌻', '🐙', '🌌'}
        # zbiór zawierający wszystkie podzbiory U (włącznie z pustym i U).
        # UWAGA: w python zbiory (set) nie mogą być elementami innych zbiorów,
        # proszę użyć frozenset jako zbiorów wewnętrznych.
        # Wynik przypisz do zmienej result
        z4 = z.zadanie_4()

        assert type(z4) is set, "Your results is not a set"
        assert len(z4) == 1024, "Your results are too short"
        assert (
                frozenset(("👻", "🕵", "🔺", "🐉", "🐍", "🦂", "🔥", "🌻", "🐙", "🌌")) in z4
        ), "You could not omit any set!"
        assert frozenset() in z4, "You could not omit any set!"


if __name__ == '__main__':
    unittest.main()
