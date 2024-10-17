from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/info')
def info():
    # Dummy data for demonstration purpose
    user_data = {
        'username': 'john_doe',
        'email': 'john@example.com',
        'ssn_last4': '1234'
    }
    
    html_content = """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>User Info</title>
      </head>
      <body>
        <h1>User Information</h1>
        <p><strong>Username:</strong> {{ username }}</p>
        <p><strong>Email:</strong> {{ email }}</p>
        <p><strong>Last 4 Digits of SSN:</strong> {{ ssn_last4 }}</p>
      </body>
    </html>
    """
    
    return render_template_string(html_content, **user_data)

if __name__ == '__main__':
    app.run(debug=True)