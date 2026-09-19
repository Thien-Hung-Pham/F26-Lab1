
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Thien Hung Pham
# Date: 18/9/2026
# Purpose: Use string methods and f-string formating.
# Usage: python3 lab1e.py

#TO-DO 1:
# Create a variable called "quantity".
# The value of "quantity" should be a decimal number of your own choice.
# Create another variable called "stock"
# The value of "stock" should also be a decimal number of your own choice.
# Print the product of `quantity` and `stock` with 4 spaces before the answer using the module % formatting.
# Then print the product of `quantity` and `stock` with 7 spaces before the answer and make sure the answer only goes to hundreadths (-.--) using the module % formatting.
quantity = 2.5
stock = 5.5
product = stock * quantity
# The %n indicate the width of the output. So to get the required output, I take the sum of spaces with the character length of product 
print("%13f" % product) # 4 (spaces) + 9 (length of product) = 13
print("%12.2f" % product) # 7 (spaces) + 5 (length of product) = 12