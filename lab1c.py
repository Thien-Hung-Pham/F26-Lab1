
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date:
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1c.py

#TO-DO 1:
# import math module.
# Create a variable called 'radius' and take its value form user.
# Convert the variable to integer using int()
# use the contant pi form math module and compute the area of the circle using the variable 'radius'
import math

radius = int(input("Enter radius: "))
area = radius**2 * math.pi 

print("Area:", area)