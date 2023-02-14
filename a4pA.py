# Write a program that deals with inflation, the rising cost of general goods
# over time.  Recall that the price of goods, such as a bag of Cheetos, goes up
# as time goes by. You will write a program to gauge the expected cost of an
# item in a specified number of years. The program asks for the cost of the
# item, the number of years, and the rate of inflation. The output is the
# estimated cost of the item after that number of years, using the given
# inflation rate.
#
# The user enters the inflation rate as a percentage, for example 4.5. You will
# have to convert the percentage to a fraction (0.045 in this example), and then
# use a loop to estimate the item's price adjusted for inflation. Note that this
# is similar to computing compound interest on a credit card account or a
# mortgage. Also note that you must check each of the values provided by the
# user to make sure that they are reasonable.  The original cost must be
# positive, and both the inflation rate and number of years should be
# non-negative.  You can assume that the original cost and inflation will be
# floats and the number of years will be an integer.  Finally, your program must
# print out the final cost with exactly two places after the decimal (for the
# cents).
#
# To adjust the price for inflation, you need to increase the price by the
# inflation rate each year. For example, if you have an item that is initially
# $10, with an inflation rate of 10%, the adjusted prices will be:
#
# After 1 year: $10.00 ∗ (1 + 0.10) = $11.00
# After 2 years: $11.00 ∗ (1 + 0.10) = $12.10
# After 3 years: $12.10 ∗ (1 + 0.10) = $13.31
# …
#
# In other words, to calculate the price after another year, you have to use the
# value from the current year, NOT the original price. You must use a loop to do
# this.
#
# Your input and output messages must conform to the following examples (note
# that $ in the original cost prompt is printed by the program, not typed by the
# user):
#
# Enter the original cost: $0
# Original cost must be positive!
#
# Enter the original cost: $10
# Enter the inflation rate (%): -0.1
# Inflation rate must be at least zero!
#
# Enter the original cost: $10
# Enter the inflation rate (%): 0
# Enter the number of years: -1
# Number of years must be at least zero!
#
# Enter the original cost: $10
# Enter the inflation rate (%): 10
# Enter the number of years: 3
# Final cost = $13.31
#
# Note the order of inputs, capitalization of messages, spacing, etc.

import sys

a = float(input("Enter the original cost: $"))
if a<=0:
    print("Original cost must be positive!")
    sys.exit()
    
b = float(input("Enter the inflation rate (%): "))
if b<0:
    print("Inflation rate must be at least zero!")
    sys.exit()

c = int(input("Enter the number of years: "))
if c<0:
    print("Number of years must be at least zero!")
    sys.exit()

while c>0:
    a = a * (1 + (b / 100))
    c -= 1
    
print(f"Final cost = {a:.2f}")
    




