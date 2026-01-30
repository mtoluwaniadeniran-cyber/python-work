sandwich_orders = ['Pastrami', 'Club Sandwich', 'Pastrami', 'Grilled Cheese Sandwich', 'Pastrami', 'Chicken Shawarma Sandwich', 'Pastrami', 'BLT', 'Pastrami', 'Tuna Melt Sandwich', 'Pastrami', 'Egg Salad Sandwich']
print(sandwich_orders)

print("Oops! We are out of Pastrami")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

print(sandwich_orders)