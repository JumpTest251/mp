import json
import urllib.request as request
import tarfile
import os

def extract_tar_from_url(url, file_name):
    """
    Downloads a tar archive from the specified
    URL, extracts it and saves it to the
    current working directory with the
    specified file name.
    """
    # Download the tar file
    response = request.urlopen(url)
    tar_file_path = os.path.join(os.getcwd(), file_name)
    
    with open(tar_file_path, 'wb') as f:
        f.write(response.read())
    
    # Extract the tar file
    if tarfile.is_tarfile(tar_file_path):
        with tarfile.open(tar_file_path, 'r') as tar:
            tar.extractall(path=os.getcwd())
    else:
        print("The file downloaded is not a valid tar file.")
    
    # Clean up: remove the tar file after extraction
    if os.path.exists(tar_file_path):
        os.remove(tar_file_path)

# Example usage
if __name__ == "__main__":
    url = "http://example.com/path/to/archive.tar"
    file_name = "archive.tar"
    extract_tar_from_url(url, file_name)