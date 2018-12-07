prompt = "\nPlease enter two numbers, and I'll add them together. "
prompt += "\nEnter 'quit' to end the program. "

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'quit':
		break
	second_number = input("\nSecond number: ")
	if second_number == 'quit':
		break
	try:
		answer = int(first_number) + int(second_number)
	except ValueError:
		print("Please enter numerals, not text.")
	else:
		print(answer)