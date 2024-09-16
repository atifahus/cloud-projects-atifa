# Create a program that checks if a user is an Adult or Minor based on their age using a conditional expression.

age=int(input("Enter your age"))

status= "Adult" if age >= 18 else "Minor"

print(status)