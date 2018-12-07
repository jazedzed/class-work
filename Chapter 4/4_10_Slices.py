animals = ['cat', 'dog', 'whale', 'bear']
print("The first three items in the list are:")
for animal in animals[:3]:
	print(animal)
print("\nTwo items from the middle of the list are:")
for animal in animals[1:3]:
	print(animal)
print("\nThe last three items in the list are:")
for animal in animals[-3:]:
	print(animal)