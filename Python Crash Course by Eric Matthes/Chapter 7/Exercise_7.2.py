group = "Welcome to Tasty Food Resturant!\n"
group += "How many people are you expecting at your dinner table? \n"
group = input(group)
group = int(group)

if group >= 8:
    print("Please wait for 10 minutes while we find you a table.")
else:
    print("Your table is ready!")