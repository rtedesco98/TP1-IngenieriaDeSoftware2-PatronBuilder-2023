
class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False

    def __str__(self):
        return f'Size: {self.size}, Cheese: {self.cheese}, Pepperoni: {self.pepperoni}, Mushrooms: {self.mushrooms}'

class PizzaBuilder:
    def __init__(self, size):
        self.pizza = Pizza()
        self.pizza.size = size

    def add_cheese(self):
        self.pizza.cheese = True

    def add_pepperoni(self):
        self.pizza.pepperoni = True

    def add_mushrooms(self):
        self.pizza.mushrooms = True

    def build(self):
        return self.pizza
