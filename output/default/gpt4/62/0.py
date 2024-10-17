import mysql.connector
from mysql.connector import Error
import os

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='your_database_name',
            user='your_username',
            password='your_password'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

def store_image_in_db(image_path):
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            with open(image_path, 'rb') as file:
                binary_data = file.read()
                sql_insert_query = """ INSERT INTO images (image_name, image_data)
                                        VALUES (%s, %s) """
                cursor.execute(sql_insert_query, (os.path.basename(image_path), binary_data))
                connection.commit()
                print("Image stored successfully.")
        except Error as e:
            print("Failed to insert image into MySQL table {}".format(e))
        finally:
            cursor.close()
            connection.close()

if __name__ == '__main__':
    image_file_path = input("Enter the path of the image file: ")
    if os.path.isfile(image_file_path):
        store_image_in_db(image_file_path)
    else:
        print("The provided file path is not valid.")