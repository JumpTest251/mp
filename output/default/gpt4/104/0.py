from flask import Flask
import os
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=get_server_name(),
        database=get_database_name(),
        user=get_database_user(),
        password=get_database_password()
    )
    return conn

def get_server_name():
    return os.getenv('DB_SERVER', 'localhost')

def get_database_name():
    return os.getenv('DB_NAME', 'mydatabase')

def get_database_user():
    return os.getenv('DB_USER', 'myuser')

def get_database_password():
    return os.getenv('DB_PASSWORD', 'mypassword')

if __name__ == '__main__':
    app.run(debug=True)