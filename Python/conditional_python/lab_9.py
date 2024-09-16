# Matching with Patterns and Guards

# 1. Pattern Matching with Guards:
num= 401
match num:
    case a if num%2==0:
        print("{} is even number".format(a))
    case b if num%2 != 0:
        print(f"{b} is odd number")
    case _:
        print("invalid number")

# 2. Matching with Multiple Conditions:

msg= "error"
match msg:
    case "error" | "alart":
        print("try again")
    case "success":
        print("you are successful")
    case _:
        print("invalid")
