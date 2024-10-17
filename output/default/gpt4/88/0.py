import os
import stat

# Create and write to the file
with open('secret.txt', 'w') as file:
    file.write('U2FsdGVkX1/R+WzJcxgvX/Iw==')

# Change the permissions to restrictive (e.g., read/write for owner only)
os.chmod('secret.txt', stat.S_IRUSR | stat.S_IWUSR)

# Print the permissions of the file
permissions = oct(os.stat('secret.txt').st_mode)[-3:]
print(f'Permissions of secret.txt: {permissions}')