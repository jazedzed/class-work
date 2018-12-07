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