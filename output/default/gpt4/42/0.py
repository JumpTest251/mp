from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# Dummy credentials for demonstration
USERNAME = 'admin'
PASSWORD = 'password'

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == USERNAME and password == PASSWORD:
        session['username'] = username
        return redirect(url_for('session_page'))
    else:
        flash('Username or Password is incorrect.', 'danger')
        return redirect(url_for('login_page'))

@app.route('/session')
def session_page():
    if 'username' in session:
        return f'Welcome, {session["username"]}!'
    return redirect(url_for('login_page'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login_page'))

if __name__ == '__main__':
    app.run(debug=True)