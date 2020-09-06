import unittest
import math


def quadratic_equation(a, b, c):
    try:
        D = b ** 2 - 4 * a * c
        if D == 0:
            x = -b / (2 * a)
            return x

        elif D > 0:
            x1 = (-b - math.sqrt(D)) / (2 * a)
            x2 = (-b + math.sqrt(D)) / (2 * a)
            return x2, x1
        elif D < 0:
            return None
    except ZeroDivisionError:
        print("Zero Division Error")


class QuadraticEquationTest(unittest.TestCase):

    def test_discriminant_greater_than_zero(self):
        self.assertEqual(quadratic_equation(1, -8, 12), (6.0, 2.0))

    def test_discriminant_less_than_zero(self):
        self.assertEqual(quadratic_equation(5, 3, 7), None)

    def test_discriminant_equal_zero(self):
        self.assertEqual(quadratic_equation(1, -6, 9), 3.0)

    def test_discriminant_equal_zero_2(self):
        self.assertEqual(quadratic_equation(1, -4, 4), 2.0)

    if __name__ == '__main__':
        unittest.main()


print(quadratic_equation(2, 1, -1))

print(quadratic_equation(1, -4, 4))

print(quadratic_equation(4, 1, 2))
print(quadratic_equation(1, -8, 12))
print(quadratic_equation(1, -6, 9))
