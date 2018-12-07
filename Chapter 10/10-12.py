import json

# Load the book, if it has been stored previously.
# Otherwise, prompt for the book and store it.

filename = 'book.json'
try:
	with open(filename) as file_object:
		book = json.load(file_object)
except FileNotFoundError:
	book = input("What is your favorite book? ")
	with open(filename, 'w') as file_object:
		json.dump(book, file_object)
		print("I'll remember your favorite book. I promise!")
else:
	print("I remember your favorite book. It's " + book + "!")