from flask import Flask, request, send_file, abort

app = Flask(__name__)

@app.route('/img')
def img():
    file_name = request.args.get('file')
    if not file_name:
        abort(400, 'File parameter is required')
    
    try:
        return send_file(file_name, as_attachment=True)
    except Exception as e:
        abort(404, 'File not found')

if __name__ == '__main__':
    app.run(debug=True)