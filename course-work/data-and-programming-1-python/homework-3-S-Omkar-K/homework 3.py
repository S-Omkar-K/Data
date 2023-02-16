# PPHA 30535
# Spring 2021
# Homework 3

# Sai Omkar Kandukuri

# Sai Omkar Kandukuri
# S-Omkar-K

# Due date: Sunday April 24th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

# Question 1: Begin with the class below and do the following:
#   a) Modify the what_to_watch method so that it takes an optional keyword
#       argument that allows the user to narrow down the random selection by
#       category (e.g. select only from movies with category 'action'), but
#       defaults to the entire list of titles as it does now.
#   b) The what_to_watch method currently raises a ValueError if you use it
#       before entering any movies. Modify it using try/except so that it tells
#       the user what they did wrong instead of raising an error.
#   c) Create a new class called InteractiveMovieDataBase that inherits MovieDataBase.
#   d) Override the add_movie method in your new class so that if it is called
#       without arguments, it instead asks for user input to add a title/year/
#       category/stars, but if it is called with arguments it behaves as before
#   e) Add some appropriate error checking to InteractiveMovieDatabase on the user 
#       input, so that they can't enter something that makes no sense (e.g. title=None
#       or year='dog')
#   f) Add a new method to InteractiveMovieDataBase named movie_rankings, which
#       returns a list of all the titles in the database currently, ordered
#       highest ranking (by stars) to lowest
#
# NOTE: Your final submission should have only TWO classes: one (modified)
#       MovieDataBase, and the new InteractiveMovieDataBase

#from numpy import random

import random

class MovieDataBase():
    def __init__(self):
        self.titles = []
        self.movies = {}

    def add_movie(self, title, year, category, stars):
        self.titles.append(title)
        self.movies[title] = {'year': year,
                              'category': category, 'stars': stars}
        print(f'{title} ({year}) added to the database.')

    def what_to_watch(self, category = None):
        titles = []
        if not category:
            titles = self.titles
        else:
            for title in self.movies.keys():
                if self.movies[title]['category'] == category:
                    titles.append(title)

        if not titles:
            print(f"Add movies having category {category} before proceeding.")
            return

        try:
            choice = random.choice(titles)
        except IndexError:
            print("Please add movies before proceeding.")
            return

        movie = self.movies[choice]
        print(
            f"Your movie today is {choice} ({movie['year']})," +
            f" which is a {movie['category']}, and was given " +
            f"{movie['stars']} stars.")


class InteractiveMovieDatabase(MovieDataBase):
    def add_movie(self, title=None, year=None, category=None, stars=None):
        while not title:
            title = input("Enter title: ")
            if title == '':
                title = None

        while not year:
            year = input("Enter year: ")
            try:
                year = int(year)
            except ValueError:
                print("year must be integer")
                year = None

        while not category:
            category = input("Enter category: ")
            if category == '':
                category = None

        while not stars:
            stars = input("Enter stars: ")
            try:
                stars = float(stars)
            except ValueError:
                print("stars must be integer or decimal")
                stars = None

        super().add_movie(title, year, category, stars)

    def movie_rankings(self):
        temp_titles = []
        for title in self.movies.keys():
            temp_titles.append([title, self.movies[title]['stars']])

        temp_titles = sorted(
            temp_titles, key=lambda item: item[1], reverse=True)

        titles = []
        for item in temp_titles:
            titles.append(item[0])

        return titles
 
    
# Test Cases
# Instantiate a new MovieDataBase
movie_db = MovieDataBase()
movie_db.what_to_watch()
movie_db.add_movie("RRR", 2022, "Fiction", 4.5)
movie_db.add_movie("Avengers", 2012, "Fiction", 5)
movie_db.what_to_watch("Fiction")

# Instantiate a new InteractiveMovieDatabase
imovie_db = InteractiveMovieDatabase()
imovie_db.add_movie("Avengers", 2012, "Fiction", 5)
imovie_db.add_movie("Kuch Kuch Hota Hai", 1999, "Rom-Com", 3.8)
imovie_db.add_movie("RRR", 2022, "Fiction", 4.5)
imovie_db.what_to_watch("Rom-Com")
print(imovie_db.movie_rankings())


