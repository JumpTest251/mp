import sqlite3
import os
import hashlib
import random
import string

def generate_salt(length=16):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def hash_password(password, salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()

def register_user(username, password):
    salt = generate_salt()
    hashed_password = hash_password(password, salt)

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT, salt TEXT)')
    
    try:
        cursor.execute('INSERT INTO users (username, password, salt) VALUES (?, ?, ?)', 
                       (username, hashed_password, salt))
        conn.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError:
        print("Username already exists. Please choose another one.")
    finally:
        cursor.close()
        conn.close()

def verify_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT password, salt FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()
    
    if result is None:
        print("Username not found.")
        return False
    
    hashed_password, salt = result
    if hashed_password == hash_password(password, salt):
        print("Login successful!")
        return True
    else:
        print("Invalid credentials.")
        return False
    finally:
        cursor.close()
        conn.close()

# Example Usage:
if __name__ == "__main__":
    while True:
        action = input("Do you want to register (r) or login (l)? ")
        if action.lower() == 'r':
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(username, password)
        elif action.lower() == 'l':
            username = input("Enter username: ")
            password = input("Enter password: ")
            verify_user(username, password)
        else:
            print("Invalid option, please choose 'r' for register or 'l' for login.")