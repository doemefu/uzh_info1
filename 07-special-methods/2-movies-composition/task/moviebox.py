#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from movie import Movie


class MovieBox(Movie):

    def __init__(self, title, movies):
        if not movies or not title:
            raise Warning
        for movie in movies:
            if  not isinstance(movie, Movie):
                raise Warning

        self.__title = title
        self.__movies = movies #list
        self.__movies.sort(key=lambda movie: movie.get_title())


    def get_title(self):
        return self.__title

    def get_actors(self):
        __actors = set()
        for movie in self.__movies:
            __actors.update(movie.get_actors())
        return sorted(__actors)

    def get_duration(self):
        return sum([movie.get_duration() for movie in self.__movies])

    def get_movies(self):
        return self.__movies.copy()

    # also implement the required special functions
    def __repr__(self):
        return f"MovieBox(\"{self.__title}\", {self.__movies})"

    def __eq__(self, other):
        return (repr(self)) == other

    def __hash__(self):
        return hash((self.__title, tuple(self.__movies)))