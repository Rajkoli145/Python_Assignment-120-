# Write a program that calculates the factorial of a given positive integer using a for loop.
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
print(f"The factorial of {num} is {factorial}")