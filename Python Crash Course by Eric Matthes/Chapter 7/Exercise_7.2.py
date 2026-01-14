group = input("Welcome to Tasty Food Resturant! How many people are you expecting at your dinner table? \n")
group = int(group)
if group >= 8:
    print("Please wait for 10 minutes while we find you a table")
else:
    print("Your table is ready!")