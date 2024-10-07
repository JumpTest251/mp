import hashlib
import os
import sqlite3

def hash_password(password: str, salt: bytes) -> str:
    """Hashes a password with a given salt."""
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000).hex()

def create_user(username: str, password: str):
    """Creates a new user with a hashed password and stores it in the database."""
    # Generate a random salt
    salt = os.urandom(16)

    # Hash the password
    hashed_password = hash_password(password, salt)

    # Connect to the database (or create it if it doesn't exist)
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password_hash TEXT,
            salt BLOB
        )
    ''')

    try:
        # Insert the new user into the database
        cursor.execute('''
            INSERT INTO users (username, password_hash, salt)
            VALUES (?, ?, ?)
        ''', (username, hashed_password, salt))

        # Commit the changes
        connection.commit()
        print("User created successfully.")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    finally:
        # Close the database connection
        connection.close()

# Get user input
if __name__ == "__main__":
    user = input("Enter username: ")
    pw = input("Enter password: ")
    create_user(user, pw)