sandwich_orders = ['turkey', 'pastrami', 'chicken salad', 'pastrami', 'veggie', 'pastrami']
finished_sandwiches = []
print("Sorry, but the deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print("\nI made your " + current_sandwich + " sandwich.")
	finished_sandwiches.append(current_sandwich)
print("\nThe following sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich)