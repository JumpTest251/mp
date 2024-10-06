def create_insertion_query(table_name, data):
    columns = ", ".join([f"'{key}'" for key in data.keys()])
    values = tuple(data.values())
    return f"INSERT INTO {table_name} ({columns}) VALUES ({values});"# Pass the name of the table and a dictionary of column names and their corresponding values
create_insertion_query("users", {"name": "Alice", "age": 30, "weight": 50.0})

# Will return the SQL query: INSERT INTO users (name, age, weight) VALUES ('Alice', 30, 50.0);