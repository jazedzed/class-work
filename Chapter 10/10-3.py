prompt = "\nPlease enter your username: "

filename = 'guest.txt'
with open(filename, 'w') as file_object:
	file_object.write(input(prompt))