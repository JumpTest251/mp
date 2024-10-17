import os
import psycopg2

def is_user_moderator(username):
    # Retrieve database credentials from environment variables
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')

    try:
        # Establish a database connection
        connection = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        cursor = connection.cursor()
        
        # Execute the query to check if the user is a moderator
        query = "SELECT is_moderator FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        
        if result is not None:
            return result[0]  # Assuming is_moderator is a boolean field
        else:
            return False  # User not found
    except Exception as e:
        print(f"Error: {e}")
        return False
    finally:
        if connection:
            cursor.close()
            connection.close()

# Example usage
# print(is_user_moderator('example_username'))