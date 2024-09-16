"""
Problem: Write a program that checks if a user is eligible for a loan based on their credit score and income. The user must have a high credit score and sufficient income.
"""


credit_score=int(input("Enter your credit score: "))
annual_income=float(input("Enter your annual income: "))

if credit_score > 700:
    if annual_income > 90000:
        print("You are eligible for loan")
    else:
        print("You are not eligible due to low income")
else:
    print("You are not eligible due to low credit score")
