class Restaurant():
	"""A simple attempt to model a restaurant."""
	def __init__(self, name, cuisine):
		"""Initialize name and cuisine attributes."""
		self.name = name
		self.cuisine = cuisine

	def describe_restaurant(self):
		"""Print a full description of the restaurant."""
		print(self.name.title() + " serves " + self.cuisine + ".")

	def open_restaurant(self):
		"""Simulate opening the restaurant."""
		print(self.name.title() + " is now open for business.")

class IceCreamStand(Restaurant):
	"""Represent aspects of a restaurant, specific to an ice cream stand."""

	def __init__(self, name, cuisine):
		"""Initialize attributes of the parent class."""
		super().__init__(name, cuisine)
		self.flavors = ['vanilla', 'chocolate', 'strawberry']

	def list_flavors(self):
		"""Print a statement listing the flavors the ice cream stand sells."""
		print(self.name.title() + " serves the following flavors: ")
		for flavor in self.flavors:
			print(flavor)

petit_louis_stand = IceCreamStand('petit louis pints', 'desserts')
petit_louis_stand.list_flavors()