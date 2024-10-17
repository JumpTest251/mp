import tarfile
import os

def unpack_tar_archive(tar_path, extract_to="/tmp/unpack"):
    """Unpack a tar archive to the specified directory."""
    # Ensure the extract directory exists
    os.makedirs(extract_to, exist_ok=True)

    with tarfile.open(tar_path, "r:*") as tar:
        tar.extractall(path=extract_to)
        print(f"Extracted {tar_path} to {extract_to}")

# Example usage
tar_file_path = "path_to_your_archive.tar.gz"
unpack_tar_archive(tar_file_path)