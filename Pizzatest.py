import unittest
import Pizza
import PizzaBuilder

class TestPizzaBuilder(unittest.TestCase):

    def test_small_pizza_with_cheese(self):
        builder = Pizza.PizzaBuilder('small')
        builder.add_cheese()
        pizza = builder.build()
        self.assertEqual(str(pizza), 'Size: small, Cheese: True, Pepperoni: False, Mushrooms: False')

    def test_large_pizza_with_pepperoni_and_mushrooms(self):
        builder = Pizza.PizzaBuilder('large')
        builder.add_pepperoni()
        builder.add_mushrooms()
        pizza = builder.build()
        self.assertEqual(str(pizza), 'Size: large, Cheese: False, Pepperoni: True, Mushrooms: True')

if __name__ == '__main__':
    unittest.main()
