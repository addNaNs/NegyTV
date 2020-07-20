import tkinter as tk
import pickle
import functools
import main
from main import User
from main import Gym
import os


root = tk.Tk()
root.title('Account setup')

setup_welcome_string = "Hi! We need you to enter a few movies you've watched, so we can give you the best experience"
setup_welcome_label = tk.Label(root, text=setup_welcome_string).grid(row=0, column=0, columnspan=6)

setup_instructions_string = "Please rate the movies you have watched, and skip the ones you haven't"
setup_instructions_label = tk.Label(root, text=setup_instructions_string).grid(row=1, column=0, columnspan=6)

trained_model = pickle.load(open('gym.obj', 'rb'))
most_viewed = trained_model.most_viewed()

movie_label = tk.Label(root, text=most_viewed[0][1]).grid(row=2, column=0, columnspan=6)

rate_1_star_btn = tk.Button(root, text='1 star').grid(row=4, column=0)
rate_2_star_btn = tk.Button(root, text='2 star').grid(row=4, column=1)
rate_3_star_btn = tk.Button(root, text='3 star').grid(row=4, column=2)
rate_4_star_btn = tk.Button(root, text='4 star').grid(row=4, column=3)
rate_5_star_btn = tk.Button(root, text='5 star').grid(row=4, column=4)
not_watched_btn = tk.Button(root, text='Did not watch').grid(row=4, column=5)

root.mainloop()
