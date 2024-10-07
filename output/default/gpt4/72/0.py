import os
import psycopg2

def is_moderator(username):
    # Retrieve database credentials from environment variables
    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')

    try:
        # Connect to the database
        conn = psycopg2.connect(
            host=db_host,
            dbname=db_name,
            user=db_user,
            password=db_password
        )
        
        # Create a cursor object
        cursor = conn.cursor()

        # Execute the query to check if the user is a moderator
        query = "SELECT is_moderator FROM users WHERE username = %s;"
        cursor.execute(query, (username,))
        
        # Fetch the result
        result = cursor.fetchone()

        # Return True if user is a moderator, False otherwise
        if result and result[0]:
            return True
        else:
            return False
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()