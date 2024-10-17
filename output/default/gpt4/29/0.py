from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

def generate_otp(length=6):
    digits = string.digits
    otp = ''.join(random.choice(digits) for _ in range(length))
    return otp

@app.route('/users/login', methods=['POST'])
def user_login():
    username = request.json.get('username')
    if not username:
        return jsonify({'error': 'Username is required'}), 400

    otp = generate_otp()
    # Here you would typically save the OTP associated with the user in a database

    return jsonify({'username': username, 'otp': otp}), 200

if __name__ == '__main__':
    app.run(debug=True)