#Version one
'''prompt = "Welcome to ZFilms!, to watch Frozen 4 please enter your age.\n"
age = input(prompt)
age = int(age)

while age != 0:
    if age < 3:
        print("Your ticket is free!.")
    elif age >= 3 and age < 12:
        print("Your ticket is $10.")
    elif age >= 12:
        print("Your ticket is $15.")
if age <= 0:
    print ("end!")
    
#Version two
prompt = "Welcome to ZFilms!, to watch Frozen 4 please enter your age.\n"

active = True
while active:
    age =input(prompt)
    age = int(age)

    if age == 0:
        active =  False
    else:
        if age > 0 and age < 3:
            print("Your ticket is free!.")
        elif age >= 3 and age < 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")

print ("end!")'''

#Version three
prompt = "Welcome to ZFilms!, to watch Frozen 4 please enter your age.\n"

while True:
    age = input(prompt)

    if age == 'quit':
        print("Thanks!")
        break

    age = int(age)

    if age < 3:
        print("Your ticket is free!.")
    elif age >= 3 and age < 12:
        print("Your ticket is $10.")
    elif age >= 12:
        print("Your ticket is $15.")