def common_words(filename):
	"""Count how many times a word appears in a text."""
	try:
		with open(filename) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		message = "Sorry, the file " + filename + "cannot be found."
		print(message)
	else:
		# Count times the word "the" appears in the text.
		print("The word 'the' appears in " + filename + " " + str(contents.lower().count('the')) + " times.")

filenames = ['Beowulf.txt', 'Wuthering_Heights.txt', 'Old_English_Mansions.txt']
for filename in filenames:
	common_words(filename)