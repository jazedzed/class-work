def make_sandwich(*contents):
	"""Print the list of sandwich contents that have been requested."""
	print("\nMaking a sandwich with the following contents:")
	for content in contents:
		print("- " + content)
make_sandwich('ham', 'cheese')
make_sandwich('hummus', 'sprouts', 'tomatoes')
make_sandwich('turkey', 'lettuce', 'mayo', 'mustard')