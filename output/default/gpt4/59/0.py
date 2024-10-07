import subprocess
from flask import Flask, jsonify

app = Flask(__name__)

def url_trigger(route):
    def decorator(func):
        app.route(route)(func)
        return func
    return decorator

@url_trigger('/ping')
def ping():
    url = 'google.com'  # You can set this to any URL you'd like to ping
    try:
        output = subprocess.check_output(['ping', '-c', '4', url], universal_newlines=True)
    except subprocess.CalledProcessError as e:
        output = str(e)
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True)