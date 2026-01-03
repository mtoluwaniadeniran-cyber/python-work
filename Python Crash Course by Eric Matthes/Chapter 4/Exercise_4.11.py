pizzas = ['pepperoni', 'pineapple', 'suya']
friend_pizzas = pizzas[:]

pizzas.append('bbq chicken')
friend_pizzas.append('veggie')

for pizza in pizzas:
  print(f"My favourite pizzas are {pizza}.")

for pizza in friend_pizzas:
  print(f"\nMy friend's favourite pizzas are {pizza}.")