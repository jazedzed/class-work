import json

book = input("What is your favorite book? ")

filename = 'book.json'
with open(filename, 'w') as file_object:
	json.dump(book, file_object)
	print("I'll remember your favorite book. I promise!")