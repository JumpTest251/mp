import hashlib

def hash_password(password):
    # Create a new sha256 hash object
    sha256 = hashlib.sha256()
    # Update the hash object with the bytes of the password
    sha256.update(password.encode('utf-8'))
    # Return the hex representation of the digest
    return sha256.hexdigest()

def register_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    hashed_password = hash_password(password)
    
    print(f"Registration successful! Username: {username}, Hashed Password: {hashed_password}")

if __name__ == "__main__":
    register_user()