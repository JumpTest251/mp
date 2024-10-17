import hashlib
import sqlite3

def hash_password(password):
    # Hashing the password using SHA-256
    return hashlib.sha256(password.encode()).hexdigest()

def insert_user(username, password):
    # Connect to the SQLite database or create it if it doesn't exist
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Create a table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (username TEXT PRIMARY KEY, 
                       password TEXT)''')
    
    # Hash the password
    hashed_password = hash_password(password)
    
    try:
        # Insert the new user into the database
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
                       (username, hashed_password))
        conn.commit()
        print("User successfully registered.")
    except sqlite3.IntegrityError:
        print("Error: Username already exists.")
    finally:
        # Close the connection
        conn.close()

def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    insert_user(username, password)

if __name__ == "__main__":
    main()