from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    payload = request.args.get('payload')
    if payload:
        try:
            data = eval(payload)  # It is recommended to use `json.loads` for safety
            name = data.get('name', 'Name not found')
            return jsonify({'name': name})
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    return jsonify({'error': 'No payload provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)