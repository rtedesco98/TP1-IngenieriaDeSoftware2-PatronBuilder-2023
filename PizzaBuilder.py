from Pizza import PizzaBuilder


builder = PizzaBuilder('large')
builder.add_cheese()
builder.add_pepperoni()
pizza = builder.build()
print(pizza)
