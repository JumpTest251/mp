from flask import Flask, send_file, abort
import os

app = Flask(__name__)

def check_file_exists(f):
    def wrapper(filename):
        file_path = os.path.join('images', filename)
        if os.path.isfile(file_path):
            return f(file_path)
        else:
            return abort(404)
    return wrapper

@app.route('/image/<filename>')
@check_file_exists
def send_image(file_path):
    return send_file(file_path)

if __name__ == '__main__':
    app.run(debug=True)