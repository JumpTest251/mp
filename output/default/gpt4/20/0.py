import tarfile
import os

# Define the path to the zip file and the extraction directory
zip_file_path = 'archive.zip'
extraction_directory = '/tmp/unpack'

# Make sure the extraction directory exists
os.makedirs(extraction_directory, exist_ok=True)

# Open the zip file as a tarfile and extract all files
with tarfile.open(zip_file_path, 'r:zip') as tar:
    tar.extractall(path=extraction_directory)