def student_data(info):
    match info:
        case {"data":{"subjects": [a,b,c],"name": name}}:
            print(f"Core subjects are: {a}, {b},{c} for student name: {name}")
        case _:
            print("invalid input")

student_data(
    {
        "data":{
            "subjects":["math", "History", "business"],
            "name":"emma"
              }
    }

)
