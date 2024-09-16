# Basic Conditionals with if, elif, and else

# 1.  Write a program that checks if a number is positive, negative, or zero. Print an appropriate message for each case.
num=int(input("Enter a number"))
if num > 0:
    print(f"{num} is a positive number")
elif num < 0:
    print(f"{num} is a negative number")
else:
    print(f"{num} is zero")

# 2. Create a program that determines the type of a day based on a given temperature: Freezing, Cold, Mild, or Hot.
temp= int(input("What is the temperature today: "))
if temp < 0:
    print("It is freezing")
elif temp > 0 and  temp < 50:
    print("It is cold")
elif temp > 50 and temp < 80:
    print("It is mild")
else:
    print("It is hot")

# 3. Implement a program that checks if a person is eligible to vote based on their age.
# If they are 18 or older, print "Eligible to vote"; otherwise, print "Not eligible to vote".

age=int(input("Enter your age:"))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")