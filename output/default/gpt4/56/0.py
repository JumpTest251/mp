class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

class LoginSystem:
    def __init__(self):
        self.logged_in_user = None

    def login(self, email, password):
        # Assuming we have a method to verify user credentials (e.g., from a database)
        if self.verify_credentials(email, password):
            self.logged_in_user = User(email, password)
            print("Login successful")
        else:
            print("Invalid email or password")

    def verify_credentials(self, email, password):
        # Here, we should have the logic to verify user's credentials. 
        # This is just a placeholder for demonstration.
        return True  # Assume success for this example

    def change_email(self, old_email, new_email, confirm_password):
        if not self.logged_in_user:
            print("You must be logged in to change your email.")
            return
        
        if self.logged_in_user.email != old_email:
            print("Old email does not match the logged-in account.")
            return
        
        if new_email == self.logged_in_user.email:
            print("New email must be different from old email.")
            return
        
        if confirm_password != self.logged_in_user.password:
            print("Incorrect password. Unable to change email.")
            return

        # Update the email
        self.logged_in_user.email = new_email
        print(f"Email changed successfully to {new_email}")

# Example Usage
login_system = LoginSystem()
login_system.login("user@example.com", "secure_password")

# Change email process
login_system.change_email("user@example.com", "new_user@example.com", "secure_password")