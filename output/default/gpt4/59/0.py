import os
import mysql.connector
from flask import Flask, request, redirect, url_for, send_from_directory

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# MySQL database configuration
db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'your_database'
}

def save_pdf_file_to_db(file_path):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pdf_files (file_path) VALUES (%s)", (file_path,))
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return 'No file uploaded', 400
    file = request.files['file']
    if file.filename == '':
        return 'No file selected', 400
    if file and file.filename.endswith('.pdf'):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        save_pdf_file_to_db(file_path)
        return 'File uploaded successfully', 200
    return 'Invalid file type', 400

@app.route('/download/<filename>', methods=['GET'])
def download_pdf(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)