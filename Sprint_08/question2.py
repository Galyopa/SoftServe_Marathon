import unittest


def divide(num_1, num_2):
    return float(num_1) / num_2


class DivideTest(unittest.TestCase):

    def test_zero_division(self):
        self.assertRaises(ZeroDivisionError, divide, 3, 0)

    def test_positive_divide(self):
        expected = 0.6666666
        actual = divide(2, 3)
        self.assertAlmostEqual(expected, actual, 6)

    def test_negative_divide(self):
        expected = -0.6666666
        actual = divide(-2, 3)
        self.assertAlmostEqual(expected, actual, 6)



    if __name__ == '__main__':
        unittest.main()


print(divide(2, 3))
