favorite_numbers = {
	'courtney': [5, 21], 
	'julianne': [7, 2], 
	'lisa': [2, 3], 
	'hannah': [3, 13],
	'paul': [1, 2],
	}
for person, numbers in favorite_numbers.items():
	print("\n" + person.title() + "'s favorite numbers are:")
	for number in numbers:
		print("\t" + str(number))