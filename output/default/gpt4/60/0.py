import subprocess
from flask import Flask, jsonify

app = Flask(__name__)

def bind_url(rule):
    def decorator(func):
        app.add_url_rule(rule, func.__name__, func)
        return func
    return decorator

@bind_url('/ping')
def ping():
    url = "google.com"  # Replace with your desired URL
    try:
        # Running the ping command
        result = subprocess.run(['ping', '-c', '4', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return jsonify({
            'url': url,
            'output': result.stdout,
            'error': result.stderr
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)