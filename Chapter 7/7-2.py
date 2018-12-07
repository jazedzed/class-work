guests = input("How many people are in your dinner group this evening? ")
guests = int(guests)
if guests > 8:
	print("I'm sorry, but you'll have to wait for a table.")
else:
	print("Your table is ready.")