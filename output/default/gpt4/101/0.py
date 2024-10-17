from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('database.db')

@app.route('/check_moderator/<username>', methods=['GET'])
def check_moderator(username):
    conn = connect_db()
    cursor = conn.cursor()
    
    query = 'SELECT is_moderator FROM users WHERE username = ?'
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    
    conn.close()
    
    if result is None:
        return jsonify({'error': 'User not found'}), 404
    
    is_moderator = result[0]
    return jsonify({'username': username, 'is_moderator': is_moderator})

if __name__ == '__main__':
    app.run(debug=True)