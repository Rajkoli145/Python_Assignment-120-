# Write a Python program that takes three numbers and prints the largest and the smallest numbers.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2 and num1 > num3:
    largest = num1
    smallest = num2 if num2 < num3 else num3
elif num2 > num1 and num2 > num3:
    largest = num2
    smallest = num1 if num1 < num3 else num3
else:
    largest = num3
    smallest = num1 if num1 < num2 else num2

print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")