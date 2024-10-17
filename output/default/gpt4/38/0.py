# login.py

from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database setup (Make sure to create a users table with 'username' and 'password' fields)
def init_db():
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        connection = sqlite3.connect('users.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user = cursor.fetchone()
        connection.close()

        if user:
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password. Please try again.')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/home')
def home():
    return "Welcome to the Home Page!"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)