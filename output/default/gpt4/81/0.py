import hashlib
import os
import sqlite3

# Database setup
def create_database():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to hash password with salt
def hash_password(password):
    salt = os.urandom(16)  # Generate a random salt
    salt_hex = salt.hex()  # Convert salt to hexadecimal string
    hash_obj = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    hash_hex = hash_obj.hex()  # Convert hash to hexadecimal string
    return f"{salt_hex}${hash_hex}"  # Store both salt and hash

# Register user
def register_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    hashed_password = hash_password(password)
    
    try:
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    finally:
        conn.close()

# Verify password
def verify_password(stored_password, provided_password):
    salt_hex, hash_hex = stored_password.split('$')
    salt = bytes.fromhex(salt_hex)
    hash_obj = hashlib.pbkdf2_hmac('sha256', provided_password.encode(), salt, 100000)
    return hash_obj.hex() == hash_hex

# Login user
def login_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT password FROM users WHERE username = ?', (username,))
    result = c.fetchone()
    
    if result:
        stored_password = result[0]
        if verify_password(stored_password, password):
            print("Login successful.")
        else:
            print("Invalid password.")
    else:
        print("Username not found.")
    
    conn.close()

# Main execution flow
if __name__ == "__main__":
    create_database()
    while True:
        action = input("Do you want to register or login? (reg/login): ").strip().lower()
        if action == 'reg':
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(username, password)
        elif action == 'login':
            username = input("Enter username: ")
            password = input("Enter password: ")
            login_user(username, password)
        else:
            print("Please enter 'reg' or 'login'.")