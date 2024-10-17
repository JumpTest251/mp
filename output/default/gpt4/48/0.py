from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/img')
def img():
    file_name = request.args.get('file')
    if file_name:
        try:
            with open(file_name, 'rb') as f:
                content = f.read()
            return Response(content, mimetype='image/jpeg')  # Adjust mimetype as needed
        except FileNotFoundError:
            return "File not found", 404
    return "No file parameter provided", 400

if __name__ == '__main__':
    app.run(debug=True)