# Create a program that checks if a given number is within a specific range and is not divisible by a certain divisor.
def check_number(num, start, end, divisor):
    if  start < num < end and num%divisor !=0:
        print("number is between the range and not divisible by divisor")
    else:
        print("Invalid")
check_number(5,0,10,3)
check_number(12,0,10,3)
check_number(5,0,10,5)