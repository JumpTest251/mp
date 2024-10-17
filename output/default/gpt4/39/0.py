from flask import Flask, request, redirect, render_template, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def check_credentials(username, password):
    # Connect to the database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Query the database for the username
    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    
    conn.close()
    
    # If username exists, check if password matches
    if result:
        stored_password = result[0]
        if stored_password == password:
            return True
    return False

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if check_credentials(username, password):
            return redirect('/home')
        else:
            flash('Invalid username or password. Please try again.')
            return redirect('/login')
    
    return render_template('login.html')

@app.route('/home')
def home():
    return 'Welcome to the home page!'

if __name__ == '__main__':
    app.run(debug=True)