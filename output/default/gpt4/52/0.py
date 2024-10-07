import os
import hashlib
import sqlite3

# Function to hash password with a salt
def hash_password(password):
    # Generate a random 16-byte salt
    salt = os.urandom(16)
    # Hash the password along with the salt
    pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    # Return the salt and the hashed password, both in hex format
    return salt.hex() + pwd_hash.hex()

# Function to create a registration database if it doesn't exist
def create_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Create a table for user registration
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Function to register a user
def register_user(username, password):
    password_hash = hash_password(password)

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
        conn.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    finally:
        conn.close()

# Create database and table
create_database()

# Example registration
if __name__ == '__main__':
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    register_user(user, pwd)