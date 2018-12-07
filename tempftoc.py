temp_Fahrenheit = float(input("Enter the temperature in degrees Fahrenheit: "))
try:
	temp_Celsius = round(float((temp_Fahrenheit - 32) * 5/9),2)
	print("The temperature " + str(temp_Fahrenheit) + " degrees Fahrenheit is " + str(temp_Celsius) + " degrees Celsius.")
except:
	print("Please enter a number.")
(quit())