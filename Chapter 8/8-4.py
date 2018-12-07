def make_shirt(message, size = 'large'):
	"""Display info about a shirt."""
	print("\nI'd like a size " + size + " shirt with a message that reads: " + message + ".")
make_shirt(message = 'I love Python')
make_shirt(message = 'I love Python', size = 'medium')
make_shirt(message = 'I love HTML', size = 'small')