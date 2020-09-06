"""

Question textCreate class Triangle with method get_area() that calculate area of triangle. As input you will have list of 3 sides size
Examples:
triangle = Triangle([3, 3, 3])
Use classes TriangleNotValidArgumentException and TriangleNotExistException
Create class TriangleTest with parametrized unittest for class Triangle
test data:
valid_test_data = [
    ((3, 4, 5), 6.0),
    ((10, 10, 10), 43.30),
    ((6, 7, 8), 20.33),
    ((7, 7, 7), 21.21),
    ((50, 50, 75), 1240.19),
    ((37, 43, 22), 406.99),
    ((26, 25, 3), 36.0),
    ((30, 29, 5), 72.0),
    ((87, 55, 34), 396.0),
    ((120, 109, 13), 396.0),
    ((123, 122, 5), 300.0)
]
not_valid_triangle = [
    (1, 2, 3),
    (1, 1, 2),
    (7, 7, 15),
    (100, 7, 90),
    (17, 18, 35),
    (127, 17, 33),
    (145, 166, 700),
    (1000, 2000, 1),
    (717, 17, 7),
    (0, 7, 7),
    (-7, 7, 7)
]
not_valid_arguments = [
    ('3', 4, 5),
    ('a', 2, 3),
    (7, "str", 7),
    ('1', '1', '1'),
    'string',
    (7, 2),
    (7, 7, 7, 7),
    'str',
    10,
    ('a', 'str', 7)
]

"""

import unittest
import math


class TriangleNotValidArgumentException(Exception):
    pass


class TriangleNotExistException(Exception):
    pass


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        try:
            if (type(self.a) is not int) or (type(self.b) is not int) or (type(self.c) is not int):
                raise TriangleNotValidArgumentException
            elif ((self.a + self.b) > self.c and (self.b + self.c) > self.a and (self.a + self.c) > self.b) == False:
                raise TriangleNotExistException
            else:
                p = (self.a + self.b + self.c) / 2
                S = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
                return round(S, 2)
        except TriangleNotExistException:
            print('error')
        except TriangleNotValidArgumentException:
            print('error 2')


class TriangleTest(unittest.TestCase):
    valid_test_data = [
        ((3, 4, 5), 6.0),
        ((10, 10, 10), 43.30),
        ((6, 7, 8), 20.33),
        ((7, 7, 7), 21.21),
        ((50, 50, 75), 1240.19),
        ((37, 43, 22), 406.99),
        ((26, 25, 3), 36.0),
        ((30, 29, 5), 72.0),
        ((87, 55, 34), 396.0),
        ((120, 109, 13), 396.0),
        ((123, 122, 5), 300.0)
    ]
    not_valid_triangle = [
        (1, 2, 3),
        (1, 1, 2),
        (7, 7, 15),
        (100, 7, 90),
        (17, 18, 35),
        (127, 17, 33),
        (145, 166, 700),
        (1000, 2000, 1),
        (717, 17, 7),
        (0, 7, 7),
        (-7, 7, 7)
    ]
    not_valid_arguments = [
        ('3', 4, 5),
        ('a', 2, 3),
        (7, "str", 7),
        ('1', '1', '1'),
        'string',
        (7, 2),
        (7, 7, 7, 7),
        'str',
        10,
        ('a', 'str', 7)
    ]

    def setUp(self):
        self.my_data = Triangle({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})

    def test_valid_data(self):
        for data in TriangleTest.valid_test_data:
            self.my_data.get_area(data)
            with self.subTest():
                self.assertEqual(self.my_data.get_area, data)

    def tearDown(self):
        self.my_data = None


t1 = Triangle(3, 4, 5)
print(t1.get_area())
t2 = Triangle(10, 10, 10)
print(t2.get_area())

t3 = Triangle(1, 2, 3)
print(t3.get_area())

t4 = Triangle(3, 5, '4')
print(t4.get_area())
