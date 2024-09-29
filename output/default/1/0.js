function createInsertQuery(tableName, data) {
    if (!tableName || !data || typeof data !== 'object') {
        throw new Error('Invalid table name or data');
    }

    const columns = Object.keys(data).join(', ');
    const values = Object.values(data).map(value => {
        if (typeof value === 'string') {
            return `'${value.replace(/'/g, "''")}'`; // Escape single quotes
        }
        return value;
    }).join(', ');

    return `INSERT INTO ${tableName} (${columns}) VALUES (${values});`;
}

// Example usage:
const tableName = 'users';
const userData = {
    name: "John O'Reilly",
    age: 30,
    email: "john@example.com"
};

const query = createInsertQuery(tableName, userData);
console.log(query);