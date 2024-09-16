# Advanced Logical Operators

# Combining Multiple Logical Operators: or, and, not
temperature = 39
is_raining = False
is_snowing = False

if (temperature > 30 and is_raining) or is_snowing:
    print("let's go out")
elif (temperature > 30 and not is_raining) or not is_snowing:
    print("it is bad weather outside")
else:
    print("check the weather")

# 2. Using not for Negation:

is_weekend = False
is_holiday = True

if not is_weekend and is_holiday:
    print("enjoy your day")
else:
    print("it is a weekday")
