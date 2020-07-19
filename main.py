import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import tkinter


class Gym:
    num_users = -1
    num_movies = -1
    num_features = -1

    user_features = None
    movie_features = None

    ratings = None
    mean_ratings = None
    has_rated = None
    userwise_rated_movies = None
    moviewise_rated_movies = None
    total_rated_movies = None

    titles = None

    __du_old__ = None
    __dm_old__ = None

    def __init__(self, ratings, num_features, titles):
        self.ratings = ratings
        self.has_rated = np.sign(ratings)
        self.num_features = num_features
        self.userwise_rated_movies = self.has_rated.sum(axis=1)
        self.moviewise_rated_movies = self.has_rated.sum(axis=0)
        self.total_rated_movies = self.userwise_rated_movies.sum()
        self.titles = titles

        self.num_users, self.num_movies = ratings.shape
        self.user_features = np.random.randn(self.num_users, num_features)
        self.movie_features = np.random.randn(self.num_movies, num_features)

        self.mean_ratings = ratings.sum(axis=0) / self.has_rated.sum(axis=0).clip(min=1)
        self.ratings = (self.ratings - self.mean_ratings) * self.has_rated

    def print_all(self):
        print('num_users :', self.num_users)
        print('num_movies :', self.num_movies)
        print('num_features :', self.num_features)

        print('user_features :\n', self.user_features)
        print('movie_features :\n', self.movie_features)

        print('mean_ratings :\n', self.mean_ratings)
        print('ratings :\n', self.ratings)
        print('has_rated :\n', self.has_rated)
        print('userwise_rated_movies :\n', self.userwise_rated_movies)
        print('moviewise_rated_movies :\n', self.moviewise_rated_movies)
        print('total_rated_movies :\n', self.total_rated_movies)

    def get_cost_elementwise(self):
        return (((self.user_features.dot(self.movie_features.T) - self.ratings)
                 * self.has_rated) ** 2 / (self.total_rated_movies) * 2)

    def get_cost(self):
        return self.get_cost_elementwise().sum()

    def get_user_feature_gradient(self):
        return ((self.user_features.dot(self.movie_features.T) * self.has_rated - self.ratings)
                * self.has_rated).dot(self.movie_features)

    def get_movie_feature_gradient(self):
        return ((self.user_features.dot(self.movie_features.T) * self.has_rated - self.ratings)
                * self.has_rated).T.dot(self.user_features)

    def get_gradients(self):
        return self.get_user_feature_gradient(), self.get_movie_feature_gradient()

    def gradient_step(self, alpha=0.00015, beta=0.9):

        du, dm = self.get_gradients()
        du = beta * self.__du_old__ + (1 - beta) * du
        dm = beta * self.__dm_old__ + (1 - beta) * dm
        self.user_features = self.user_features - du * alpha
        self.movie_features = self.movie_features - dm * alpha
        self.__du_old__ = du
        self.__dm_old__ = dm

    def gradient_descent(self, epochs=100, alpha=0.00015, beta=0.9):
        costs = [self.get_cost()]
        self.__du_old__ = 0
        self.__dm_old__ = 0
        for i in range(epochs):
            self.gradient_step(alpha, beta)
            costs.append(self.get_cost())
            print(self.get_cost())
        plt.plot(range(epochs + 1), costs)

    def predict(self, sur, num_it=500):
        suf = np.random.randn(1, self.num_features)
        suhr = np.sign(sur)
        sutrm = suhr.sum()
        sur = sur - self.mean_ratings * suhr
        for i in range(num_it):
            sufg = ((suf.dot(self.movie_features.T) * suhr - sur)
                    * suhr).dot(self.movie_features)
            suf = suf - sufg * 0.0015
            if i % 50 == 0:
                print((((suf.dot(self.movie_features.T) - sur)
                        * suhr) ** 2 / (sutrm) * 2).sum())
        return suf.dot(self.movie_features.T) + self.mean_ratings

    def recommend(self, user):
        sur = user.ratings
        preds = list(self.predict(sur, 5000).flatten())
        suhr = list(np.sign(sur))
        recommends = list(zip(self.titles, preds, suhr))
        recommends.sort(key=lambda arg: -arg[1])
        return recommends


class User:
    name = None
    surname = None
    username = None
    __password__ = None
    ratings = None

    def __init__(self, username, name, surname, password, ratings=None):
        self.username = username
        self.name = name
        self.surname = surname
        self.__password__ = password
        self.ratings = ratings


if __name__ == '__main__':
    trained_model = pickle.load(open('gym.obj', 'rb'))
    all_users = None
    try:
        all_users = pickle.load(open('./users.obj', 'rb'))
    except FileNotFoundError:
        all_users = list()

    pickle.dump(all_users, open('./users.obj', 'wb'))

    import login as login
    print(login.index)
    print("HI!")




