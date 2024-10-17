from flask import Flask, request, jsonify, session
import MySQLdb

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your actual secret key

# MySQL database connection
def get_db_connection():
    connection = MySQLdb.connect(
        host='localhost',
        user='your_username',      # Replace with your database username
        password='your_password',  # Replace with your database password
        db='your_database'         # Replace with your database name
    )
    return connection

# Route to return all todos for a user provided in the url
@app.route("/todos/<username>", methods=["GET"])
def get_todos(username):
    """
    Get all todos for a user and return them
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM todos WHERE username = %s", (username,))
    todos = cursor.fetchall()
    cursor.close()
    connection.close()

    # Format the response
    todos_list = [{'id': todo[0], 'task': todo[1], 'completed': todo[2]} for todo in todos]
    return jsonify(todos_list)

if __name__ == "__main__":
    app.run(debug=True)