# Problem: Create a program that determines the shipping cost based on the weight of a package and whether it's express delivery.

weight=float(input("What is the weight"))
is_express=input("Is this express delivery? ").strip().lower()

if weight <= 5:
    if is_express == "yes":
        print("Your shipping cost is $20")
    else:
        print("Your shipping cost is $10")

else:
    if is_express == "yes":
        print("your shipping cost is $50")
    else:
        print("Your shipping cost is $30")