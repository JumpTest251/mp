import os

# Create and write to the file
with open('secret.txt', 'w') as file:
    file.write('U2FsdGVkX1/R+WzJcxgvX/Iw==')

# Change the permissions of the file to 128 (0o200 in octal)
os.chmod('secret.txt', 0o200)

# Print the permissions of the file
permissions = oct(os.stat('secret.txt').st_mode & 0o777)
print(permissions)