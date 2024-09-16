# Implement a program that uses pattern matching with guards to determine if a user’s role is Admin, Editor, or Viewer

def user_role(role):
    match role:
        case "admin" | "Admin":
            return "Role: Admin"
        case "editor" | "Editor":
            return "Role: Editor"
        case "viewer" | "Viewer":
            return "Role: Viewer"
        case _:
            return "Invalid Role"

print(user_role("admin"))
print(user_role(input("what is your role: ")))
