def read_contents(filename):
	"""Read the contents of a file."""
	try:
		with open(filename) as file_object:
			contents = file_object.read()
			print(contents)
	except FileNotFoundError:
		pass

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
	read_contents(filename)