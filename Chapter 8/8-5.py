def describe_city(city, country = 'germany'):
	"""Display info about a city and country."""
	print("\n" + city.title() + " is in " + country.title() + ".")
describe_city(city = 'berlin')
describe_city(city = 'frankfurt')
describe_city(city = 'dublin')