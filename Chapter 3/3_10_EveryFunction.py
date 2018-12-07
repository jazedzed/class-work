# the functions I need to cover here are 
# 1) accessing elements in a list with their indices
# 2) modifying elements in a list
# 3) adding elements to the end of a list with the append() method
# 4) inserting elements into a list with the insert() method
# 5) removing elements from a list with the del statement
# 6) removing elements from a list with the pop() method
# 7) removing elements from a list by value with the remove() method
# 8) sorting a list temporarily with the sorted() function and its reverse
# 9) printing a list in reverse order
# 10) sorting a list permanently with the sort() method and its reverse
# 11) finding the length of a list with the len() function
cats = ['katie', 'claudia', 'penny', 'allie', 'molly']
print(cats)
print(cats[0].title()) # accessing an element in the list by its index
cats[4] = 'rosie' # modifying an element in the list
print(cats)
cats.append('mary jane') # adding an element with the append() method
print(cats)
cats.insert(0, 'blue') # inserting an element with the insert() method
print(cats)
del cats[4] # deleting an element with the del statement
print(cats)
popped_cat = cats.pop() # removing an element with the pop() method
print(cats)
print(popped_cat.title())
cats.remove('claudia') # removing an element with the remove() method
print(cats)
cats.reverse() # reversing the original order of the list
print(cats)
print(sorted(cats)) # sorting the list temporarily with the sorted() function
print(sorted(cats, reverse = True)) # sorting the list temporarily with the sorted() function reversed
cats.sort() # sorting the list permanently with the sort() method
print(cats)
cats.sort(reverse = True) # sorting the list permanently in reverse
print(len(cats)) # finding the length of the list
