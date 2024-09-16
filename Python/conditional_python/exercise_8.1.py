# Write a program that determines if a person can attend an event based on
# multiple conditions: weekend, holiday, or special invitation.
def event(weekend, holiday, special_invitation ):
    if weekend or holiday or special_invitation:
        print("You are attend the event")
    else:
        print("you can't attend the event")

event(True, False,False)
event(True,True,True)
event(False,False,False)