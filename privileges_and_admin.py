from user import User

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