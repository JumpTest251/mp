import sqlite3

def buy_stock(stock_name, quantity):
    # Connect to the database
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    
    # Insert the stock purchase into the database
    cursor.execute("INSERT INTO purchases (stock_name, quantity) VALUES (?, ?)", (stock_name, quantity))
    conn.commit()
    
    # Close the database connection
    conn.close()
    
    # Call the buy_function
    buy_function(stock_name)

def buy_function(stock_name):
    # Logic for processing the stock purchase 
    print(f"Processing purchase for {stock_name}")

# Example of how this function would be called on a button click
# Assuming 'stock_name' and 'quantity' are obtained from the form
# stock_name = "AAPL"  # This would come from the user input
# quantity = 10        # This would also come from the user input
# buy_stock(stock_name, quantity)