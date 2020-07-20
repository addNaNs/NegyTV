import tkinter as tk
import pickle
import numpy as np
import functools
import main
from main import User
from main import Gym
import os
import functools


def not_watched(text_var):
    next_movie(text_var)


def next_movie(text_var):
    global movie_index
    movie_index += 1
    text_var.set(most_viewed[movie_index][1])


def rate(text_var, stars):
    global setup_ratings
    global most_viewed
    global movie_index
    setup_ratings[most_viewed[movie_index][0]] = stars
    next_movie(text_var)


root = tk.Tk()
root.title('Account setup')

setup_welcome_string = "Hi! We need you to enter a few movies you've watched, so we can give you the best experience"
setup_welcome_label = tk.Label(root, text=setup_welcome_string).grid(row=0, column=0, columnspan=6)

setup_instructions_string = "Please rate the movies you have watched, and skip the ones you haven't"
setup_instructions_label = tk.Label(root, text=setup_instructions_string).grid(row=1, column=0, columnspan=6)

trained_model = pickle.load(open('gym.obj', 'rb'))
most_viewed = trained_model.most_viewed()
setup_ratings = np.zeros(trained_model.num_movies)

movie_index = 0
movie_str = tk.StringVar(root, most_viewed[movie_index][1])
movie_label = tk.Label(root, textvariable=movie_str).grid(row=2, column=0, columnspan=6)

not_watched_partial = functools.partial(not_watched, movie_str)
rate_1_partial = functools.partial(rate, movie_str, 1)
rate_2_partial = functools.partial(rate, movie_str, 2)
rate_3_partial = functools.partial(rate, movie_str, 3)
rate_4_partial = functools.partial(rate, movie_str, 4)
rate_5_partial = functools.partial(rate, movie_str, 5)

rate_1_star_btn = tk.Button(root, text='1 star', command=rate_1_partial).grid(row=4, column=0)
rate_2_star_btn = tk.Button(root, text='2 star', command=rate_2_partial).grid(row=4, column=1)
rate_3_star_btn = tk.Button(root, text='3 star', command=rate_3_partial).grid(row=4, column=2)
rate_4_star_btn = tk.Button(root, text='4 star', command=rate_4_partial).grid(row=4, column=3)
rate_5_star_btn = tk.Button(root, text='5 star', command=rate_5_partial).grid(row=4, column=4)
not_watched_btn = tk.Button(root, text='Did not watch', command=not_watched_partial).grid(row=4, column=5)

root.mainloop()
