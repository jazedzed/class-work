current_users = ['julianne', 'dj', 'lisa', 'paul', 'ed']
new_users = ['kate', 'erin', 'sean', 'layla', 'ED']
for username in new_users:
	if username.lower() not in current_users:
		print("That username is available.")
	if username.lower() in current_users:
		print("That username is taken. Please enter a new username.")
