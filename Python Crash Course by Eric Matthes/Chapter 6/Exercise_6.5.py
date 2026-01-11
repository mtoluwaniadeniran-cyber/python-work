Rivers = {'Nile': 'Egypt', 'Mississippi': 'Noth America', 'Yellow River': 'China'}
for key, value in Rivers.items():
    print(f"The {key} runs through {value}.")

print('\n')
for river in Rivers.keys():
    print(river)

print('\n')
for country in Rivers.values():
    print(country)