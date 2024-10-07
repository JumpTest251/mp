from flask import Flask, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a random secret key

@app.route('/')
def home():
    if 'logged_in' in session:
        if session.get('is_admin'):
            return redirect(url_for('admin_page'))
        else:
            return redirect(url_for('user_page'))
    else:
        return redirect(url_for('login_page'))

@app.route('/login')
def login_page():
    # Render login page or handle login logic here
    return "This is the login page."

@app.route('/user')
def user_page():
    return "This is the user page."

@app.route('/admin')
def admin_page():
    return "This is the admin page."

@app.route('/login_user', methods=['POST'])
def login_user():
    # This is where you would handle the actual login logic
    # After successful login
    session['logged_in'] = True
    session['is_admin'] = False  # Set to True if the user is an admin

    return redirect(url_for('home'))

@app.route('/login_admin', methods=['POST'])
def login_admin():
    # This is where you would handle the actual admin login logic
    # After successful admin login
    session['logged_in'] = True
    session['is_admin'] = True

    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('is_admin', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)