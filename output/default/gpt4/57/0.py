import os
import stat

# Step 1: Create a string with super secret info
super_secret_info = "This is some super secret information."

# Step 2: Create a file and write the super secret info to it
file_name = "super_secret_info.txt"
with open(file_name, 'w') as file:
    file.write(super_secret_info)

# Step 3: Change the permissions of the file to read-only for the owner
os.chmod(file_name, stat.S_IRUSR)

# Step 4: Print the name of the file to the screen
print(file_name)