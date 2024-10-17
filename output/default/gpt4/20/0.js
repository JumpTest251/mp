const express = require('express');
const mysql = require('mysql');
const app = express();

// Create a connection to the database
const db = mysql.createConnection({
    host: 'localhost',
    user: 'your_username',
    password: 'your_password',
    database: 'your_database'
});

// Connect to the database
db.connect((err) => {
    if (err) {
        console.error('Database connection failed: ' + err.stack);
        return;
    }
    console.log('Connected to database.');
});

// Route to return all todos for a user provided in the URL
app.get('/todos/:username', (req, res) => {
    const username = req.params.username;
    const query = 'SELECT * FROM todos WHERE username = ?';

    db.query(query, [username], (err, results) => {
        if (err) {
            return res.status(500).json({ error: 'Database query failed' });
        }
        res.json(results);
    });
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});