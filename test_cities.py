import unittest
from city_functions import location

class CityCountryTestCase(unittest.TestCase):
	"""Tests for 'city_functions.py'."""

	def test_location(self):
		"""Do locations like 'London, England' work?"""
		formatted_location = location('london', 'england')
		self.assertEqual(formatted_location, 'London, England')

	def test_location_demographics(self):
		"""Do locations with populations like 'London, England, population: 8.7 million' work?"""
		formatted_location = location(
			'london', 'england', '8.7 million')
		self.assertEqual(formatted_location, 'London, England, population: 8.7 million')

unittest.main()