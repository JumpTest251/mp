class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

class LoginSystem:
    def __init__(self):
        self.users = {}
        self.logged_in_user = None

    def register(self, email, password):
        if email in self.users:
            print("Email already registered.")
            return False
        self.users[email] = User(email, password)
        print("Registration successful.")
        return True

    def login(self, email, password):
        user = self.users.get(email)
        if user and user.password == password:
            self.logged_in_user = user
            print("Login successful.")
            return True
        print("Invalid email or password.")
        return False

    def change_email(self, old_email, new_email, confirm_password):
        if not self.logged_in_user:
            print("You must be logged in to change your email.")
            return False
        if self.logged_in_user.email != old_email:
            print("Old email does not match.")
            return False
        if self.logged_in_user.password != confirm_password:
            print("Password confirmation failed.")
            return False
        if new_email in self.users:
            print("New email is already registered.")
            return False
        
        self.logged_in_user.email = new_email
        self.users[new_email] = self.users.pop(old_email)
        print("Email changed successfully.")
        return True

# Example usage
if __name__ == "__main__":
    system = LoginSystem()
    system.register("user@example.com", "password123")
    
    # Log in
    system.login("user@example.com", "password123")
    
    # Change email
    system.change_email("user@example.com", "new_user@example.com", "password123")