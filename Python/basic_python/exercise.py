"""
1.Write a Python program that prints the following:
"Welcome to Python Programming!"
"Python is fun!"
"""
from Python.basic_python.basic_lab import current_year, person

print("Welcome to Python Programming!")
print("Python is fun!")

# 2. Modify the program to print each line in uppercase letters.
print("Welcome to Python Programming!".upper())
print("Python is fun!".upper())

# 3. Write a Python program to display your name, age, and favorite hobby
name="Atifa"
age=30
hobby="travelling"
print(f"My name is {name}. I am {age} years old. My hobby is {hobby}.")

"""
4. Create a program that prints the following:
The current year
Your birth year
Your age
"""
current_year: 2024
birth_year=2017
age= current_year-birth_year
print("Age : ", age)

#5. Write a Python script that calculates the area of a rectangle. Add comments to explain each step.
#declare and initiating length and width
length=22
width=10
area=length*width
#printing the area of a rectangle
print("The area of a rectangle is: ", area)

"""
7. Write a Python program that calculates and prints the result of the following:
    8 multiplied by 7
    15 divided by 3
    The remainder when 22 is divided by 7
"""
print(8*7)
print(15/3)
print(22%7)

# 8. Modify the program to calculate the square of a number and the cube of another number.
n=7
print("The square of n is: ",n**2)
print("The cube of n is: ", n**3)

# 9. Create a variable to store the number of apples you have and another to store the number of oranges.
# Print the total number of fruits.
apple=6
orange=15
total_fruits=apple+orange
print("Total numbers of fruits: ", total_fruits)

# 11. Assign the value 100 to a variable x. Reassign x to 50 and print both values.
x=100
print("Assigning the value of x: ",x)
x=50
print("Reassigning the value of x: ",x)

# 12. Assign values to three variables: a, b, and c.
# Swap the values between a and b, and then between b and c. Print the final values of a, b, and c.
a="apple"
b="banana"
c="cherry"

a,b=b,a
print("swap between a and b".upper())
print("a= ",a)
print("b= ",b)

b,c=c,b
print("swap between b and c".upper())
print("b= ",b)
print("c= ",c)

print("final value".upper(), "a= ", a," b= ", b, " c= ",c)

# 15. Create variables to store a person's name, age, and whether they are a student.
# Print a sentence describing this person using these variables.
p_name="Sam"
p_age=18
if_student=True
print("{} is {} years old. Student?: {}".format(p_name,p_age,if_student))

# 16. Define variables for a product's name, price, and stock availability (True or False).
# Print these details in a formatted sentence.
product="Laptop"
price=1280.00
in_stock=True
print(f"The product is {product} in a price of {price} in stock = {in_stock} ")


"""# 18. Write a program that asks the user for their favorite word and then prints it repeated 10 times.
word=input("What is your favorite word?")
print(word * 10)"""