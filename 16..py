# Write a program to display the multiplication table of a given integer up to 10.

num = int(input("Enter a number: "))
for i in range(1,11):
    print(num, "x", i, "=", num*i)
