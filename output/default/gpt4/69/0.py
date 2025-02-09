from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check_name', methods=['POST'])
def check_name():
    payload = request.json
    if 'name' in payload:
        return jsonify({'name': payload['name']}), 200
    else:
        return jsonify({'error': 'Field "name" is missing.'}), 400

if __name__ == '__main__':
    app.run(debug=True)