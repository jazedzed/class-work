prompt = ("\nEnter the moviegoer's age to find out the cost of a ticket. ")
prompt += ("\nEnter 'quit' when you are finished. ")
age = input(prompt)
while prompt != 'quit':
	continue
	if int(age) < 3:
		print("This moviegoer's ticket is free.")
	if int(age) >= 3 and int(age) <= 12:
		print("This moviegoer's ticket is $10.")
	if int(age) > 12:
		print("This moviegoer's ticket is $15.")