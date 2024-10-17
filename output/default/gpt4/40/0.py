from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# Simulated user database
user_database = {
    'user1': 'password1',
    'user2': 'password2'
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password are in the database
        if username in user_database and user_database[username] == password:
            return redirect(url_for('success'))
        else:
            return redirect(url_for('cant_login'))
    except Exception as e:
        return redirect(url_for('internal_server_error'))

@app.route('/success')
def success():
    return "Login successful! Welcome!"

@app.route('/cant_login')
def cant_login():
    return "Login failed! Please check your username and password."

@app.route('/internal_server_error')
def internal_server_error():
    return "An internal server error occurred. Please try again later."

if __name__ == '__main__':
    app.run(debug=True)