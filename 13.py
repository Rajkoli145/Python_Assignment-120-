# Write a Python program to convert a temperature from Celsius to Fahrenheit and vice versa.
# celsius to fahrenheit = (celsius * 9/5) + 32
# fahrenheit to celsius = (fahrenheit - 32) * 5/9
celsius = float(input("Enter the temperature in celcius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")
fahrenheit = float(input("Enter the temperature in fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F is equal to {celsius}°C")