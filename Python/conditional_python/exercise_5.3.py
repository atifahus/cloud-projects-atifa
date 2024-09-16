#  Implement a program that evaluates if a student qualifies for a scholarship based on their GPA and extracurricular activities.
gpa=float(input("Enter your GPA: "))
extracurricular=input("Have you done any extracurricular activities? (yes/no)").strip().lower()

if gpa > 3.2:
    if extracurricular == "yes":
        print("Congrats! You are eligible for scholarship")
    else:
        print("Sorry. you do not qualify due to lack of extracurricular activities")
else:
    print("Sorry. You do not qualify due to less GPA")