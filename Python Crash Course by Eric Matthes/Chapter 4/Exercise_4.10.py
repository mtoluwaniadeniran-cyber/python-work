my_foods = ['amala', 'fried rice', 'bread', 'spagetti', 'moi-moi', 'pounded yam', 'egusi soup ',  'jollof rice']
print("The first three items in the list are:")
for food in my_foods[:3]:
  print(food)

print("\nThree items from the middle of the list are:")
for food in my_foods[1:4]:
  print(food)

print("\nThe last three items in the list are:")
for food in my_foods[-3:]:
  print(food)