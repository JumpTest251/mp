import sqlite3
from flask import Flask, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database connection
def init_db():
    with sqlite3.connect('stocks.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                stock_name TEXT NOT NULL,
                stock_quantity INTEGER NOT NULL
            )
        ''')
        conn.commit()

@app.route('/buy', methods=['POST'])
def buy_stock():
    username = session.get('username')  # Assuming the user is logged in and username is in session
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']

    with sqlite3.connect('stocks.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO orders (username, stock_name, stock_quantity)
            VALUES (?, ?, ?)
        ''', (username, stock_name, stock_quantity))
        conn.commit()
    
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    # Here you would render the profile page for the user
    return "Profile Page"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)