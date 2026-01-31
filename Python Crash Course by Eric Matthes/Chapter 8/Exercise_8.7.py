def make_album(artist_name, album_title, album_number=None):
    """Display a dictionary on an album"""
    if album_number !=None:
        musician = {'name': artist_name, 'title': album_title, 'songs': album_number}
    else:
        musician = {'name': artist_name, 'title': album_title}
    return musician

musician= make_album('Asa', 'Beautiful Imperfection', 5)
print(musician)