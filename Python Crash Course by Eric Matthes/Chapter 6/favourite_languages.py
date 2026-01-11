'''favourite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

#language = favourite_language['jen'].title()
#print(f"Jen's favourite language is {language}.")

#Another method using loops
for name, language in favourite_language.items(): 
    print(f"{name.title()}'s favorite language is {language.title()}.")'''

#Looping through all keys in the dictionary
'''friends = ['phil', 'sarah']
for name in favourite_language: 
    #print(name.title())
    print(f"Hi {name.title()}.") 

if 'erin' not in favourite_language.keys(): 
    print("Erin, please take our poll!")

    if name in friends: 
        language = favourite_language[name].title() 
        print(f"\t{name.title()}, I see you love {language}!")

for name in sorted(favourite_language.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentioned:") 
#for language in favourite_language.values(): 
# Line 32 can be changed to:
for language in set(favourite_language.values()): 
    print(language.title())'''

#Nesting a list in a dictionary
favorite_languages = { 
'jen': ['python', 'rust'], 
'sarah': ['c'], 
    'edward': ['rust', 'go'], 
    'phil': ['python', 'haskell'], 
    } 
for name, languages in favorite_languages.items(): 
    print(f"\n{name.title()}'s favorite languages are:") 
    for language in languages: 
        print(f"\t{language.title()}")
        