from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    with sqlite3.connect('stocks.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS stock_orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                stock_name TEXT NOT NULL,
                quantity INTEGER NOT NULL
            )
        ''')
        conn.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        stock_name = request.form['stock_name']
        quantity = request.form['quantity']
        return redirect(f'/buy_order?stock_name={stock_name}&quantity={quantity}')
    return render_template('form.html')

@app.route('/buy_order')
def buy_order():
    stock_name = request.args.get('stock_name')
    quantity = request.args.get('quantity')

    # Insert into database
    with sqlite3.connect('stocks.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO stock_orders (stock_name, quantity) VALUES (?, ?)", (stock_name, quantity))
        conn.commit()
    
    return redirect('/stock_view')

@app.route('/stock_view')
def stock_view():
    with sqlite3.connect('stocks.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM stock_orders")
        orders = cursor.fetchall()
    return render_template('stock_view.html', orders=orders)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)