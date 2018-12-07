usernames = []
prompt = "What is your username?"
if usernames == []:
	print("We need to find some users!")
else:
	username = input(prompt)
	if username == 'admin':
		print("Hello, admin. Would you like to see a status report?")
	else:
		print("Hello, " + username + "!")
