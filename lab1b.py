# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 18/9/2026
# Purpose: Use arithmetic in python.
# Usage: python3 lab1b.py

# TO-DO 1:
#	Create a variable called "num1", take its value from user.
#	Create another variable called "num2" and take its value from user. 
# Convert the values to integers using int() function

num1 = input("Enter num1: ")
num2 = input("Enter num2: ")

print(type(num1))
print(type(num2))

num1= int(num1)
num2= int(num2)

# TO-DO 2:
# Perform all arithmetic oeprations as outlined in the description in README.md file, and print in the required format.
sum = num1 + num2 
diff = num1 - num2 
product = num1 * num2 
exponent = num1 ** num2
quotient = num1 / num2
floor = num1 // num2
mod = num1 % num2

print("num1 + num2 =", sum)
print("num1 - num2 =", diff)
print("num1 * num2 =", product)
print("num1 ** num2 =", exponent)
print("num1 / num2 =", quotient)
print("num1 // num2 =", floor)
print("num1 % num2 =", mod)