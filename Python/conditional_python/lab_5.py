# Nested Conditionals

# 1. Nested if Statements:
age=21
has_id=False

if age>= 18:
    if has_id:
        print("you can enter to the club")
    else:
        print("you don't have a valid id")

else:
    print("you are underage")

# 2. Combining Multiple Conditions:
temp= 55
is_raining= False

if temp > 40:
    if is_raining:
        print("we can't go out today")
    else:
        print("let's go for a walk")
else:
    print("it is too cold")
