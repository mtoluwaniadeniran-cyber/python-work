my_foods = ['amala', 'fried rice', 'bread', 'spagetti']
friend_foods = my_foods[:]

my_foods.append('moi-moi')
friend_foods.append('meat pie')

print("My favourite foods are:")
for food in my_foods:
  print(food)

print("\nMy friend's favourite foods are:")
for food in friend_foods:
  print(food)