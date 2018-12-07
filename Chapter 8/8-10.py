def show_magicians(magicians):
	"""Print the name of each magician in the list."""
	for magician in magicians:
		print(magician.title())
def make_great(magicians):
	"""Modify each magician's name by adding 'the Great' to the end."""
	great_magicians = []
	while magicians:
		magician = magicians.pop()
		great_magician = magician + ' the Great'
		great_magicians.append(great_magician)
	for great_magician in great_magicians:
		magicians.append(great_magician)
magicians = ['mike', 'molly', 'mark']
show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)