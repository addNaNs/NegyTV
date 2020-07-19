import tkinter as tk
import main
import pickle
import functools
import os

index = None


def validate_login(username, password):
    global index
    print("username entered :", username.get())
    print("password entered :", password.get())
    all_users = pickle.load(open('./users.obj', 'rb'))
    for i, user in enumerate(all_users):
        if user.validate(username.get(), password.get()):
            index = i
            return i
    return None


def register():
    os.system('python register.py')


root = tk.Tk()
root.geometry('400x150')
root.title('Please login or register')

username_label = tk.Label(root, text="Username").grid(row=0, column=0)
username_str = tk.StringVar()
username_entry = tk.Entry(root, textvariable=username_str).grid(row=0, column=1)

password_label = tk.Label(root, text="Password").grid(row=1, column=0)
password_str = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_str, show='*').grid(row=1, column=1)

validate_login_partial = functools.partial(validate_login, username_str, password_str)

login_btn = tk.Button(root, text="Login", command=validate_login_partial).grid(row=4, column=0)
login_btn = tk.Button(root, text="Register", command=register).grid(row=4, column=1)
login_btn = tk.Button(root, text="Quit", command=quit).grid(row=4, column=2)

root.mainloop()
