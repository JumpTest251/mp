from flask import Flask, request, render_template_string

app = Flask(__name__)

# Dummy database for username/password
users_db = {
    "user1": "password1",
    "user2": "password2"
}

@app.route('/')
def home():
    return render_template_string('''
        <form method="post" action="/check_mod">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Submit">
        </form>
    ''')

@app.route('/check_mod', methods=['POST'])
def check_mod():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users_db and users_db[username] == password:
        return 'true'
    else:
        return 'false'

if __name__ == '__main__':
    app.run(debug=True)