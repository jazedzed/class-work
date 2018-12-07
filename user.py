class User():
	"""A simple attempt to model a user."""

	def __init__(self, first_name, last_name, profession, location):
		"""Initialize attributes to describe a person."""
		self.first_name = first_name
		self.last_name = last_name
		self.profession = profession
		self.location = location

	def describe_user(self):
		"""Print a summary of the user's informaton."""
		print(self.first_name.title() + " " + self.last_name.title() + ", " + self.profession + " in " + self.location.title())


	def greet_user(self):
		"""Simulate greeting the user."""
		print("Hello, " + self.first_name.title() + " " + self.last_name.title() + ".")