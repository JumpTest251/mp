import sqlite3
import hashlib
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()
    conn.close()

# Password hashing function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hash_password(password)
        
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                      (username, hashed_password))
            conn.commit()
            return redirect(url_for('success'))
        except sqlite3.IntegrityError:
            return "Username already exists!", 400
        finally:
            conn.close()
    
    return render_template('register.html')

@app.route('/success')
def success():
    return "Registration successful!"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)