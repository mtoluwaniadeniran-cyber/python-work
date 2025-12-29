my_fav_things = ['purple', 'God', 'music', 'productivity']
print(my_fav_things)

"\n", print(my_fav_things[1].title())

my_fav_things = ['purple', 'God', 'music', 'productivity']
message = f"My favourite colour is {my_fav_things[0]}."
print(message)

my_fav_things[2] = 'Youtube'
print(my_fav_things)

my_fav_things.append('family')
print(my_fav_things)

my_fav_things.insert(4, 'friends')
print(my_fav_things)

del my_fav_things[3]
print(my_fav_things)

popped_favs = my_fav_things.pop()
print(popped_favs)

my_fav_things.remove('purple')
print(my_fav_things)

my_fav_things.sort()
print(my_fav_things)

my_fav_things.sort(reverse=True)
print(my_fav_things)

print(sorted(my_fav_things))

my_fav_things.reverse()
print(my_fav_things)

print(len(my_fav_things))