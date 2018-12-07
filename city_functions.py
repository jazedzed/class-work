def location(city, country, population = ''):
	"""Return a neatly formatted city and country."""
	if population:
		info = city.title() + ", " + country.title() + ", population: " + population
	else:
		info = city.title() + ", " + country.title()
	return(info)