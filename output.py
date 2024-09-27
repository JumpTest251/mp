def generate_insert_query(table_name, data):
    """
    Generates an SQL INSERT query based on the provided table name and data dictionary.

    :param table_name: str, the name of the table to insert data into
    :param data: dict, a dictionary where the keys are column names and values are the data to insert
    :return: str, the formatted SQL INSERT query
    """
    columns = ', '.join(data.keys())
    placeholders = ', '.join(['%s'] * len(data))
    sql_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders});"
    return sql_query, list(data.values())

# Example usage
table = "users"
user_data = {
    "username": "johndoe",
    "email": "johndoe@example.com",
    "age": 30
}
query, values = generate_insert_query(table, user_data)
print(query)  # Outputs: INSERT INTO users (username, email, age) VALUES (%s, %s, %s);
print(values) # Outputs: ['johndoe', 'johndoe@example.com', 30]