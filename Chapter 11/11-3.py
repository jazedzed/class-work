class Employee():
    """Represent an employee."""

    def __init__(self, first_name, last_name, salary):
        """Initialize the employee."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.salary = salary

    def give_raise(self, amount = 5000):
        """Give the employee a raise."""
        self.salary += amount

import unittest

class TestEmployee(unittest.TestCase):
    """Create test cases for the employee."""

    def setUp(self):
        """Create an employee."""
        self.julianne = Employee('julianne', 'peeling', 20000)

    def test_give_default_raise(self):
        """Test that a default raise works correctly."""
        self.julianne.give_raise()
        self.assertEqual(self.julianne.salary, 25000)

    def test_give_custom_raise(self):
        """Test that a custom raise works correctly."""
        self.julianne.give_raise(10000)
        self.assertEqual(self.julianne.salary, 30000)

unittest.main()