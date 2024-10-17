from flask import Flask, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')  # Replace with your actual database
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/buy_stock', methods=['POST'])
def buy_stock():
    username = request.form['username']
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']

    # Insert buy order into the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO buy_orders (username, stock_name, stock_quantity) 
        VALUES (?, ?, ?)
    ''', (username, stock_name, stock_quantity))
    conn.commit()
    conn.close()

    # Redirect to profile page
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    return "Welcome to your profile!"

if __name__ == '__main__':
    app.run(debug=True)