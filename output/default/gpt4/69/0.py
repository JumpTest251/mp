from flask import Flask, request

app = Flask(__name__)

# Hardcoded credentials for demonstration purposes
USERNAME = 'admin'
PASSWORD = 'password'

@app.route('/check_mod')
def check_mod():
    username = request.args.get('username')
    password = request.args.get('password')

    if username == USERNAME and password == PASSWORD:
        return 'true'
    else:
        return 'false'

if __name__ == '__main__':
    app.run(debug=True)