prompt = "Welcome to ZFilms!, to watch Frozen 4 please enter your age.\n"
age = input(prompt)
age = int(age)

while age != 0:
    if age < 3:
        print("Your ticket is free!.")
    elif age >= 3 and age < 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")
    age = input(prompt)
    age = int(age)



