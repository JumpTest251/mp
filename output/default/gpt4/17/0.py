from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)

def check_file_exists(func):
    def wrapper(filename):
        file_path = os.path.join('images', filename)
        if not os.path.exists(file_path):
            abort(404)  # File not found
        return func(filename)
    return wrapper

@app.route('/image/<filename>')
@check_file_exists
def serve_image(filename):
    return send_from_directory('images', filename)

if __name__ == '__main__':
    app.run(debug=True)