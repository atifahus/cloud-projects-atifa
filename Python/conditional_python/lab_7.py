# Using match with Data Structures

#1. Pattern Matching with Lists:

car=["bmw","audi","lexus"]
match car:
    case ["bmw","audi","lexus"]:
        print("match with car list")
    case [1,2,3]:
        print("match with number list")
    case _:
        print("doesn't match")

#2. Pattern Matching with Dictionaries:

menu={
    "entree": "steak",
    "dessert": "cake",
    "drink": "pepsi"
}
match menu:
    case{
        "entree": "steak",
        "dessert": "cake",
        "drink": "pepsi"
    }:
        print("This is a good menu")
    case _:
        print("show me other menu")