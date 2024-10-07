import sqlite3

def create_insert_query(table_name, data):
    """
    Creates an SQL insert query for a given table and data.

    Parameters:
        table_name (str): The name of the table to insert data into.
        data (dict): A dictionary where the keys are column names and the values are the data to insert.

    Returns:
        str: An SQL insert query.
    """
    columns = ', '.join(data.keys())
    placeholders = ', '.join('?' for _ in data)
    query = f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})'
    
    return query, tuple(data.values())

# Example usage:
if __name__ == "__main__":
    table = "users"
    user_data = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "age": 30
    }
    
    query, values = create_insert_query(table, user_data)
    print("SQL Query:", query)
    print("Values:", values)
    
    # For executing the query, you can use:
    # conn = sqlite3.connect('database.db')
    # cursor = conn.cursor()
    # cursor.execute(query, values)
    # conn.commit()
    # conn.close()