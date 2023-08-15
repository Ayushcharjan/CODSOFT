#Codsoft task "Password Generator"

import tkinter as tk
import random
import string


def generate_password():
    password_length = int(length_entry.get())

    if password_length < 8:
        password_label.config(text="Password length should be at least 8 characters.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_label.config(text="Generated Password: " + password)


# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create GUI components
length_label = tk.Label(root, text="Password Length:")
length_entry = tk.Entry(root)
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#f59436")
password_label = tk.Label(root, text="Generated Password will appear here.")

# Place components on the window
length_label.pack(pady=10)
length_entry.pack()
generate_button.pack(pady=5)
password_label.pack(pady=10)

# Start the main event loop
root.mainloop()
