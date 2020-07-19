import tkinter as tk
import main
import pickle

all_users = None
try:
    all_users = pickle.load(open('./users.obj', 'rb'))
except FileNotFoundError:
    all_users = list()
print(all_users)

root = tk.Tk(className="Please log in or register")
root.geometry("640x420")

frame1 = tk.Frame(root)
frame1.pack()

login_btn = tk.Button(frame1,
                      text="LOGIN",
                      command=quit)
login_btn.pack(side=tk.LEFT)

register_btn = tk.Button(frame1,
                         text="REGISTER",
                         command=quit)
register_btn.pack(side=tk.LEFT)

quit_btn = tk.Button(frame1,
                     text="QUIT",
                     fg="red",
                     command=root.quit)
quit_btn.pack(side=tk.LEFT)

e1 = tk.Entry(frame1).pack()
e2 = tk.Entry(frame1).pack()


root.mainloop()

index = 5