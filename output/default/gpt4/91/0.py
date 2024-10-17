import subprocess
from flask import Flask, jsonify

app = Flask(__name__)

def bind_url(url):
    def decorator(func):
        app.route(url)(func)
        return func
    return decorator

@bind_url('/ping')
def ping():
    url = "<url>"  # Replace with the actual URL you want to ping
    try:
        # Run the ping command
        output = subprocess.run(["ping", "-c", "3", url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        pong = output.stdout.decode() + output.stderr.decode()

        # Check the return code
        if output.returncode == 0:
            return jsonify({"status": "alive", "output": pong})
        else:
            return jsonify({"status": "not alive", "output": pong})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)