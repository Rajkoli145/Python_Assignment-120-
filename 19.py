# Write a Python program to find the sum of all natural numbers up to a given number n.

num = int (input("Enter a number: "))   
sum= 0
for i in range(1,num+1):
    sum = sum + i
print(f"The sum of all natural numbers up to {num} is {sum}")