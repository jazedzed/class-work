def make_album(artist_name, album_title, tracks = ''):
	"""Return a dictionary of info about an album."""
	album_dictionary = {'artist': artist_name.title(), 'title': album_title.title()}
	return album_dictionary
while True:
	print("\nPlease enter the artist and album title. ")
	print("(enter 'q' at any time to quit)")
	a_name = input("Artist name: ")
	if a_name == 'q':
		break
	a_title = input("Album title: ")
	if a_title == 'q':
		break
	album = make_album(a_name, a_title)
	print(album)