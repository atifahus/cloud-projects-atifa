# Problem 1: Print Your Own Message
print("Name : Anna")
print("Age : 30")
print("Hobby : Cooking")

# Problem 2: Personalized Greeting

"""
name= input("what is your name?")
print(name)
"""

# Problem 3: Comment Your Code
# it will print the table of 3
for i in range(1,6):
    print(i*3)

# Problem 4: Basic Arithmetic Operations
print("Addition: ", 3+5)
print("Subtraction: ", 10-7)
print("Multiplication: ",2*6)
print("Division: ", 100/25)
print("Exponentation: ", 3**3)


# Problem 5: Store Your Birth Year
age=7
current_year=2024
print("Birth year: ", current_year-age)

# Problem 6: Calculating the Area of a Rectangle
length= 12
width= 5.5
area=length * width
print("the area is : ", area)


# Problem 7: Data Types Identification
food ="Pizza"
price= 3.99
quantity=2
available=True
print(type(food))
print(type(price))
print(type(quantity))
print(type(available))


# Problem 8: Swap Two Variables
a= 10
b=30
print("Before: " , "a= ",a, " b= ", b)
a,b=b,a
print("After: ", "a= ",a, " b= ", b)

"""# Problem 9: Simple Interest Calculator
principle=float(input("Enter principle: "))
rate=float(input("Enter rate: "))
time=int(input("Enter the time in years: "))
interest=(principle*rate*time)/100
print("Interest is : ", interest)"""

# Problem 10: Data Type Conversion
# converts an integer to a string, a float to an integer, and a string to a float, then prints the results.
int_num=10
print("Before: ",type(int_num))
int_str=str(int_num)
print("After: ",type(int_str))

fl_num=29.56
print("Before: ",type(fl_num))
fl_int=int(fl_num)
print("After: ", type(fl_int))

str_a="99"
print("Before: ", type(str_a))
str_fl=float(str_a)
print("After: ", type(str_fl))
print(str_fl)

# Problem 11: Concatenating Strings
f_name="mr."
l_name="python"
full_name=f_name+ " " + l_name
print("my name is ",full_name)

# Problem 12: List Operations
num=[12,44,62,11]
num.append(4)
print(num)

#Problem 13: Accessing List Elements
fruit=["apple","banana","strawberry","kiwi","mango"]
print(fruit[0])
print(fruit[-1])

# Problem 14: Dictionary Basics
person={
    "name":"Jess",
    "age":"24",
    "city":"Paris"
}
print("Name: ",person["name"])
print("Age: ", person["age"])
print("City: ",person["city"])

# Problem 15: Adding to a Dictionary
person["email"]="jessinparis@fun.com"
print(person)

# Problem 16: Basic String Operations
# converts a string to uppercase, lowercase, and calculates its length.
line= "i am jess from paris"
print(line.upper())
print(line.lower())
print(len(line))

# Problem 17: List Slicing
# print the first three elements of a list and the last two elements.
my_list=[1,2,3,4,"apple","mango","white","red"]
print(my_list[:3])
print(my_list[-2:])

# Problem 18: String Formatting
# format a string using the format() method or f-strings.

# format() method
name="Emily"
city="Paris"
print("My name is {} and I live in {}".format(name,city))

# f-strings

print(f"I am {name} from {city}")

# Problem 19: Calculating the Perimeter of a Circle
import math
radius=3.44
perimeter = 2 * math.pi * radius
print(perimeter)

# Problem 20: Boolean Operations
a=10
b=22
c=5
print("a>b", a>b)
print("c<b",c<b)
print("a>=c",a>=c)
print("a<=b", a<=b)
print("b==c",b==c)
print("b!=c",b!=c)

