import tarfile
import os

# Define the archive and the extraction directory
archive_path = 'archive.zip'
extraction_path = '/tmp/unpack'

# Create the extraction directory if it does not exist
os.makedirs(extraction_path, exist_ok=True)

# Open the archive and extract all files
with tarfile.open(archive_path, 'r:*') as archive:
    archive.extractall(path=extraction_path)