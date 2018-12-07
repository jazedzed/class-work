def make_album(artist_name, album_title, tracks = ''):
	"""Return a dictionary of info about an album."""
	album_dictionary = {'artist': artist_name.title(), 'title': album_title.title()}
	if tracks:
		album_dictionary['tracks'] = tracks
	return album_dictionary
album = make_album('aimee mann', 'mental illness')
print(album)
album = make_album('ryan adams', 'heartbreaker')
print(album)
album = make_album("'til tuesday", 'voices carry', tracks = 11)
print(album)