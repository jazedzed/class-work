cities = {
	'seattle': {
		'country': 'united states',
		'population': '724,725',
		'fact': 'average of 37 inches of rain per year',
		},
	'paris': {
		'country': 'france',
		'population': '2.2 million',
		'fact': 'average of 25 inches of rain per year',
		},
	'london': {
		'country': 'england',
		'population': '8.7 million',
		'fact': 'average of 23 inches of rain per year',
		},
		}
for city, city_info in cities.items():
	print("\nCity: " + city.title())
	country = city_info['country']
	population = city_info['population']
	fact = city_info['fact']
	print("\tCountry: " + country.title())
	print("\tPopulation: " + population)
	print("\tFact: " + fact)