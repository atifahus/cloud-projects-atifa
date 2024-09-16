# Write a program that uses match to process a list of different lengths and prints a corresponding message.
from Python.basic_python.basic_lab import length


def length_of_list(text):
    match text:
        case []:
            print("The list is empty")
        case [a]:
            print(f"The list has one item: {a}")
        case [a,b]:
            print(f"The list has two items: {a}, {b}")
        case [a,b,c]:
            print(f"The list has three items: {a}, {b}, {c} ")
        case _:
            print("The list has more than three items")

length_of_list(["apple"])
length_of_list(["fruits", 123])
length_of_list([1,4,7])
length_of_list(["light", "camera", "and", "action"])

