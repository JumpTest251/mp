import tarfile
import os

# Define the path to the archive and the unpack directory
archive_path = 'archive.zip'
unpack_dir = '/tmp/unpack'

# Create the unpack directory if it doesn't exist
os.makedirs(unpack_dir, exist_ok=True)

# Open the archive file and extract its contents
with tarfile.open(archive_path, 'r') as archive:
    archive.extractall(unpack_dir)