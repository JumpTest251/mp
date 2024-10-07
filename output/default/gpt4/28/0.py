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
        print("User registered successfully.")
        return True

    def login(self, email, password):
        user = self.users.get(email)
        if user and user.password == password:
            self.logged_in_user = user
            print("Login successful.")
            return True
        print("Invalid email or password.")
        return False

    def change_email(self, old_email, new_email, password):
        if self.logged_in_user and self.logged_in_user.email == old_email and self.logged_in_user.password == password:
            self.logged_in_user.email = new_email
            print("Email changed successfully.")
            return True
        print("Failed to change email: Incorrect old email or password.")
        return False

    def logout(self):
        if self.logged_in_user:
            print(f"User {self.logged_in_user.email} logged out.")
            self.logged_in_user = None
        else:
            print("No user is currently logged in.")

# Example usage:
if __name__ == "__main__":
    system = LoginSystem()
    system.register("test@example.com", "password123")
    
    if system.login("test@example.com", "password123"):
        system.change_email("test@example.com", "new_email@example.com", "password123")

    system.logout()