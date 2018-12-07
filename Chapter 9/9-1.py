class Restaurant():
	"""A simple attempt to model a restaurant."""
	def __init__(self, name, cuisine):
		"""Initialize name and cuisine attributes."""
		self.name = name
		self.cuisine = cuisine

	def describe_restaurant(self):
		"""Print a full description of the restaurant."""
		print(self.name.title() + " serves " + self.cuisine.title() + " cuisine.")

	def open_restaurant(self):
		"""Simulate opening the restaurant."""
		print(self.name.title() + " is now open for business.")

my_restaurant = Restaurant('rocket to venus', 'vegan')
print("One of my favorite restaurants, " + my_restaurant.name.title() + ", serves " + my_restaurant.cuisine + " cuisine.")