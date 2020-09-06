import unittest


class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


class Cart(Product):
    def __init__(self):
        self.total_price = None
        self.cart = {}

    def add_product(self):
        if self.count <= 5:
            self.total_price = self.price * self.count
            return self.total_price
        elif self.count <= 7:
            self.total_price = (self.price - (self.price / 100 * 5)) * self.count
            return self.total_price
        elif self.count <= 10:
            self.total_price = (self.price - (self.price / 100 * 10)) * self.count
            return self.total_price
        elif self.count <= 20:
            self.total_price = (self.price - (self.price / 100 * 30)) * self.count
            return self.total_price
        elif self.count > 20:
            self.total_price = (self.price - (self.price / 100 * 50)) * self.count
            return self.total_price


# class CartTest(unittest.TestCase):
#     def test1(self):
#         print('test 1')

apple = Product("apple", 32, 4)
# print(count_tests > 0)
#
# print(failures)
#
# print(errors)
# print(assertEqual)
