import sqlite3

def unsubscribe(email):
    # Connect to the database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Check if the email address exists
    cursor.execute("SELECT * FROM subscribers WHERE email = ?", (email,))
    result = cursor.fetchone()
    
    if result:
        # Email is in the database, remove it
        cursor.execute("DELETE FROM subscribers WHERE email = ?", (email,))
        conn.commit()
        print(f"{email} has been successfully unsubscribed.")
    else:
        # Email is not in the database
        print(f"{email} is not in the database.")
    
    # Close the database connection
    conn.close()

# Example of usage
email_to_unsubscribe = input("Enter your email address to unsubscribe: ")
unsubscribe(email_to_unsubscribe)