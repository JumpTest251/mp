from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

# Sample product prices
product_prices = {
    'product_1': 10.0,
    'product_2': 15.5,
    'product_3': 7.25,
}

def get_price_for_product_code(product_code):
    return product_prices.get(product_code, 0)

@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    yaml_payload = request.args.get('payload')
    if not yaml_payload:
        return jsonify({'error': 'Missing payload'}), 400
    
    try:
        data = yaml.safe_load(yaml_payload)
        product_code = data.get('product_code')
        quantity = data.get('quantity', 0)
        
        price_per_unit = get_price_for_product_code(product_code)
        total_price = price_per_unit * quantity
        
        response = {
            'product_code': product_code,
            'quantity': quantity,
            'total_price': total_price
        }
        return yaml.dump(response), 200, {'Content-Type': 'application/x-yaml'}
    
    except yaml.YAMLError:
        return jsonify({'error': 'Invalid YAML format'}), 400

if __name__ == '__main__':
    app.run(debug=True)