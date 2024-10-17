from flask import Flask, request, jsonify, session
import MySQLdb

app = Flask(__name__)

# Configuration for MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'your_database'

@app.route("/todos/<username>/<int:todo_id>", methods=["GET"])
def get_todo_by_id(username, todo_id):
    """
    Get a single todo for a user and return the description as a HTML String
    format: "Description: <description>"
    """
    try:
        db = MySQLdb.connect(host=app.config['MYSQL_HOST'],
                             user=app.config['MYSQL_USER'],
                             passwd=app.config['MYSQL_PASSWORD'],
                             db=app.config['MYSQL_DB'])
        cursor = db.cursor()
        query = "SELECT description FROM todos WHERE username = %s AND id = %s"
        cursor.execute(query, (username, todo_id))
        result = cursor.fetchone()

        if result:
            description = result[0]
            return f"Description: {description}", 200
        else:
            return jsonify({"error": "Todo not found"}), 404

    except MySQLdb.Error as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if db:
            db.close()

if __name__ == "__main__":
    app.run(debug=True)