from flask import Flask, request, redirect, url_for, render_template
import sqlite3

app = Flask(__name__)

def insert_user_message_in_db(username, message):
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS messages (username TEXT, message TEXT)")
    cursor.execute("INSERT INTO messages (username, message) VALUES (?, ?)", (username, message))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username, message FROM messages")
    messages = cursor.fetchall()
    conn.close()
    return render_template('index.html', messages=messages)

@app.route('/post', methods=['POST'])
def post_message():
    username = request.form['username']
    message = request.form['message']
    insert_user_message_in_db(username, message)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)