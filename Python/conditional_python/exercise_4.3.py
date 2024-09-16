"""
Exercise 3: Type of Input
Objective: Implement a program that matches and prints messages based on the type of input: string, list, or dictionary.

Instructions:

Create a program that uses the match statement to determine the type of input.
Print "This is a string" for string inputs.
Print "This is a list" for list inputs.
Print "This is a dictionary" for dictionary inputs.
Print "Unknown type" for any other type of input.
"""

def type_of_input(value):
    match value:
        case str():
            print("This is a String")
        case list():
            print("This is a list")
        case dict():
            print("This is a dictionary")
        case _:
            print("Unknown type")

type_of_input("Apple")

type_of_input(["fruits", "vegetable","drinks"])

type_of_input({
    "Mango": 12,
    "Banana": 3

}
)
type_of_input(123)
