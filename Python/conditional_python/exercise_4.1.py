"""
Exercise 1: Day of the Week
Objective: Write a program that matches a day of the week and prints a message indicating whether it is a weekend or a weekday.

Instructions:

Create a program that uses the match statement to categorize days of the week.
Print "It's the weekend!" for Saturday and Sunday.
Print "It's a weekday!" for Monday through Friday.
"""

day=input("Which day is today? ").strip().lower()

match day:
    case "monday" | "tuesday" | "wednesday"| "thrusday" | "friday":
        print(" It's a weekday")
    case "saturday" | "sunday":
        print("It's weekend")
    case _:
        print("Invalid Input")