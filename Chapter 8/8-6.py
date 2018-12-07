def get_city_names(city, country):
	"""Return a city and its country."""
	city_country = city + ", " + country
	return city_country.title()
destination = get_city_names('berlin', 'germany')
print(destination)
destination = get_city_names('london', 'england')
print(destination)
destination = get_city_names('dublin', 'ireland')
print(destination)