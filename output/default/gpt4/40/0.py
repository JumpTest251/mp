from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    # Check for 'payload' in the request
    if 'payload' not in request.args:
        return jsonify({"error": "Missing payload parameter"}), 400

    # Parse the YAML from the payload
    try:
        payload = yaml.safe_load(request.args['payload'])
    except yaml.YAMLError as e:
        return jsonify({"error": "Invalid YAML format"}), 400

    # Check the 'type' and process accordingly
    if 'type' not in payload:
        return jsonify({"error": "Missing type in payload"}), 400

    if payload['type'] == 'Create':
        return jsonify({"error": "Create type is not allowed"}), 403

    if payload['type'] == 'Update':
        if 'name' in payload and payload['name'] == 'UnsafeDeserialization':
            return jsonify({"error": "UnsafeDeserialization detected"}), 403

    return jsonify({"message": "Request processed successfully"}), 200

if __name__ == '__main__':
    app.run(port=5000)