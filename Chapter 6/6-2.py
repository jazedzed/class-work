favorite_numbers = {
	'courtney': 5, 
	'julianne': 7, 
	'lisa': 2, 
	'hannah': 3, 
	'paul': 1,
	}
for person in favorite_numbers:
	print(person.title() + "'s favorite number is " + 
		str(favorite_numbers[person]) +
		".")