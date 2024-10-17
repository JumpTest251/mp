from flask import Flask
import subprocess

app = Flask(__name__)

def url_decorator(route):
    def decorator(func):
        app.add_url_rule(route, view_func=func)
        return func
    return decorator

@url_decorator('/ping/<path:url>')
def ping(url):
    try:
        # Run the ping command and capture the output
        output = subprocess.check_output(['ping', '-c', '4', url], stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        output = e.output
    return output

if __name__ == '__main__':
    app.run(debug=True)