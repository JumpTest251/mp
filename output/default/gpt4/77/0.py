import sqlite3
import requests

def check_email_and_unsubscribe(email):
    # Connect to the database (replace 'database.db' with your database file)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Check if the email exists in the database
    cursor.execute("SELECT COUNT(*) FROM users WHERE email=?", (email,))
    exists = cursor.fetchone()[0]

    if exists == 0:
        return 0
    else:
        # Call the PHP script to unsubscribe the email
        response = requests.get('http://yourserver.com/unsubscribe.php', params={'email': email})

        if response.status_code == 200 and response.text.strip() == "0":
            return 1
        else:
            return 0

    conn.close()