# Create a program that matches and extracts values from a dictionary, then prints the values.

def information_dict(info):
    match info:
        case {"name": name, "age": age}:
            print(f"Name: {name} ; Age: {age}")
        case {"name": name}:
            print(f"Name: {name} ; Age is unknown ")
        case {"age": age}:
            print(f"Age: {age} ; Name is unknown")
        case _:
            print("Information is missing")

information_dict({"name": "sam", "age": "23"})
information_dict({"name": "bella"})
information_dict({"age": "31"})
information_dict({})
