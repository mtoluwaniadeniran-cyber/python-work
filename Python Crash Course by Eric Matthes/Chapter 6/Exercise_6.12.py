favourite_books = {
    'Margaret': {
        'Self-Development': 'Atomic Habits',
        'Faith': 'Purpose Driven Life',
        'Technology': 'Clean Code'
    },
    'Daniel': {
        'Fiction': 'The Alchemist',
        'Philosophy': 'Man’s Search for Meaning',
        'Self-Development': 'Deep Work'
    },
    'Aisha': {
        'Business': 'Think and Grow Rich',
        'Finance': 'The Psychology of Money',
        'Biography': 'Becoming'
    },
    'Samuel': {
        'Finance': 'Rich Dad Poor Dad',
        'Self-Development': 'The 7 Habits of Highly Effective People',
        'Leadership': 'Leaders Eat Last'
    },
    'Grace': {
        'Faith': 'The Purpose Driven Life',
        'Fiction': 'Redeeming Love',
        'Poetry': 'Milk and Honey'
    }
}

for name, genres in favourite_books.items():
    print(f"\nThis are {name}'s favourite books:")

    for genre in genres:
        print(f"{genre}: {genres[genre]}")