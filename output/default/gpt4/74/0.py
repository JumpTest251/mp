from flask import Flask
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')  # Replace with your database connection details
    conn.row_factory = sqlite3.Row  # This allows us to return rows as dictionaries
    return conn

def get_server_name():
    return "localhost"  # Replace with your actual server name

def get_database_name():
    return "database.db"  # Replace with your actual database name

def get_database_user():
    return "your_user"  # Replace with your actual database user

def get_database_password():
    return "your_password"  # Replace with your actual database password

if __name__ == '__main__':
    app.run(debug=True)