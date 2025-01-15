# Write a function that takes a string s and an integer n, and returns the string repeated n times.
def repeat_string(s, n):
    return (s+ " ")* n

s = input("Enter a string: ")
n = int(input("Enter a number: "))
print(repeat_string(s,n))



