import sqlite3

def unsubscribe(email):
    # Connect to the database
    conn = sqlite3.connect('database.db')  # Replace 'database.db' with your database file
    cursor = conn.cursor()
    
    # Check if the email exists in the database
    cursor.execute("SELECT * FROM subscribers WHERE email = ?", (email,))
    result = cursor.fetchone()
    
    if result:
        # Email exists, proceed with removal
        cursor.execute("DELETE FROM subscribers WHERE email = ?", (email,))
        conn.commit()
        print(f"The email address {email} has been successfully unsubscribed.")
    else:
        # Email does not exist
        print(f"The email address {email} is not found in the database.")
    
    # Close the database connection
    cursor.close()
    conn.close()

# Example Usage
if __name__ == "__main__":
    user_email = input("Please enter your email address to unsubscribe: ")
    unsubscribe(user_email)