def make_album(artist_name, album_title):
    """Display a dictionary on an album"""
    artist_info = f"{artist_name}, {album_title}."
    return artist_info.title()

while True:
    print("\nWho is your favourite artist? ")
    print("\nWhat is your favourite ablum of the artist? ")
    print("(Enter 'q' if you want to quit)")

    art_name = input("Artist name: ")
    if art_name == 'q':
        break

    art_album = input("Album: ")
    if art_album == 'q':
        break

    info = make_album(art_name, art_album)
    print(f"\nYour line up is: {info} ")