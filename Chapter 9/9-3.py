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

user_1 = User('julianne', 'peeling', 'copy editor', 'baltimore, md')
user_2 = User('david', 'eden', 'actuary', 'baltimore, md')
user_3 = User('paul', 'peeling', 'librarian', 'glenville, pa')
user_4 = User('lisa', 'hughes', 'librarian', 'dunedin, fl')
user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()
user_4.describe_user()
user_4.greet_user()