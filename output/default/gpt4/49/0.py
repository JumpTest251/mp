import hashlib
import sqlite3

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def insert_user(username, password):
    hashed_password = hash_password(password)
    
    # Connect to the database (or create it)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Create users table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')
    
    try:
        # Insert the user into the database
        cursor.execute('''
            INSERT INTO users (username, password)
            VALUES (?, ?)''', (username, hashed_password))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    finally:
        conn.close()

def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    insert_user(username, password)

if __name__ == "__main__":
    main()