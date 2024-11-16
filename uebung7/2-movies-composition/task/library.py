#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from movie import Movie
from moviebox import MovieBox


class Library:

    def __init__(self):
        self.__my_movies = []

    def add_movie(self, movie):
        if movie not in self.__my_movies:
            self.__my_movies.append(movie)
        self.__my_movies.sort(key=lambda movie: movie.get_title())

    def get_movies(self):
        movies = []
        for item in self.__my_movies:
            movies += self.checker(item)

        print(movies)
        movies = list(set(movies))
        movies.sort(key=lambda movie: movie.get_title())

        return movies

    def checker(self, item):
        if isinstance(item, MovieBox):
            return_list = []
            for element in item.get_movies():
                return_list += self.checker(element)
            return return_list
        elif isinstance(item, Movie):
            return [item]

    def get_total_duration(self):
        return sum([movie.get_duration() for movie in self.__my_movies])
