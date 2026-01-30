def make_shirt(size, text='I love Python'):
    """Display text on shirt"""
    print(f"Your shirt size is {size} and '{text.title()}' is printed on it.")

make_shirt('large')
make_shirt('medium')

def make_shirt(text, size='small'):
    """Display text on shirt"""
    print(f"Your shirt size is {size} and '{text.title()}' is printed on it.")

make_shirt('God is so good')
make_shirt('god is intentional about me')