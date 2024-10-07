from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy username and password for demonstration
USERNAME = 'admin'
PASSWORD = 'password123'

@app.route('/')
def index():
    return '<h1>Index Page</h1><a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['username'] = username
            return redirect('/secret')
        else:
            return '<h1>Invalid credentials! Please try again.</h1>'
    return '''
        <h1>Login Page</h1>
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/secret')
def secret():
    if 'username' in session:
        return '<h1>Secret Settings</h1>'
    else:
        return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)