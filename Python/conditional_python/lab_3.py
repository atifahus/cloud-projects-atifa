# Boolean Values
#1. logging in
is_log_in=True
if is_log_in:
    print("Welcome! You are successfully logged in")
else:
    print("Try again.")

# 2. Combining Boolean Expressions: using "and"
is_member=True
has_coupon=False
if is_member and has_coupon:
    print("Discount applied")
else:
    print("No discount")