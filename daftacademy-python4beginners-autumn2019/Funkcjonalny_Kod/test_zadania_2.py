import unittest
import zadania_2 as z


class TestZadania1(unittest.TestCase):

	@staticmethod
	def test_power():
		# Zadanie 1
		# Napisz funkcję power, która dla danego n i p zwraca w wyniku n podniesione do
		# potęgi p.
		# Domyślna wartość argumentu p to 3.
		# Niech n i p będą liczbami całkowitymi >= 0.
		assert z.power(5) == 125
		assert z.power(5, 3) == 125
		assert z.power(0, 0) == 1
		assert z.power(0) == 0

	@staticmethod
	def test_fold():
    	# Zadanie 2
        # Napisz funkcję fold.
		# Funkcja ma na celu mnożenie kolejnych par elementów zadanej listy i
		# zwrócenie listy iloczynów kolejnych par.
		# Jeżeli listy wejściowe są nierówne, na ostatnich pozycjach listy wyjściowej
		# powinny znaleźć się 0. Tyle 0, ile jest różnicy między listami.

		# Tego jak obsłużyć niepoprawny dane, czy to z wejścia, czy też powstawe
		# podczas ich przetwarzania, dowiecie się na wykładzie 4
		assert z.fold(None, None) == []
		assert z.fold([1, 2, 3], [1, 2, 3]) == [1, 4, 9]
		assert z.fold([1, 2], [1, 2, 3]) == [1, 4, 0]
		assert z.fold(None, [1, 2, 3]) == [0, 0, 0]
		assert z.fold([1, 2, 3], None) == [0, 0, 0]


if __name__ == '__main__':
	unittest.main()
