invites = ["Michelle", "Richard", "Tolulope", "Wisdom", "David"]
print(f"Hi {invites[0]}!\nYou are invited to my New Years Eve dinner.")
print(f"Hi {invites[1]}!\nYou are invited to my New Years Eve dinner.")
print(f"Hi {invites[2]}!\nYou are invited to my New Years Eve dinner.")
print(f"Hi {invites[3]}!\nYou are invited to my New Years Eve dinner.")
print(f"Hi {invites[4]}!\nYou are invited to my New Years Eve dinner.")

print(f"\nUnfortunately, {invites[3]} is unavailable to attend the dinner so he is being replaced.\n")
invites[3] = "Prince"

print(f"Hi {invites[0]}!\nYou are invited to my New Years Eve dinner.")
print(f"Hi {invites[1]}!\nYou are invited to my New Years Eve dinner.")
print(f"Hi {invites[2]}!\nYou are invited to my New Years Eve dinner.")
print(f"Hi {invites[3]}!\nYou are invited to my New Years Eve dinner.")
print(f"Hi {invites[4]}!\nYou are invited to my New Years Eve dinner.")

print("\nI have found a bigger dinner table, so I will be inviting more guests!")
invites.insert(0, "Feranmi")
invites.insert(2, "Sharon")
invites.append("Uje")

print(f"Hi {invites[0]}!\nYou are invited to my New Years Eve dinner.")
print(f"Hi {invites[1]}!\nYou are invited to my New Years Eve dinner.")
print(f"Hi {invites[2]}!\nYou are invited to my New Years Eve dinner.")
print(f"Hi {invites[3]}!\nYou are invited to my New Years Eve dinner.")
print(f"Hi {invites[4]}!\nYou are invited to my New Years Eve dinner.")
print(f"Hi {invites[5]}!\nYou are invited to my New Years Eve dinner.")
print(f"Hi {invites[6]}!\nYou are invited to my New Years Eve dinner.")
print(f"Hi {invites[7]}!\nYou are invited to my New Years Eve dinner.")

print("\nDue to some circumstances, I can only invite two people to my dinner.\n")

remove_guests = invites.pop()
print(f"Hey, {remove_guests}, I am sorry to inform you that you can't come for my dinner anymore.")
remove_guests = invites.pop()
print(f"Hey, {remove_guests}, I am sorry to inform you that you can't come for my dinner anymore.")
remove_guests = invites.pop()
print(f"Hey, {remove_guests}, I am sorry to inform you that you can't come for my dinner anymore.")
remove_guests = invites.pop()
print(f"Hey, {remove_guests}, I am sorry to inform you that you can't come for my dinner anymore.")
remove_guests = invites.pop()
print(f"Hey, {remove_guests}, I am sorry to inform you that you can't come for my dinner anymore.")
remove_guests = invites.pop()
print(f"Hey, {remove_guests}, I am sorry to inform you that you can't come for my dinner anymore.")

print(f"\nHi {invites[0]}! You are still invited to my dinner.")
print(f"\nHi {invites[1]}! You are still invited to my dinner.")

del invites[1]
del invites[0]

print(f"\nFinal guests list: {invites}")

