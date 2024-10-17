import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed_password = hash_password(password)
    
    # Store the username and hashed password (Here it is just printed)
    print(f"Username: {username}")
    print(f"Hashed Password: {hashed_password}")

if __name__ == "__main__":
    register_user()