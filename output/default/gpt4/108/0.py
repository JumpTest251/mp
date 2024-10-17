import sqlite3

def buy_stock(stock_name, quantity):
    # Insert stock purchase into the database
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO purchases (stock_name, quantity) VALUES (?, ?)", (stock_name, quantity))
    conn.commit()
    
    # Call buy_function with the stock name
    buy_function(stock_name)
    
    conn.close()

def buy_function(stock_name):
    # Logic for handling the stock purchase
    print(f"Processing purchase for {stock_name}")

# Example usage when the user clicks the buy button
if __name__ == "__main__":
    stock_name = "AAPL"  # Example stock name
    quantity = 10        # Example quantity
    buy_stock(stock_name, quantity)