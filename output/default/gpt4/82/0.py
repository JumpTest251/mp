import os
import hashlib
import sqlite3

def generate_salt(length=16):
    """Generate a random salt for hashing."""
    return os.urandom(length)

def hash_password(password, salt):
    """Hash the password with the given salt."""
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)

def store_user(username, password):
    """Store the username and hashed password in the database."""
    salt = generate_salt()
    hashed_password = hash_password(password, salt)
    
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password BLOB NOT NULL,
            salt BLOB NOT NULL
        )
    ''')
    
    # Insert the new user record
    cursor.execute('''
        INSERT INTO users (username, password, salt)
        VALUES (?, ?, ?)
    ''', (username, hashed_password, salt))
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Example usage
if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")
    store_user(username, password)
    print("User registered successfully!")