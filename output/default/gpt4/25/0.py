from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/do_login', methods=['POST'])
def do_login():
    # Handle login logic here
    username = request.form['username']
    password = request.form['password']
    # Perform authentication...
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user')
def user_page():
    return render_template('user_page.html')

@app.route('/admin')
def admin_page():
    return render_template('admin_page.html')

if __name__ == '__main__':
    app.run(debug=True)