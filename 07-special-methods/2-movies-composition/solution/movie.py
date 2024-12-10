#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

class Movie:

    def __init__(self, title, actors, duration):
        if not title or not actors or duration < 1:
            raise Warning("Invalid parameters provided to __init__")
        self._title = title
        self._actors = actors
        self._duration = duration

    def __eq__(self, other):
        if not type(other) == Movie:
            return NotImplemented

        return self._title == other._title \
               and self._actors == other._actors \
               and self._duration == other._duration

    def __hash__(self):
        attrs = [self._title]
        attrs.extend(self._actors)
        attrs.append(self._duration)
        return hash(tuple(attrs))

    def __repr__(self):
        return 'Movie("{}", ["{}"], {})'.format(self._title, '", "'.join(self._actors), self._duration)

    def __lt__(self, other):
        if not isinstance(other, Movie):
            return NotImplemented
        return self._title < other._title

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return other < self

    def __ge__(self, other):
        return other < self or self == other

    def get_title(self):
        return self._title

    def get_actors(self):
        return self._actors[:] # clone

    def get_duration(self):
        return self._duration
