def show_magicians(magicians):
	"""Print the name of each magician in the list."""
	for magician in magicians:
		print(magician.title())
magicians = ['mike', 'molly', 'mark']
show_magicians(magicians)