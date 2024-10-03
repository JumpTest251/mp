def create_insert_query(table_name: str, column_names: List[str], values: List[Any]) -> str:
    # Build the INSERT statement
    insert_stmt = f"INSERT INTO {table_name} ("
    for i in range(len(column_names)):
        if i != 0:
            insert_stmt += ", "
        insert_stmt += column_names[i]
    insert_stmt += ") VALUES ("
    for i in range(len(values)):
        if i != 0:
            insert_stmt += ", "
        insert_stmt += f"?{i+1}"
    insert_stmt += ")"

    # Build the parameters list
    params = []
    for i in range(len(column_names)):
        params.append(values[i])

    return insert_stmt, paramstable_name = "users"
column_names = ["username", "password"]
values = ["john@example.com", "123456"]

query, params = create_insert_query(table_name, column_names, values)

# Execute the query with the parameters
conn = ... # Establish a connection to the database
cursor = conn.cursor()
cursor.execute(query, params)

# Commit the change and close the cursor
conn.commit()
cursor.close()