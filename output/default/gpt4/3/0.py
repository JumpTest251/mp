import os

def read_file(filename):
    file_path = os.path.join('files', filename)
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"File '{filename}' not found in '/files/' directory."
    except Exception as e:
        return f"An error occurred: {e}"