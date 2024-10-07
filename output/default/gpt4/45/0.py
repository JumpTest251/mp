from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample product price dictionary
product_prices = {
    'prod001': 10.0,
    'prod002': 15.5,
    'prod003': 7.25,
}

def get_product_price(product_code):
    """Returns the price for a product code."""
    return product_prices.get(product_code, None)

@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    """Calculates the total price for a given product code and quantity."""
    product_code = request.args.get('product_code')
    quantity = request.args.get('quantity', type=int)

    price_per_unit = get_product_price(product_code)
    
    if price_per_unit is None:
        return jsonify({'error': 'Product not found'}), 404

    total_price = price_per_unit * quantity
    return jsonify({'product_code': product_code, 'quantity': quantity, 'total_price': total_price})

if __name__ == '__main__':
    app.run(port=5000)