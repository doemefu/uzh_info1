#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from task.movie import Movie


class MovieBox(Movie):
    def __init__(self, title, movies):
        if not title or not movies:
            raise Warning("Invalid parameters provided to __init__")
        self._title = title
        self._movies = movies

    def __eq__(self, other):
        if not isinstance(other, MovieBox):
            return NotImplemented

        return self._title == other._title and self._movies == other._movies

    def __hash__(self):
        attrs = [self._title]
        attrs.extend(self._movies)
        return hash(tuple(attrs))

    def __repr__(self):
        movies_as_str = [str(m) for m in self._movies]
        return 'MovieBox("{}", [{}])'.format(self._title, ", ".join(movies_as_str))

    def get_title(self):
        return self._title

    def get_actors(self):
        actors = []
        for m in self._movies:
            actors.extend(m.get_actors())
        return actors

    def get_duration(self):
        durations = [m.get_duration() for m in self.get_movies()]
        return sum(durations)

    def get_movies(self):
        return self._movies[:]
