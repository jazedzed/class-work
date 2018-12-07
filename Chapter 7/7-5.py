prompt = ("\nEnter the moviegoer's age to find out the cost of a ticket. ")
prompt += ("\nEnter 'quit' when you are finished. ")
age = " "
while age != 'quit':
	age = input(prompt)
	if age != 'quit':
		if int(age) < 3:
			print("This moviegoer's ticket is free.")
		elif int(age) < 13:
			print("This moviegoer's ticket is $10.")
		else:
			print("This moviegoer's ticket is $15.")