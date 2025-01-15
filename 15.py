# Write a Python program to round a float to 2 decimal places without using the built-in round() function.
num=float (input("Enter a number: "))
rounded_number = int(num * 100 + 0.5) / 100
print(rounded_number)