class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

class UserManager:
    def __init__(self):
        self.logged_in_user = None

    def login(self, email, password):
        # Simulating a login check
        if self.logged_in_user and self.logged_in_user.email == email and self.logged_in_user.password == password:
            return True
        return False

    def register(self, email, password):
        self.logged_in_user = User(email, password)

    def change_email(self, old_email, new_email, password, confirm_password):
        if not self.logged_in_user:
            return "You must be logged in to change your email."
        
        if self.logged_in_user.email != old_email:
            return "Old email does not match the logged-in user."
        
        if password != self.logged_in_user.password:
            return "Incorrect password."
        
        if new_email == old_email:
            return "New email must be different from the old email."
        
        if password == confirm_password:
            self.logged_in_user.email = new_email
            return "Email changed successfully."
        else:
            return "Passwords do not match."

# Simulation of usage
user_manager = UserManager()
user_manager.register("old_email@example.com", "securepassword123")

# Simulate user login
if user_manager.login("old_email@example.com", "securepassword123"):
    # Change email
    result = user_manager.change_email("old_email@example.com", "new_email@example.com", "securepassword123", "securepassword123")
    print(result)  # Should print: "Email changed successfully."
else:
    print("Login failed.")