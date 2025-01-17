class Goods:

    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy

    def price_after_discount(self):
        if self.discount_strategy is not None:
            return self.price - self.discount_strategy(self.price)
        return self.price

    def __str__(self):
        return f'Price: {self.price} price after discount: {self.price_after_discount()} '


def on_sale_discount(order):
    return order / 2


def twenty_percent_discount(order):
    return order / 100 * 20


print(Goods(20000))
# Price: 20000, price after discount: 20000

print(Goods(20000, discount_strategy=twenty_percent_discount))
# Price: 20000, price after discount: 16000.0

print(Goods(20000, discount_strategy=on_sale_discount))
# Price: 20000, price after discount: 10000.0
