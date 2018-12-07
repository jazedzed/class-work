favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby', 
	'phil': 'python',
	}
people = ['jen', 'sarah', 'edward', 'phil', 'julianne', 'paul']
for person in people:
	if person in favorite_languages:
		print("Thank you for taking the poll, " + person.title() + "!")
	else:
		print("Please take the poll, " + person.title() + ".")