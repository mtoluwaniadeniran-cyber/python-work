favourite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'tolu': 'ruby',
    'kenneth': 'SQL'
    }

poll_list = ['jen', 'sarah', 'edward', 'phil', 'tolu', 'kenneth', 'erni', 'jade' ]
for name in poll_list:
    if name not in favourite_language:
        print(f"Hey {name}, please respond to the poll.")
    else:
        print(f"\nHi {name}, thank you for responding to the poll.")