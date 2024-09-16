student_info = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": True,
    "courses": [
        {"course_name": "DevOps",
         "start_date": "Sep 10, 2024"
         },
        {"course_name": "DataAnalytics",
         "start_date": "Nov 20, 2024"
         }
    ]
}


alice_courses = student_info["courses"]



# To do Small Problem
# Find out the start_date value of DevOps course for Alice from student_info dictionary ,
# your code should also ensure there is DevOps Course.


course= alice_courses[0]
start_date=course["start_date"]

if course : "DevOps"
print("The start date for Devops course is : "+ start_date)



#In one line. Trying with data analytics example
data_course = student_info["courses"][1]["start_date"]

if course : "DataAnalytics"
print("The start date for Data Analytics course is : "+ data_course)


