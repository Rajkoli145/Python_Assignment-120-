# Write a Python function that takes a string and returns its length without using the built-in len() function.
str = input("Enter a string: ")
length = 0
for i in str:
    length += 1
print(f"Length of the string: {length}")  