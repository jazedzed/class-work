import json

filename = 'book.json'

with open(filename) as file_object:
	book = json.load(file_object)
	print("I remember your favorite book. It's " + book + "!")