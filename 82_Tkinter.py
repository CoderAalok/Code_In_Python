import tkinter as tk
from tkinter import messagebox
from cap import uservalidation

root = tk.Tk()

def login_setup():
    username = username_entry.get()
    password = password_entry.get()
    
    try:
        # check validation
        if uservalidation.valid_user(username, password):
            messagebox.showinfo("Account", "Login successful")
        else:
            messagebox.showerror("Error", "Invalid candentials!")
            
    except Exception as e:
        messagebox.showerror("System error", str(e))

root.geometry("800x600")
root.minsize(415, 500)
root.maxsize(725, 570)
#cornal side show up this litle widget
root.title("Chatty Account")

tk.Label(root, text="Username:").grid(row=2, column=0, padx=2, pady=1)
tk.Label(root, text="Password:").grid(row=3, column=0, padx=3, pady=4)

username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")

# input grid creates
username_entry.grid(row=2, column=5)
password_entry.grid(row=3, column=5)

# button creates
tk.Button(root, text="Login", command=login_setup).grid(row=12, column=5, padx=5, pady=7)

root.mainloop()

