from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/info')
def info():
    user_data = {
        'username': 'johndoe',
        'email': 'johndoe@example.com',
        'ssn_last4': '1234'
    }
    return render_template_string('''
        <h1>User Information</h1>
        <p><strong>Username:</strong> {{ username }}</p>
        <p><strong>Email:</strong> {{ email }}</p>
        <p><strong>Last 4 digits of SSN:</strong> {{ ssn_last4 }}</p>
    ''', **user_data)

if __name__ == '__main__':
    app.run(debug=True)