#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

class Movie():

    def __init__(self, title, actors, duration):
        if not title or not actors or duration < 1:
            raise Warning
        self.__title = title
        self.__actors = actors
        self.__duration = duration

    def get_title(self):
        return self.__title

    def get_actors(self):
        return self.__actors.copy()

    def get_duration(self):
        return self.__duration

    # also implement the required special functions

    def __repr__(self):
        mystr = f"Movie(\"{self.__title}\", {self.__actors}, {self.__duration})"
        return str(mystr).replace("'", '"')

    def __eq__(self, other):
        return (repr(self)) == other

    def __hash__(self):
        return hash((self.__title, tuple(self.__actors), self.__duration))