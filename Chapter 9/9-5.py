class User():
	"""A simple attempt to model a user."""

	def __init__(self, first_name, last_name, profession, location):
		"""Initialize attributes to describe a person."""
		self.first_name = first_name
		self.last_name = last_name
		self.profession = profession
		self.location = location
		self.login_attempts = 0

	def describe_user(self):
		"""Print a summary of the user's informaton."""
		print(self.first_name.title() + " " + self.last_name.title() + ", " + self.profession + " in " + self.location.title())

	def greet_user(self):
		"""Simulate greeting the user."""
		print("Hello, " + self.first_name.title() + " " + self.last_name.title() + ".")

	def increment_login_attempts(self):
		"""Add the given number to the number of logins."""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Reset the number of logins to 0."""
		self.login_attempts = 0

user_3 = User('paul', 'peeling', 'librarian', 'glenville, pa')
user_3.increment_login_attempts()
user_3.increment_login_attempts()
user_3.increment_login_attempts()
print("Login attempts: " + str(user_3.login_attempts))

user_3.reset_login_attempts()
print("Login attempts: " + str(user_3.login_attempts))