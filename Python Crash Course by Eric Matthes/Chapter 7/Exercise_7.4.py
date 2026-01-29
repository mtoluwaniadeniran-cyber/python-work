prompt = "\nWelcome to PizzaTops! Enter your desired toppings: "
prompt += "\nEnter 'quit' when you finish.\n"

toppings = ""

while toppings != 'quit':
    toppings = input(prompt)
    if toppings != 'quit':
        print(f"I will be adding {toppings} to your pizza.")
    else:
        print("done")