user = input("Please enter a number: ")
user = int(user)

if user % 10 == 0:
    print(f"{user} is a multiple of 10.")
else:
    print(f"{user} is not a multiple of 10.")