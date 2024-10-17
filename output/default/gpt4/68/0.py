from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    payload = request.args.get('payload')
    if payload:
        try:
            # Convert the payload string to a dictionary
            payload_dict = eval(payload)  # Note: eval can be dangerous, consider using json.loads() instead for safer parsing
            name_value = payload_dict.get('name', None)

            if name_value is not None:
                return jsonify({'name': name_value}), 200
            else:
                return jsonify({'error': 'name not found in payload'}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    else:
        return jsonify({'error': 'payload parameter is missing'}), 400

if __name__ == '__main__':
    app.run(debug=True)