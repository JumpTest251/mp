app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

# Database connection
db = MySQLdb.connect(host="localhost", user="your_user", passwd="your_password", db="your_db")
cursor = db.cursor()

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    
    # Hash the password to compare with the database
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    # Check user credentials in the database
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, hashed_password))
    user = cursor.fetchone()
    
    if user:
        session['user_id'] = user[0]  # Assuming the first column is user_id
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

@app.route("/logout", methods=["POST"])
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logout successful"}), 200

if __name__ == "__main__":
    app.run(debug=True)