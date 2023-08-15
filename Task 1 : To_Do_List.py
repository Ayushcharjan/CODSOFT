#Codsoft task "To-Do List"

import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_tasks():
    task_listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create GUI components
task_entry = tk.Entry(root, width=30)
add_button = tk.Button(root, text="Add Task", command=add_task, bg="#3697f5")
remove_button = tk.Button(root, text="Remove Task", command=remove_task, bg="#97f536")
clear_button = tk.Button(root, text="Clear All", command=clear_tasks, bg="#f59436")
task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)

# Place components on the window
task_entry.pack(pady=10)
add_button.pack()
remove_button.pack()
clear_button.pack()
task_listbox.pack()

# Start the main event loop
root.mainloop()
