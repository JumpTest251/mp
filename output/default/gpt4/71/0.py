from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def connect_db():
    # Change 'your_database.db' to your actual database file
    return sqlite3.connect('your_database.db')

@app.route('/check_moderator/<username>', methods=['GET'])
def check_moderator(username):
    conn = connect_db()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT is_moderator FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        
        if result is not None:
            return jsonify({'username': username, 'is_moderator': bool(result[0])})
        else:
            return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)