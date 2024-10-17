import os

# Super secret info
secret_info = "This is some super secret information."

# File name
file_name = "secret_info.txt"

# Write the secret info to the file
with open(file_name, 'w') as file:
    file.write(secret_info)

# Change the file permissions to read-only for the owner
os.chmod(file_name, 0o400)  # Owner can read, no permissions for group and others

# Print the name of the file
print(file_name)