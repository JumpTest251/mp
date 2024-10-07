import zipfile
import os

# Define the path to the zip file and the output directory
zip_file_path = 'archive.zip'
output_dir = '/tmp/unpack'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Open the zip file and extract all its contents
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(output_dir)