# Required libraries
from flask import Flask, request, redirect, url_for, render_template
import sqlite3

app = Flask(__name__)

# Mock database connection (replace with your actual database connection)
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

# Login page route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return login_user(username, password)
    return render_template('login.html')

# Login function
def login_user(username, password):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    conn.close()
    
    if user is None:
        return "Username does not exist", 401

    if user['password'] == password:
        return redirect(url_for('home'))
    else:
        return "Incorrect password", 401

# Home page route
@app.route('/home')
def home():
    return "Welcome to the home page!"

if __name__ == '__main__':
    app.run(debug=True)