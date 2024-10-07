import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def insert_image(connection, image_path):
    try:
        with open(image_path, 'rb') as file:
            binary_data = file.read()
            cursor = connection.cursor()
            sql_insert_blob_query = """INSERT INTO images (image) VALUES (%s)"""
            cursor.execute(sql_insert_blob_query, (binary_data,))
            connection.commit()
            print("Image successfully inserted into the database")
            cursor.close()
    except Exception as e:
        print(f"Failed to insert image into MySQL table: {e}")

if __name__ == "__main__":
    # Database connection parameters
    host = "localhost"
    user = "your_username"
    password = "your_password"
    database = "your_database_name"

    # Connect to the database
    conn = create_connection(host, user, password, database)

    # Image file path
    image_file = "path_to_your_image.jpg"

    # Insert image into the database
    insert_image(conn, image_file)

    # Close database connection
    if conn:
        conn.close()