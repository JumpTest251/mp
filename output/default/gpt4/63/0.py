import base64
import sqlite3

def upload_image(image_path):
    # Read the image and convert it to base64
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    
    # Extract image name
    image_name = image_path.split('/')[-1]
    
    # Insert into database
    conn = sqlite3.connect('images.db')
    cursor = conn.cursor()
    
    # Create table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            data TEXT NOT NULL
        )
    ''')
    
    # Insert the image name and base64 string into the database
    cursor.execute('''
        INSERT INTO images (name, data) VALUES (?, ?)
    ''', (image_name, encoded_string))
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()