# Write a Python program to calculate compound interest given principal, rate, and time in years.
# A = P(1 + r/n)^(nt)

p=float(input("Enter the principal amount: "))
r=float(input("Enter the rate of interest: "))
t=float(input("Enter the time period: "))
n=float(input("Enter the number of times that interest is compounded per year: "))
compound_interest=p*(1+r/n)**(n*t)
print(f"The compound interest is: {compound_interest}")