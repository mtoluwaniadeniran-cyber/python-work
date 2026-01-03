buffet_menu = ("beef", "chicken", "fish", "vegetarian", "pasta")
# buffet_menu[0] = "lamb"  # This line is commented out because tuples are immutable
print("Original menu:")
for food in buffet_menu:
  print(food)

buffet_menu = ("lamb", "chicken", "salmon", "vegetarian", "pasta")
print("\nModified menu:")
for food in buffet_menu:
  print(food)