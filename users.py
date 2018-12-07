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

class Privileges():
	"""Represent privileges of a user."""

	def __init__(self, privileges = ['can add post', 'can delete post', 'can ban user', 'can add user', 'can delete user']):
		"""Initialize the user's privileges."""
		self.privileges = privileges

	def show_privileges(self):
		"""Print a statement showing the admin's privileges."""
		print("This user has the following privileges: ")
		for privilege in self.privileges:
			print(privilege)

class Admin(User):
	"""Represent features of a user, specific to an administrator."""

	def __init__(self, first_name, last_name, profession, location):
		"""Initialize attributes of the parent class."""
		super().__init__(first_name, last_name, profession, location)
		self.privileges = Privileges()