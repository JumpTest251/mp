from flask import Flask, request, jsonify

app = Flask(__name__)

# Example product prices
product_prices = {
    'A001': 10.0,
    'A002': 15.5,
    'A003': 7.25
}

def get_product_price(product_code):
    return product_prices.get(product_code, 0)

@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    product_code = request.args.get('product_code')
    quantity = int(request.args.get('quantity', 1))
    
    price_per_unit = get_product_price(product_code)
    total_price = price_per_unit * quantity
    
    return jsonify({
        'product_code': product_code,
        'quantity': quantity,
        'total_price': total_price
    })

if __name__ == '__main__':
    app.run(port=5000)