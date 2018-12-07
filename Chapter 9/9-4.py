class Restaurant():
	"""A simple attempt to model a restaurant."""

	def __init__(self, name, cuisine):
		"""Initialize name and cuisine attributes."""
		self.name = name
		self.cuisine = cuisine
		self.number_served = 0

	def describe_restaurant(self):
		"""Print a full description of the restaurant."""
		print(self.name.title() + " serves " + self.cuisine.title() + " cuisine.")

	def open_restaurant(self):
		"""Simulate opening the restaurant."""
		print(self.name.title() + " is now open for business.")

	def count_number_served(self):
		"""Simulate counting the number of customers served."""
		print(self.name.title() + " has served " + str(self.number_served) + " customers.")

	def set_number_served(self, customers):
		"""Set the number of customers served to the given value."""
		self.number_served = customers

	def increment_number_served(self, customers):
		"""Add the given number to the customers served."""
		self.number_served += customers

restaurant = Restaurant('alglio e olio', 'Mediterranean')
restaurant.set_number_served(47)
restaurant.count_number_served()
restaurant.increment_number_served(52)
restaurant.count_number_served()