filename = 'programming_poll.txt'

prompt = "\nWhy do you like programming? "
prompt += "\nEnter 'quit' when you are finished. "

while True:
	reason = input(prompt)

	if reason == 'quit':
		break
	else:
		with open(filename, 'a') as file_object:
			file_object.write(reason + "\n")