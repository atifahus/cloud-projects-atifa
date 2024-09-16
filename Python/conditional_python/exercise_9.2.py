# Create a program that processes different types of input strings and applies guards to handle special cases.

def types_of_string(s):
    match s:
        case s if s.isdigit():
            print("String is numeric")
        case s if s.isalpha():
            print("String is alphabetic ")
        case s if len(s) > 10:
            print("string length is too long")
        case _:
            print("Invalid String")

types_of_string("1212")
types_of_string("apple")
types_of_string("123456789asfff")

