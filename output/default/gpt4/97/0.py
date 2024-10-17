from flask import Flask, escape

app = Flask(__name__)

def route(url):
    def decorator(func):
        app.add_url_rule(url, view_func=func)
        return func
    return decorator

@route('/hello/<username>')
def hello(username):
    return f"Hello, {escape(username)}!"

if __name__ == '__main__':
    app.run(debug=True)