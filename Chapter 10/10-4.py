filename = 'guest_book.txt'

prompt = "\nPlease enter your name. "
prompt += "\nEnter 'quit' to end the program. "

while True:
	name = input(prompt)

	if name == 'quit':
		break
	else:
		with open(filename, 'a') as file_object:
			file_object.write(name + "\n")
		print("You have been added to the guest book, " + name + ".")