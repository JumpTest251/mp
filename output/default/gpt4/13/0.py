from flask import Flask, session, render_template_string

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

@app.route('/info', methods=['GET'])
def info():
    username = session.get('username', 'N/A')
    email = session.get('email', 'N/A')
    ssn = session.get('ssn', 'N/A')[-4:]  # Get last 4 digits of SSN
    return render_template_string("""
        <html>
            <body>
                <h1>User Info</h1>
                <p><strong>Username:</strong> {{ username }}</p>
                <p><strong>Email:</strong> {{ email }}</p>
                <p><strong>Last 4 digits of SSN:</strong> {{ ssn }}</p>
            </body>
        </html>
    """, username=username, email=email, ssn=ssn)

if __name__ == '__main__':
    app.run(debug=True)