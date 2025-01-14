# Write a Python program that asks the user to input a float number, then prints the integer part (truncate), and the fraction part separately.
num = float(input("Enter a float number: "))
print(f"Integer part: {int(num)}")
print(f"Fraction part: {num - int(num):.4f}")
