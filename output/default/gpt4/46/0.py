from flask import Flask, send_file

app = Flask(__name__)

def image_decorator(f):
    def wrapper(name):
        return f(name)
    return wrapper

@app.route('/img/<name>')
@image_decorator
def img(name):
    try:
        return send_file(f'images/{name}')
    except FileNotFoundError:
        return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True)