from flask import Flask, render_template, request, redirect, url_for, flash, session

# Sample user data
USER_DATA = {
    'username': 'admin',
    'password': 'password'
}

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == USER_DATA['username'] and password == USER_DATA['password']:
        session['username'] = username
        return redirect(url_for('session_page'))
    else:
        flash('Username or password is incorrect')
        return redirect(url_for('home'))

@app.route('/session')
def session_page():
    if 'username' in session:
        return f'Welcome {session["username"]}!'
    else:
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)