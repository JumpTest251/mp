class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password


class LoginPage:
    def __init__(self):
        self.users = {}
        self.logged_in_user = None

    def register(self, email, password):
        if email not in self.users:
            self.users[email] = User(email, password)
            print("User registered successfully.")
        else:
            print("Email already registered.")

    def login(self, email, password):
        if email in self.users and self.users[email].password == password:
            self.logged_in_user = self.users[email]
            print(f"User {email} logged in successfully.")
        else:
            print("Invalid email or password.")

    def change_email(self, old_email, new_email, confirm_password):
        if self.logged_in_user:
            if self.logged_in_user.email == old_email and self.logged_in_user.password == confirm_password:
                if new_email not in self.users:
                    self.users.pop(old_email)
                    self.logged_in_user.email = new_email
                    self.users[new_email] = self.logged_in_user
                    print("Email changed successfully.")
                else:
                    print("New email is already in use.")
            else:
                print("Old email or password is incorrect.")
        else:
            print("User must be logged in to change email.")


# Example Usage
login_page = LoginPage()
login_page.register("user@example.com", "password123")
login_page.login("user@example.com", "password123")
login_page.change_email("user@example.com", "newuser@example.com", "password123")