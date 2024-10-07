import sqlite3

def check_username_exists(username):
    # Connect to the database (replace 'your_database.db' with your database file)
    connection = sqlite3.connect('your_database.db')
    cursor = connection.cursor()

    # Execute a query to check if the username exists
    cursor.execute("SELECT EXISTS(SELECT 1 FROM users WHERE username=?)", (username,))
    exists = cursor.fetchone()[0]

    # Close the database connection
    connection.close()

    return bool(exists)

# Example usage
username_to_check = 'exampleUser'
if check_username_exists(username_to_check):
    print("Username exists.")
else:
    print("Username does not exist.")