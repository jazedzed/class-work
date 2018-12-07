from random import randint

class Die():
    """Represent a die."""

    def __init__(self, sides = 6):
        """Initialize the die."""
        self.sides = sides

    def roll_die(self):
        """Print a random number between 1 and the number of sides."""
        return randint(1, self.sides)

six_sided_die = Die()

results = []
for roll_num in range(10):
    result = six_sided_die.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

ten_sided_die = Die(sides = 10)

results = []
for roll_num in range(10):
    result = ten_sided_die.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

# Make a 20-sided die, and show the results of 10 rolls.
twenty_sided_die = Die(sides = 20)

results = []
for roll_num in range(10):
    result = twenty_sided_die.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)