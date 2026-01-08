current_users = ['alice', 'bob', 'charlie', 'david', 'eve']
new_users = ['Frank', 'Grace', 'alice', 'Heidi', 'Bob']
 
for user in new_users:
    if user.lower() in current_users:
        print("Oops!, this username is taken. Please enter a new username.")
    else:
        print("This user name is available.")