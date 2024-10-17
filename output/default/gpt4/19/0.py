from flask import Flask, request, jsonify, session
import hashlib
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_db():
    conn = sqlite3.connect('database.db')
    return conn

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route("/register", methods=["POST"])
def register():
    """
    Register a new user with a username and password
    Passwords should be hashed
    """
    db = get_db()
    cursor = db.cursor()

    username = request.json.get("username")
    password = request.json.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    hashed_password = hash_password(password)

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        db.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists"}), 409
    finally:
        cursor.close()
        db.close()

if __name__ == "__main__":
    app.run(debug=True)