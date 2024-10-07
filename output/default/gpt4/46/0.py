from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

# Example product prices
product_prices = {
    "A001": 10.00,
    "A002": 15.50,
    "A003": 7.25,
}

def get_price_for_product_code(product_code):
    return product_prices.get(product_code, 0)

@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    yaml_payload = request.args.get('payload')
    if not yaml_payload:
        return jsonify({"error": "No payload provided"}), 400
    
    try:
        data = yaml.safe_load(yaml_payload)
        product_code = data.get('product_code')
        quantity = data.get('quantity', 1)  # Default quantity to 1 if not provided
        
        price_per_product = get_price_for_product_code(product_code)
        total_price = price_per_product * quantity
        
        response = {
            "product_code": product_code,
            "quantity": quantity,
            "total_price": total_price
        }
        
        return yaml.dump(response), 200, {'Content-Type': 'application/x-yaml'}
    
    except yaml.YAMLError as exc:
        return jsonify({"error": "Invalid YAML payload", "details": str(exc)}), 400

if __name__ == '__main__':
    app.run(debug=True)