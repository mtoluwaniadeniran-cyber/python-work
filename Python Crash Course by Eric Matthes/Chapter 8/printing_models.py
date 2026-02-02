#Start with some designs that nees to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

#Simulate printing each design, until none are left.
#Move each design to completed_models after printing
while unprinted_designs:
    current_designs = unprinted_designs.pop()
    print(f"Printing model: {current_designs}")
    completed_models.append(current_designs)

#Display all completed models.
print("\nThe foloowing models have been printed: ")
for completed_model in completed_models:
    print(completed_model)