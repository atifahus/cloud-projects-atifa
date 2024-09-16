"""
Exercise 2: Categorize Numbers
Objective: Create a program to categorize numbers into Positive, Negative, or Zero using pattern matching.

Instructions:

Create a program that uses the match statement to categorize a number.
Print "The number is positive" for positive numbers.
Print "The number is negative" for negative numbers.
Print "The number is zero" for zero.
"""

number=float(input("Enter a number: "))

if number > 0:
    print(f"{number} is a positive number")
elif number < 0:
    print(f"{number} is a negative number")
else:
    print(f"{number} is zero")
