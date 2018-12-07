def build_car(manufacturer, model, **features):
	"""Build a dictionary containing all info about a car."""
	description = {}
	description['manufacturer'] = manufacturer
	description['model'] = model
	for key, value in features.items():
		description[key] = value
	return description
car_description = build_car('subaru', 'outback', color = 'green', automatic = True)
print(car_description)