# Write a Python program that calculates simple interest. Prompt for principal, rate, and time, then compute the interest.
# simle interest = (p*r*t)/100
p=float(input("Enter the principal amount: "))
r=float(input("Enter the rate of interest: "))
t=float(input("Enter the time period: "))
simple_interest=(p*r*t)/100
print(f"The simple interest is: {simple_interest}")
