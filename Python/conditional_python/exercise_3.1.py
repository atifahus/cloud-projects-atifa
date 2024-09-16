# Write a program to check if a user is logged in and has a premium subscription. Print "Access Granted" if both conditions are true; otherwise, print "Access Denied".

user_logging=input("Did you logged in? ").strip().lower()=="yes"
subscription=input("Do you have a premium subscription? ").strip().lower()=="yes"

if user_logging and subscription:
    print("Access Granted")
else:
    print("Access Denied")