# Write a program that categorizes a number as Low, Medium, or High using pattern matching with guards.
def categorize_number(number):
    match number:
        case a if 0 < number < 25:
            print("LOW")
        case b if 25 < number < 50:
            print( "MEDIUM")
        case _:
            print("HIGH")

categorize_number(23)
categorize_number(44)
categorize_number(56)