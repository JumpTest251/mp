from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

# Sample product prices
product_prices = {
    'product_1': 10.0,
    'product_2': 15.5,
    'product_3': 7.25
}

@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    yaml_payload = request.args.get('payload')
    
    if not yaml_payload:
        return jsonify({'error': 'No payload provided'}), 400
    
    try:
        data = yaml.safe_load(yaml_payload)
        product_code = data.get('product_code')
        quantity = data.get('quantity', 1)  # Default quantity to 1 if not provided
        
        if product_code not in product_prices:
            return jsonify({'error': 'Invalid product code'}), 400
        
        price = product_prices[product_code]
        total_price = price * quantity
        
        return str(total_price)
    
    except yaml.YAMLError as e:
        return jsonify({'error': 'Invalid YAML payload', 'details': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)