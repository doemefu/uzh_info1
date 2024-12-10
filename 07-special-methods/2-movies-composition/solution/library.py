#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from task.movie import Movie
from task.moviebox import MovieBox


class Library:
    def __init__(self):
        self._movies = []

    def add_movie(self, movie):
        if movie not in self._movies:
            self._movies.append(movie)

    def get_movies(self):
        movies = []
        for m in self._movies:
            movies.extend(self._expand(m))
        # easiest solution seems to make movies comparable
        return sorted(movies)

    def _expand(self, movie):
        res = []
        if type(movie) == Movie:
            res.append(movie)
        elif type(movie) == MovieBox:
            for m in movie.get_movies():
                res.extend(self._expand(m))
        else:
            raise NotImplementedError()
        return res

    def get_total_duration(self):
        durations = [m.get_duration() for m in self._movies]
        return sum(durations)
