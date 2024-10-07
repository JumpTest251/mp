import tarfile

# Using the with statement to create a tar archive
with tarfile.open('example.tar.gz', 'w:gz') as tar:
    # Adding a file to the archive
    tar.add('file_to_add.txt', arcname='file_in_archive.txt')

# Using the with statement to read from a tar archive
with tarfile.open('example.tar.gz', 'r:gz') as tar:
    tar.extractall(path='extracted_files')  # Extract all contents to a directory