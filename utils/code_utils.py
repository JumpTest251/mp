import os
import re

def remove_comments(code, language):
    if language == "python":
        return re.sub(r'(#.*|\'\'\'.*?\'\'\'|\"\"\".*?\"\"\")', '', code)
    else:
        return re.sub(r'(//.*|/\*.*?\*/)', '', code)

def write_to_file(location, filename, language, code_blocks):
    if not os.path.exists(location):
        os.makedirs(location)

    file_ending = "py" if language == "python" else "js"
    with open(f"{location}{filename}.{file_ending}", "w") as f:
        for code in code_blocks:
            f.write(code.strip())


