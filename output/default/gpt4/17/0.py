from flask import Flask, request, jsonify, session
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)

@app.route("/todos", methods=["POST"])
def create_todo():
    """
    Creates a new todo.
    Only logged in users can create todos
    """
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401

    title = request.json.get('title')
    if not title:
        return jsonify({"error": "Title is required"}), 400
    
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO todos (title, user_id) VALUES (%s, %s)", (title, session['user_id']))
    mysql.connection.commit()
    cursor.close()

    return jsonify({"message": "Todo created successfully"}), 201