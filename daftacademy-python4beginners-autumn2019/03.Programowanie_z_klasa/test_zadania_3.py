import unittest
from zadania_3 import MyPolynomial


class TestMyPolynomial(unittest.TestCase):
    @staticmethod
    def test_zadanie_1():
        assert type(MyPolynomial()) is MyPolynomial
        assert type(MyPolynomial(1)) is MyPolynomial
        assert type(MyPolynomial(1, 2)) is MyPolynomial
        assert type(MyPolynomial(0, 0)) is MyPolynomial
        assert any(
            name.startswith("_") and not callable(name)
            for name in MyPolynomial().__dict__.keys()
        )
        # import ipdb  # Warto zobaczyć co to i jak używać 

        # ipdb.sset_trace()
    
    @staticmethod
    def test_zadanie_2():
        assert "1 + 2x^1" == str(MyPolynomial(1, 2))
        assert "MyPolynomial(1, 2)" == repr(MyPolynomial(1, 2))
        assert "MyPolynomial(0)" == repr(MyPolynomial())
        assert "MyPolynomial(0)" == repr(MyPolynomial(0, 0, 0))
        assert "0" == str(MyPolynomial(0, 0, 0))

    @staticmethod
    def test_zadanie_3():
        assert MyPolynomial(1, 2, 2)(0) == 1
        assert MyPolynomial(1, 2, 2)(1) == 5
        assert MyPolynomial(1, 2, 2)(2) == 13
        assert MyPolynomial(1, 2, 2)(3) == 25
        assert MyPolynomial(1, 2, 2)(4) == 41

    @staticmethod
    def test_zadanie_4():
        assert MyPolynomial(1, 2, 2) == MyPolynomial(1, 2, 2)
        assert (MyPolynomial(1, 2, 2) == MyPolynomial(1, 2)) is False
        assert MyPolynomial(0) == MyPolynomial()
        assert MyPolynomial(0, 0) == MyPolynomial(0)
        assert MyPolynomial(0, 0, 0) == MyPolynomial(0)
        assert MyPolynomial(1, 0, 0) == MyPolynomial(1)
        assert MyPolynomial(0, 1, 0) == MyPolynomial(0, 1)
        assert MyPolynomial(0, 1, 1) == MyPolynomial(0, 1, 1)

    @staticmethod
    def test_zadanie_5():
        assert MyPolynomial.from_iterable([0, 1, 2]) == MyPolynomial(0, 1, 2)
        assert MyPolynomial.from_iterable((0, 1, 2)) == MyPolynomial(0, 1, 2)
        assert MyPolynomial.from_iterable([1, 2, 2]) == MyPolynomial(1, 2, 2)
        assert (MyPolynomial.from_iterable((1, 2, 2)) == MyPolynomial(1, 2)) is False
        assert MyPolynomial.from_iterable([0]) == MyPolynomial()
        assert MyPolynomial.from_iterable([0, 0]) == MyPolynomial(0)
        assert MyPolynomial.from_iterable(set([0, 0, 0])) == MyPolynomial(0)

    @staticmethod
    def test_zadanie_6():
        assert MyPolynomial(5, 4).degree() == 1
        assert MyPolynomial().degree() == 0
        assert MyPolynomial(0, 0, 0).degree() == 0
        assert MyPolynomial(0, 1, 0).degree() == 1
        assert MyPolynomial(0, 0, 1).degree() == 2
        assert MyPolynomial.from_iterable([0, 1, 0]).degree() == 1

    @staticmethod
    def test_zadanie_7():
        assert MyPolynomial(5, 8) == MyPolynomial(2, 4) + MyPolynomial(3, 4)
        assert MyPolynomial(5, 4) == MyPolynomial(2) + MyPolynomial(3, 4)
        assert MyPolynomial(6, 4) == MyPolynomial(2, 4) + MyPolynomial(4)

        mp1 = MyPolynomial(2, 4)
        old_id = id(mp1)
        mp2 = MyPolynomial(3, 4)
        mp3 = MyPolynomial(5, 8)
        mp1 += mp2
        new_id = id(mp1)
        assert mp3 == mp1
        assert old_id == new_id, "After +=, you returned different object!"

    @staticmethod
    def test_zadanie_8():
        assert MyPolynomial(6, 14, 8) == MyPolynomial(2, 2) * MyPolynomial(3, 4)
        assert MyPolynomial(9, 6, 13, 4, 4) == MyPolynomial(3, 1, 2) * MyPolynomial(3, 1, 2)
        assert MyPolynomial(16, 24, 25, 20, 10, 4, 1) == MyPolynomial(
            4, 3, 2, 1
        ) * MyPolynomial(4, 3, 2, 1)
        assert MyPolynomial(1, 4, 7, 10, 8) == MyPolynomial(1, 2) * MyPolynomial(1, 2, 3, 4)
        assert MyPolynomial(1, 4, 7, 10, 8) == MyPolynomial(1, 2, 3, 4) * MyPolynomial(1, 2)
        assert MyPolynomial(6, 14, 8) == MyPolynomial(3, 7, 4) * 2
        assert MyPolynomial(9, 21, 12) == 3 * MyPolynomial(3, 7, 4)

        mp1 = MyPolynomial(3, 7, 4)
        mp1_old_id = id(mp1)
        mp2 = MyPolynomial(0)
        mp1 *= mp2
        mp1_new_id = id(mp1)
        assert mp1 == mp2, "Something went wrong with: MyPolynomial * MyPolynomial"
        assert mp1_old_id == mp1_new_id, "After *=, you returned different object!"

        mp1 = MyPolynomial(3, 7, 4)
        mp1_old_id = id(mp1)
        mp1 *= 0
        mp1_new_id = id(mp1)
        assert mp1 == MyPolynomial(0), "Something went wrong with: MyPolynomial *= number"
        assert mp1_old_id == mp1_new_id, "After *=, you returned different object!"


# print("TEST")
# my = MyPolynomial(1, 2, 2)
# print("{}:{}".format(id(my), my))
# my2 = MyPolynomial(1, 2, 3, 4)
# print("{}:{}".format(id(my2), my2))
# my3 = my + my2
# print("{}:{}".format(id(my3), my3))
# my4 = my + [1, 2, 3, 4]
# print("{}:{}".format(id(my4), my4))
# my5 = [1, 2, 3, 4] + my
# print("{}:{}".format(id(my5), my5))
# my6 = MyPolynomial()
# print("{}:{}".format(id(my6), my6))
# my6 += my
# print("{}:{}".format(id(my6), my6))
# print(my(2))
# my7 = MyPolynomial(-1, -2, -2)
# print("{}:{}".format(id(my7), my7))

if __name__ == '__main__':
    unittest.main()
