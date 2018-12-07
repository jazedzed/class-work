responses = {}
polling_active = True
while polling_active:
	name = input("\nWhat is your name? ")
	response = input("If you could go anywhere on vacation, what destination would you choose? ")
	responses[name] = response
	repeat = input("\nWould you like to let another person respond? Enter 'yes' or 'no.' ")
	if repeat == 'no':
		polling_active = False
print("\n--- Poll results ---")
for name, response in responses.items():
	print(name.title() + " would like to go to " + response.title() + " on vacation.")