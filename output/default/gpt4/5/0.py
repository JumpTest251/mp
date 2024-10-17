import os
import subprocess

def list_directory_contents(directory_path):
    try:
        # Run the `ls` command in the specified directory
        result = subprocess.run(['ls', directory_path], capture_output=True, text=True, check=True)
        return result.stdout.strip().splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while listing directory: {e}")
        return []