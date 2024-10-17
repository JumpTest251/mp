import os
from flask import Flask, request

app = Flask(__name__)

# Create the uploads directory if it doesn't exist
uploads_dir = 'uploads'
os.makedirs(uploads_dir, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    file_path = os.path.join(uploads_dir, file.filename)
    file.save(file_path)
    
    return 'File uploaded successfully', 200

if __name__ == '__main__':
    app.run(debug=True)