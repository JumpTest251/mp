import subprocess
from flask import Flask, jsonify

app = Flask(__name__)

def url_ping_decorator(url):
    def decorator(func):
        @app.route(url, methods=['GET'])
        def wrapper():
            try:
                output = subprocess.check_output(["ping", "-c", "1", url], stderr=subprocess.STDOUT)
                pong = output.decode('utf-8')
                return jsonify({"url": url, "status": "alive", "output": pong}), 200
            except subprocess.CalledProcessError:
                return jsonify({"url": url, "status": "not alive"}), 200
        return wrapper
    return decorator

@url_ping_decorator('ping')
def ping():
    pass  # This function is not used, but must be defined to apply the decorator.

if __name__ == '__main__':
    app.run(debug=True)