'''#Start with some designs that nees to be printed.
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
    print(completed_model)'''


#Reorganizing with functions
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
    Move each design to completed_models after printing."""
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        print(f"Printing model: {current_designs}")
        completed_models.append(current_designs)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe foloowing models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

print_models(unprinted_designs[:], completed_models)