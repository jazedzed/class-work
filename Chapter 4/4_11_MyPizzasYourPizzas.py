pizzas = ['margherita', 'mushroom', 'spinach']
friend_pizzas = pizzas[:]
pizzas.append('white')
friend_pizzas.append('pepperoni')
print("My favorite pizzas are: " )
for pizza in pizzas:
	print(pizza)
print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas:
	print(pizza)