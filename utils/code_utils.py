import os

def write_to_file(location, filename, code_blocks):
    if not os.path.exists(location):
        os.makedirs(location)

    with open(f"{location}{filename}", "w") as f:
        for code in code_blocks:
            f.write(code.strip())