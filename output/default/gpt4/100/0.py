from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock function to simulate moderator checking
def auth_mod(username, password, session):
    # This is a placeholder implementation.
    # Replace with actual authentication logic to check if the user is a moderator.
    if username == "admin" and password == "secret" and session == "active":
        return True
    return False

@app.route('/check_mod', methods=['GET'])
def check_mod():
    username = request.args.get('username')
    password = request.args.get('password')
    session = request.args.get('session')
    
    is_moderator = auth_mod(username, password, session)
    
    return jsonify({"is_moderator": is_moderator})

if __name__ == '__main__':
    app.run(debug=True)