from flask import Flask, request, redirect, render_template, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def insert_user_message_in_db(username, message):
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (username, message) VALUES (?, ?)", (username, message))
    conn.commit()
    conn.close()

@app.route('/post', methods=['POST'])
def post():
    username = request.form.get('username')
    message = request.form.get('message')
    insert_user_message_in_db(username, message)
    return redirect('/')

@app.route('/')
def main_page():
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username, message FROM messages")
    messages = cursor.fetchall()
    conn.close()
    return render_template('main_page.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)