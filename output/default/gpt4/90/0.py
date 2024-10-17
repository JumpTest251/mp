from flask import Flask, request
import subprocess

app = Flask(__name__)

def bind_url(url):
    def decorator(func):
        app.add_url_rule(url, func.__name__, func)
        return func
    return decorator

@bind_url('/ping')
def ping():
    url = request.args.get('url')
    if not url:
        return "Please provide a URL to ping.", 400
    
    try:
        result = subprocess.run(['ping', '-c', '4', url], capture_output=True, text=True)
        return f"<pre>{result.stdout}</pre>", 200
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)