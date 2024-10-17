import sqlite3
import bcrypt

def create_database():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    email TEXT)''')
    conn.commit()
    conn.close()

def register_user(username, password, first_name, last_name, email):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    
    # Check if username already exists
    c.execute('SELECT * FROM users WHERE username = ?', (username,))
    if c.fetchone():
        conn.close()
        return "Username already exists."

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insert new user into the database
    c.execute('INSERT INTO users (username, password, first_name, last_name, email) VALUES (?, ?, ?, ?, ?)',
              (username, hashed_password, first_name, last_name, email))
    conn.commit()
    conn.close()

    return "Registration succeeded."

# Example usage
if __name__ == "__main__":
    create_database()
    result = register_user('johndoe', 'password123', 'John', 'Doe', 'john@example.com')
    print(result)