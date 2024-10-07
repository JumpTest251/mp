import sqlite3
import hashlib

# Connect to the SQLite database (or create it)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create users table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    first_name TEXT,
    last_name TEXT,
    email TEXT
)
''')

# Function to hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to register a new user
def register_user(username, password, first_name, last_name, email):
    # Check if the username already exists
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    if cursor.fetchone() is not None:
        return "Username already exists."
    
    # Hash the password
    hashed_password = hash_password(password)

    # Insert new user into the database
    cursor.execute('''
    INSERT INTO users (username, password, first_name, last_name, email)
    VALUES (?, ?, ?, ?, ?)
    ''', (username, hashed_password, first_name, last_name, email))
    
    # Commit changes
    conn.commit()

    return "Registration succeeded."

# Example usage
if __name__ == '__main__':
    username = input("Enter username: ")
    password = input("Enter password: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")

    message = register_user(username, password, first_name, last_name, email)
    print(message)

# Close the database connection
conn.close()