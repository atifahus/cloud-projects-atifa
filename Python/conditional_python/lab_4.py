# Pattern Matching with match
# 1. Basic match Statement:

day= "monday"

match day:
    case "monday" | "tuesday" | "wednesday":
        print("it is workday")
    case "friday":
        print("it is almost weekend")
    case _:
        print("have a good day")


# 2. Pattern Matching with Patterns:
num=9
match num:
    case 1 | 2 | 3:
        print("low number")
    case 4 | 5 | 6:
        print("mid number")
    case _:
        print("high number")