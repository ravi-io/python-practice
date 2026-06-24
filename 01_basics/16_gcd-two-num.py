import math

# The Greatest Common Divisor (GCD)—also known as the 
# Greatest Common Factor (GCF) or Highest Common Factor (HCF)—is 
# the largest positive integer that divides both numbers evenly without leaving a remainder

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"GCD of {a} and {b} is: {math.gcd(a, b)}")