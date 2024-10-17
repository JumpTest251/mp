from flask import Flask, request, redirect, render_template

app = Flask(__name__)

def insert_user_message_in_db(username, message):
    # Example implementation of database insertion
    # This should connect to your database and insert the username and message
    pass

@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        return post()
    return render_template('main_page.html')

def post():
    username = request.form.get('username')
    message = request.form.get('message')
    insert_user_message_in_db(username, message)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)