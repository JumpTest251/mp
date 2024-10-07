from flask import Flask, send_file

app = Flask(__name__)

def url_decorator(url_rule):
    def decorator(f):
        app.add_url_rule(url_rule, f.__name__, f)
        return f
    return decorator

@url_decorator('/img/<name>')
def img(name):
    return send_file(f'images/{name}', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)