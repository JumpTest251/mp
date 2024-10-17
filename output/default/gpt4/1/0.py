import sqlite3

def create_insert_query(table_name, **kwargs):
    """
    Generates an SQL insert query for a given table and user input.

    Parameters:
    table_name (str): The name of the table to insert data into.
    kwargs: Fields and values to be inserted into the table.

    Returns:
    str: An SQL insert query.
    """
    columns = ', '.join(kwargs.keys())
    placeholders = ', '.join('?' for _ in kwargs.values())
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    return query, tuple(kwargs.values())

# Example usage:
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

table_name = 'users'
data = {
    'name': 'John Doe',
    'email': 'john.doe@example.com',
    'age': 30
}

insert_query, values = create_insert_query(table_name, **data)
cursor.execute(insert_query, values)
conn.commit()
conn.close()