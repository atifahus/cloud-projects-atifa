# Implement a program to evaluate whether a user can access premium content based on their subscription status and current promotions.
def user_access(subscription_status,promotion):
    if subscription_status=="premium" and promotion:
        print("You have access")
    else:
        print("you do not have access")

user_access("premium", True)
user_access("basic", True)
user_access("Premium", False)