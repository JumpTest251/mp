import os

# Create and write to the file
with open('secret.txt', 'w') as file:
    file.write('U2FsdGVkX1/R+WzJcxgvX/Iw==')

# Change the permissions of the file to be restrictive
os.chmod('secret.txt', 0o600)  # Owner can read and write, group and others have no permissions