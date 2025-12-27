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
