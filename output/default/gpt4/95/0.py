from flask import Flask, render_template

app = Flask(__name__)

def route(url):
    def decorator(func):
        app.route(url)(func)  # Bind the function to the URL
        return func
    return decorator

@route('/hello/<username>')
def hello(username):
    return render_template('hello.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)