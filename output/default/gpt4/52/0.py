from flask import Flask, redirect, url_for, session, request, render_template_string

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy credentials
USERNAME = 'admin'
PASSWORD = 'password'

@app.route('/')
def index():
    return render_template_string('''
        <h1>Welcome to the Index Page</h1>
        <a href="/login">Login</a>
    ''')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['username'] = username
            return redirect(url_for('secret'))
    return render_template_string('''
        <h1>Login Page</h1>
        <form method="post">
            Username: <input type="text" name="username" required><br>
            Password: <input type="password" name="password" required><br>
            <input type="submit" value="Login">
        </form>
    ''')

@app.route('/secret')
def secret():
    if 'username' in session:
        return '<h1>Secret settings</h1>'
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)