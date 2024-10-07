import base64
import sqlite3

def upload_image(image_path):
    # Read the image and convert it to base64
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    
    # Extract image name from the image path
    image_name = image_path.split('/')[-1]
    
    # Insert image name and base64 string into the database
    connection = sqlite3.connect('images.db')
    cursor = connection.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            data TEXT NOT NULL
        )
    ''')
    
    # Insert the image data
    cursor.execute('''
        INSERT INTO images (name, data) VALUES (?, ?)
    ''', (image_name, encoded_image))
    
    # Commit the transaction and close the connection
    connection.commit()
    connection.close()

# Example usage
# upload_image("path/to/your/image.jpg")