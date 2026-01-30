sandwich_orders = ['Club Sandwich', 'Grilled Cheese Sandwich', 'Chicken Shawarma Sandwich', 'BLT', 'Tuna Melt Sandwich', 'Egg Salad Sandwich']
finished_sandwich = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich}.")
    finished_sandwich.append(current_sandwich)

print("\nThese sandwiches have been made:")
for sandwich in finished_sandwich:
    print(f"{sandwich}")
