from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)

# Simulated user data
users = {
    'admin': 'admin_password',
    'user': 'user_password'
}

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/do_login', methods=['POST'])
def do_login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username in users and users[username] == password:
        if username == 'admin':
            return redirect(url_for('admin_page'))
        else:
            return "You are not authorized to access this page."
    else:
        return "Invalid credentials."

@app.route('/admin_page')
def admin_page():
    return "Welcome to the admin page!"

if __name__ == '__main__':
    app.run(debug=True)