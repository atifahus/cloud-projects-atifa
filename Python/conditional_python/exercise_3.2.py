#  Implement a program to check if a user is on vacation or it's a weekend. Print "Vacation Time!" if either condition is true

in_vacation=input("Are you in vacation? (yes/no) ").strip().lower()=="yes"
is_weekend=input("Is it a weekend? (yes/no) ").strip().lower()=="yes"

if in_vacation or is_weekend:
    print("Vacation Time!")
else:
    print("Keep working")