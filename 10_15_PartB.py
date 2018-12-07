instruments = ['guitar', 'piano', 'drums', 'bass']
print(instruments)
prompt = "What other instrument should we add to our band? "
instrument = input(prompt)
instruments.append(instrument)
print(instruments)
prompt = "Let's add one more instrument to our sound. What should it be? "
instrument = input(prompt)
instruments.append(instrument)
print("Here's our lineup:")
for instrument in instruments:
	print(instrument)