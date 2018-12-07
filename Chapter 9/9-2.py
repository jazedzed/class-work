class Restaurant():
	"""A simple attempt to model a restaurant."""
	def __init__(self, name, cuisine):
		"""Initialize name and cuisine attributes."""
		self.name = name
		self.cuisine = cuisine

	def describe_restaurant(self):
		"""Print a full description of the restaurant."""
		print(self.name.title() + " serves " + self.cuisine + " cuisine.")

	def open_restaurant(self):
		"""Simulate opening the restaurant."""
		print(self.name.title() + " is now open for business.")

my_restaurant = Restaurant('rocket to venus', 'vegan')
my_restaurant.describe_restaurant()
dj_restaurant = Restaurant('clark burger', 'Canadian')
dj_restaurant.describe_restaurant()
mom_restaurant = Restaurant('wicked sister', 'American')
mom_restaurant.describe_restaurant()