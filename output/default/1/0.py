def create_insert_query(table_name, columns, values):
    if len(columns) != len(values):
        raise ValueError("Number of columns and values must match.")

    columns_str = ', '.join(f"`{column}`" for column in columns)
    placeholders_str = ', '.join('%s' for _ in values)  # Using placeholders for safety

    query = f"INSERT INTO `{table_name}` ({columns_str}) VALUES ({placeholders_str});"
    return query, values

# Example usage:
table_name = 'users'
columns = ['name', 'email', 'age']
values = ['John Doe', 'john@example.com', 30]

query, params = create_insert_query(table_name, columns, values)
print(query)
print(params)