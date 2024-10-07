from flask import Flask, request, redirect, render_template, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ensure to set a secret key for session management

# Dummy database for demonstration purposes
users_db = {
    "user1": "password1",
    "user2": "password2"
}

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/do_login', methods=['POST'])
def do_login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username in users_db and users_db[username] == password:
        return redirect('/user_page')
    else:
        flash('Invalid username or password.')
        return redirect('/login')

@app.route('/user_page')
def user_page():
    return "Welcome to your user page!"

if __name__ == '__main__':
    app.run(debug=True)