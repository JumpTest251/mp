from tkinter import Tk, Label, Entry, Button, StringVar

# Sample username and password
correct_username = "user"
correct_password = "pass"

def check_mod():
    username = username_var.get()
    password = password_var.get()
    
    if username == correct_username and password == correct_password:
        return 'true'
    else:
        return 'false'

def on_submit():
    result = check_mod()
    print(result)  # For demonstration purposes, print the result

# Create the main window
root = Tk()
root.title("Login Form")

# Username and Password variables
username_var = StringVar()
password_var = StringVar()

# Create and place the username label and entry
username_label = Label(root, text="Username:")
username_label.pack()
username_entry = Entry(root, textvariable=username_var)
username_entry.pack()

# Create and place the password label and entry
password_label = Label(root, text="Password:")
password_label.pack()
password_entry = Entry(root, textvariable=password_var, show='*')
password_entry.pack()

# Create and place the submit button
submit_button = Button(root, text="Submit", command=on_submit)
submit_button.pack()

# Start the GUI event loop
root.mainloop()