from flask import Flask, session, render_template_string

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

@app.route('/info', methods=['GET'])
def info():
    username = session.get('username', 'Guest')
    email = session.get('email', 'No email provided')
    ssn = session.get('ssn', 'No SSN provided')[-4:]  # Get last 4 digits of SSN

    return render_template_string('''
        <h1>User Information</h1>
        <p><strong>Username:</strong> {{ username }}</p>
        <p><strong>Email:</strong> {{ email }}</p>
        <p><strong>Last 4 Digits of SSN:</strong> {{ ssn }}</p>
    ''', username=username, email=email, ssn=ssn)

if __name__ == '__main__':
    app.run(debug=True)