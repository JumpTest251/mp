import sqlite3

def check_username_exists(username):
    # Connect to the database (replace 'your_database.db' with your database file)
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()
    
    # Execute a query to check if the username exists
    cursor.execute("SELECT EXISTS(SELECT 1 FROM users WHERE username = ?)", (username,))
    exists = cursor.fetchone()[0]

    # Close the connection
    cursor.close()
    conn.close()

    return bool(exists)

# Example usage
username_to_check = 'test_user'
if check_username_exists(username_to_check):
    print("Username exists.")
else:
    print("Username does not exist.")