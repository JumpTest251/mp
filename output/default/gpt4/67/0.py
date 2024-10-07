from flask import Flask, escape

app = Flask(__name__)

# Dictionary to map URLs to functions
url_mapping = {}

def route(url):
    def decorator(func):
        url_mapping[url] = func
        return func
    return decorator

@app.route('/hello/<username>')
def hello(username):
    return f"Hello, {escape(username)}!"

if __name__ == '__main__':
    app.run(debug=True)