import unittest
from praca_domowa import *

class Tests(unittest.TestCase):
    """Manin Test class."""

    def test_3_1(self):
        assert type(MyPolynomial()) is MyPolynomial
        assert type(MyPolynomial(1)) is MyPolynomial
        assert type(MyPolynomial(1, 2)) is MyPolynomial
        assert type(MyPolynomial(0, 0)) is MyPolynomial
        assert any(["_MyPolynomial__" in name for name in MyPolynomial().__dict__.keys()])

    def test_3_2(self):
        assert "1 + 2x^1" == str(MyPolynomial(1, 2))
        assert "MyPolynomial(1, 2)" == repr(MyPolynomial(1, 2))
        assert "MyPolynomial(0)" == repr(MyPolynomial())
        assert "MyPolynomial(0)" == repr(MyPolynomial(0, 0, 0))
        assert "0" == str(MyPolynomial(0, 0, 0))

    def test_3_3(self):
        assert MyPolynomial(1, 2, 2)(0) == 1
        assert MyPolynomial(1, 2, 2)(1) == 5
        assert MyPolynomial(1, 2, 2)(2) == 13
        assert MyPolynomial(1, 2, 2)(3) == 25
        assert MyPolynomial(1, 2, 2)(4) == 41

    def test_3_4(self):
        assert MyPolynomial(1, 2, 2) == MyPolynomial(1, 2, 2)
        assert (MyPolynomial(1, 2, 2) == MyPolynomial(1, 2)) is False
        assert MyPolynomial(0) == MyPolynomial()
        assert MyPolynomial(0, 0) == MyPolynomial(0)
        assert MyPolynomial(0, 0, 0) == MyPolynomial(0)
        assert MyPolynomial(1, 0, 0) == MyPolynomial(1)
        assert MyPolynomial(0, 1, 0) == MyPolynomial(0, 1)
        assert MyPolynomial(0, 1, 1) == MyPolynomial(0, 1, 1)

    def test_3_5(self):
        assert MyPolynomial.from_iterable([0, 1, 2]) == MyPolynomial(0, 1, 2)
        assert MyPolynomial.from_iterable((0, 1, 2)) == MyPolynomial(0, 1, 2)
        assert MyPolynomial.from_iterable([1, 2, 2]) == MyPolynomial(1, 2, 2)
        assert (MyPolynomial.from_iterable((1, 2, 2)) == MyPolynomial(1, 2)) is False
        assert MyPolynomial.from_iterable([0]) == MyPolynomial()
        assert MyPolynomial.from_iterable([0, 0]) == MyPolynomial(0)
        assert MyPolynomial.from_iterable(set([0, 0, 0])) == MyPolynomial(0)

    def test_3_6(self):
        assert MyPolynomial(5, 4).degree() == 1
        assert MyPolynomial().degree() == 0
        assert MyPolynomial(0, 0, 0).degree() == 0
        assert MyPolynomial(0, 1, 0).degree() == 1
        assert MyPolynomial(0, 0, 1).degree() == 2
        assert MyPolynomial.from_iterable([0, 1, 0]).degree() == 1

    def test_3_7(self):
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

    def test_3_8(self):
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

    def test_4_1_1(self):
        assert '1 - 2x^1' == str(MyPolynomial(1, -2))
        assert '-1 + x^1 - 2x^2' == str(MyPolynomial(-1, 1, -2))
        assert '1 + 2x^2' == str(MyPolynomial(1, 0, 2))
        assert '-1 - 2x^2' == str(-MyPolynomial(1, 0, 2))
        assert '-1 - 2x^2 + x^7' == str(-MyPolynomial(1, 0, 2, 0, 0, 0, 0, -1))
        assert 'MyPolynomial(-1, -2)' == repr(MyPolynomial(-1, -2))
        assert 'MyPolynomial(-1, -2)' == repr(-MyPolynomial(1, 2))

    def test_4_1_2(self):
        assert MyPolynomial(2, 4) == MyPolynomial(5, 4) - 3
        assert MyPolynomial(0, 4, 1, 4) == (MyPolynomial(0, 4, 1, 4) - 2) + 2

    def test_4_1_3(self):
        assert MyPolynomial(2, 4) == MyPolynomial(5, 8) - MyPolynomial(3, 4)
        assert MyPolynomial(1, 1, 2, 2) == MyPolynomial(2, 2, 2, 2) - MyPolynomial(1, 1)
        assert MyPolynomial(3, 3, 2, 2) == MyPolynomial(2, 2, 2, 2) - -MyPolynomial(1, 1)

    def test_4_1_4(self):
        assert MyPolynomial(-2, -4) == -MyPolynomial(2, 4)
        assert MyPolynomial(-2, 4) == -MyPolynomial(2, -4)

    def test_4_2_1(self):
        assert MyPolynomial(1, 1) == MyPolynomial(2, 2) / 2
        assert MyPolynomial(3, 5, 6) == MyPolynomial(6, 10, 12) / 2
        assert MyPolynomial(3, -5, 6) == MyPolynomial(6, -10, 12) / 2
        assert MyPolynomial(3, -5, 6) == -MyPolynomial(6, -10, 12) / -2

    def test_4_3_1(self):
        data = [(1,), (1, 2, 3, 4), (MyPolynomial(1, 2), ), (100, ), ('yolo', ),
                (None, ), (True, ), ({}, ), (dict(), ),
                ]
        expect_exceptions = [False, False, False, False, True, True, True, True, True]
        params = zip(data, expect_exceptions)
        for args, expect_exception in params:
            if expect_exception:
                with self.assertRaises(InvalidInputOperandError):
                    MyPolynomial(*args)
            else:
                MyPolynomial(*args)

    def test_4_3_2(self):
        a = MyPolynomial(21, 37)
        b = MyPolynomial(14, 88)

        with self.assertRaises(OperationNotSupportedError):
            c = a ** b

        with self.assertRaises(OperationNotSupportedError):
            c = a // b

        with self.assertRaises(OperationNotSupportedError):
            c = a << b

        with self.assertRaises(OperationNotSupportedError):
            c = b >> a

        with self.assertRaises(OperationNotSupportedError):
            c = a ** 5

        with self.assertRaises(OperationNotSupportedError):
            c = a // 6

        with self.assertRaises(OperationNotSupportedError):
            c = a >> 1

        with self.assertRaises(OperationNotSupportedError):
            c = b << 9

        with self.assertRaises(OperationNotSupportedError):
            c = 9 / b

        with self.assertRaises(OperationNotSupportedError):
            x = 9
            x /= b

    def test_4_3_3(self):
        polynomianl = MyPolynomial(2)
        operands = ['yolo', [], {}, dict(), None, False, True, '', {1, 2}]
        for operand in operands:
            with self.assertRaises(InvalidOperandError):
                a = polynomianl + operand
            with self.assertRaises(InvalidOperandError):
                a = operand + polynomianl
            with self.assertRaises(InvalidOperandError):
                a = polynomianl * operand
            with self.assertRaises(InvalidOperandError):
                a = operand * polynomianl
            with self.assertRaises(InvalidOperandError):
                a = polynomianl / operand
            with self.assertRaises(InvalidOperandError):
                a = polynomianl - operand
            with self.assertRaises(InvalidOperandError):
                a = operand - polynomianl

    def test_4_4_1(self):

        with self.assertRaises(InvalidInputOperandError):
            MyPolynomial(MyPolynomial(1, MyPolynomial(1, 2, 3), "1"))

        assert MyPolynomial(MyPolynomial(1, 2, 3)) == MyPolynomial(1, 2, 3)
        assert MyPolynomial(MyPolynomial(-1, -2)) == -MyPolynomial(1, 2)
        assert MyPolynomial(1, MyPolynomial(-1, -2)) == MyPolynomial(1, -1, -2)

    def test_4_4_2(self):
        assert MyPolynomial(
            MyPolynomial(1, 2, 3),
            MyPolynomial(1, 2, 3),
            MyPolynomial(1, 2, 3)) == MyPolynomial(1, 3, 6, 5, 3)
        assert MyPolynomial(
            MyPolynomial(1, 2, 3),
            MyPolynomial(1, -2, 3),
            MyPolynomial(1, 2, -3)) == MyPolynomial(1, 3, 2, 5, -3)

    def test_4_4_3(self):
        x = MyPolynomial(MyPolynomial(1, 2, 3),
                         -MyPolynomial(2, MyPolynomial(1, 2, 3), 3, 4, MyPolynomial(1, 2, 3)),
                         MyPolynomial(1),
                         -5,
                         MyPolynomial(1),
                         MyPolynomial(1, 2, 3))

        assert x == MyPolynomial(1, 0, 3, -10, -6)


if __name__ == '__main__':
    unittest.main()
