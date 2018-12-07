prompt = ("\nEnter the toppings you would like, and they will be added to your pizza." )
prompt += ("\nEnter 'quit' to end the program. ")
message = " "
while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(message.title() + " will be added to your pizza.")