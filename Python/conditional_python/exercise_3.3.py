# Create a program that determines if a user can access a restricted area based on their role and membership status.

role=input("what is your role?").strip().lower()
membership=input("Are you a member? ").strip().lower()=="yes"

allowed_role= ("admin", "dev", "manager")

if role in allowed_role and membership:
    print("Access Granted")
else:
    print("Access Denied")
