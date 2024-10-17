class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.logged_in = False

    def login(self, password):
        if self.password == password:
            self.logged_in = True
            print("Login successful.")
        else:
            print("Login failed. Incorrect password.")

    def change_email(self, old_email, new_email, password):
        if not self.logged_in:
            print("You must be logged in to change your email.")
            return
        
        if old_email == self.email and password == self.password:
            self.email = new_email
            print("Email changed successfully.")
        else:
            print("Email change failed. Incorrect old email or password.")

# Example usage
user = User("john_doe", "john@example.com", "securepassword")

# Attempt to change email without logging in
user.change_email("john@example.com", "john_new@example.com", "securepassword")

# Logging in
user.login("securepassword")

# Attempt to change email with correct credentials
user.change_email("john@example.com", "john_new@example.com", "securepassword")

# Attempt to change email with incorrect old email
user.change_email("wrong_email@example.com", "john_new@example.com", "securepassword")

# Attempt to change email with incorrect password
user.change_email("john@example.com", "john_new@example.com", "wrongpassword")