import tkinter as tk
import pickle
import functools
import main
from main import User
import os


def create_account(username, name, surname, password, repeat_password):
    if password.get() != repeat_password.get():
        print("Not matching passwords")
        return
    all_users = pickle.load(open('./users.obj', 'rb'))
    for i, user in enumerate(all_users):
        if user.username == username.get():
            print("Username is taken")
            return
    all_users.append(main.User(username.get(), name.get(), surname.get(), password.get()))
    pickle.dump(all_users, open('./users.obj', 'wb'))
    print("Account created successfully")


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
quit_btn = tk.Button(root, text="Quit", command=root.quit).grid(row=5, column=2)

root.mainloop()
