# Logical Operators with or, and, and bool
from Python.conditional_python.lab_8 import is_snowing

# 1. Write a program that determines if a person should stay at home or go outside based on the weather.
# The conditions are: temperature > 20, not raining, and not snowing.
weather=int(input("What is the temperature?"))
is_raining=input("Is it raining?").strip().lower() == "yes"
is_snowing=input("is it snowing?").strip().lower() == "yes"

if weather > 20 and not is_raining  and not is_snowing:
    print("You can go outside")
else:
    print("You should stay at home")


#2. Problem: Implement a program to check if a student has passed an exam.
# The student passes if their score is at least 50 or if they have a teacher’s recommendation.

score=int(input("Enter your score:"))
recommendation= input("Do you have teacher's recommendation: ").strip().lower()=="yes"

if score >=50 or recommendation:
    print("Passed")
else:
    print("Failed")

# 3. Create a program that checks if a person is eligible for a discount.
# The criteria are: being a member or having a coupon.
is_mem= input("are you a member? ").strip().lower()=="yes"
has_coupon=input("do you have any coupon? ").strip().lower()=="yes"
if is_mem or has_coupon:
    print("Discount applied")
else:
    print("No discount")
