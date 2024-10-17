from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/do_login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    # Authenticate the user (this is a placeholder for demonstration)
    if username == "admin" and password == "password":
        return redirect(url_for('admin_page'))
    return redirect(url_for('login'))

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/user', methods=['GET'])
def user_page():
    return render_template('user_page.html')

@app.route('/admin', methods=['GET'])
def admin_page():
    return render_template('admin_page.html')

if __name__ == '__main__':
    app.run(debug=True)