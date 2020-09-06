"""Create a Pizza class with the attributes order_number and ingredients (which is given as a list).
 Only the ingredients will be given as input.

You should also make it so that its possible to choose a ready made pizza flavour rather than typing out
the ingredients manually! As well as creating this Pizza class, hard-code the following pizza flavours."""


class Pizza:
    order_number = 0

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.order_number = Pizza.order_number
        Pizza.order_number += 1

    def garden_feast():
        ingredients = ['spinach', 'olives', 'mushrooms']
        return Pizza(ingredients)

    def hawaiian():
        ingredients = ['ham', 'pineapple']
        return Pizza(ingredients)

    def meat_festival():
        ingredients = ['beef', 'meatball', 'bacon']
        return Pizza(ingredients)


p1 = Pizza(['bacon', 'parmesan', 'ham'])
print(p1.ingredients)
p2 = Pizza.garden_feast()
print(p2.ingredients)
p3 = Pizza.hawaiian()
print(p3.ingredients)
p4 = Pizza.meat_festival()
print(p4.ingredients)
p5 = Pizza(["pepperoni", "bacon"])
print(p5.ingredients)
my_pizza = Pizza(['cheese', 'caviar', 'oyster', 'uranium'])

print(my_pizza.ingredients)
print(p1.order_number)
print(p2.order_number)
print(p3.order_number)
print(p4.order_number)
print(p5.order_number)
print(my_pizza.order_number)
