from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

# Sample product price list
product_prices = {
    'product1': 10.0,
    'product2': 20.0,
    'product3': 15.5
}

@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    yaml_payload = request.args.get('payload')
    
    if not yaml_payload:
        return jsonify({'error': 'No YAML payload provided'}), 400

    try:
        data = yaml.safe_load(yaml_payload)
        product_code = data.get('product_code')
        quantity = data.get('quantity')

        if product_code not in product_prices:
            return jsonify({'error': f'Product {product_code} not found'}), 404

        if quantity <= 0:
            return jsonify({'error': 'Quantity must be greater than zero'}), 400

        total_price = product_prices[product_code] * quantity
        return str(total_price), 200
        
    except yaml.YAMLError as e:
        return jsonify({'error': 'Invalid YAML payload'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)