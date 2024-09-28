def generate_insert_query(table_name, data):
    """
    Generates an SQL INSERT query based on the provided table name and data.

    :param table_name: Name of the table
    :param data: Dictionary containing column names as keys and values as data to insert
    :return: SQL INSERT query string
    """
    columns = ', '.join(data.keys())
    placeholders = ', '.join(['%s'] * len(data))
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    return query

# Example usage:
table = "users"
user_data = {
    "username": "john_doe",
    "email": "john@example.com",
    "age": 30
}

insert_query = generate_insert_query(table, user_data)
print(insert_query)