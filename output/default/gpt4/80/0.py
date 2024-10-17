import sqlite3
import os
import hashlib

# Function to create a salted hash
def hash_password(password):
    salt = os.urandom(16)  # Generate a random 16-byte salt
    salted_password = salt + password.encode()
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    return salt.hex(), hashed_password

# Function to insert user into the database
def insert_user(username, password):
    salt, hashed_password = hash_password(password)
    
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Create users table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (username TEXT PRIMARY KEY, salt TEXT, hashed_password TEXT)''')
    
    # Insert username and hashed password into the database
    try:
        cursor.execute('INSERT INTO users (username, salt, hashed_password) VALUES (?, ?, ?)',
                       (username, salt, hashed_password))
        conn.commit()
        print("User successfully registered.")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    
    # Close the database connection
    cursor.close()
    conn.close()

# Main execution
if __name__ == "__main__":
    user = input("Enter username: ")
    pwd = input("Enter password: ")
    
    insert_user(user, pwd)