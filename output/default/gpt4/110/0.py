from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stocks.db'
db = SQLAlchemy(app)

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buy_order', methods=['POST'])
def buy_order():
    stock_name = request.form['stock_name']
    quantity = request.form['quantity']
    new_stock = Stock(name=stock_name, quantity=int(quantity))
    db.session.add(new_stock)
    db.session.commit()
    return redirect(url_for('stock_view'))

@app.route('/stock_view')
def stock_view():
    stocks = Stock.query.all()
    return render_template('stock_view.html', stocks=stocks)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)