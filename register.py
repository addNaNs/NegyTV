import tkinter as tk
import main
import pickle
import functools

def create_account(username, name, surname, password, repeat_password):
    pass


root = tk.Tk()
root.geometry('400x150')
root.title('Create a new account')

username_label = tk.Label(root, text="Username").grid(row=0, column=0)
username_str = tk.StringVar()
username_entry = tk.Entry(root, textvariable=username_str).grid(row=0, column=1)

name_label = tk.Label(root, text="Name").grid(row=1, column=0)
name_str = tk.StringVar()
name_entry = tk.Entry(root, textvariable=name_str).grid(row=1, column=1)

surname_label = tk.Label(root, text="Surname").grid(row=2, column=0)
surname_str = tk.StringVar()
surname_entry = tk.Entry(root, textvariable=surname_label).grid(row=2, column=1)

password_label = tk.Label(root, text="Password").grid(row=3, column=0)
password_str = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_str, show='*').grid(row=3, column=1)

repeat_password_label = tk.Label(root, text="Repeat password").grid(row=4, column=0)
repeat_password_str = tk.StringVar()
repeat_password_entry = tk.Entry(root, textvariable=repeat_password_str, show='*').grid(row=4, column=1)


create_account_partial = functools.partial(create_account,
                                           username_str, name_str, surname_str, password_str, repeat_password_str)

login_btn = tk.Button(root, text="Create Account", command=create_account_partial).grid(row=5, column=0)
login_btn = tk.Button(root, text="Quit", command=root.quit).grid(row=5, column=2)

root.mainloop()
