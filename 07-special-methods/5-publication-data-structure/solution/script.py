#!/usr/bin/env python3

class Publication:

    def __init__(self, authors, title, year):
        self.__authors = authors
        self.__title = title
        self.__year = year

    def get_authors(self):
        return self.__authors[:]

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    def __hash__(self):
        keys = self.__authors[:]
        keys.append(self.__title)
        keys.append(self.__year)
        return hash(tuple(keys))

    def __eq__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        else:
            return self.__authors == other.__authors \
                   and self.__title == other.__title \
                   and self.__year == other.__year

    def __lt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        if self.__authors < other.__authors:
            return True
        elif self.__authors == other.__authors:
            if self.__title < other.__title:
                return True
            elif self.__title == other.__title:
                return self.__year < other.__year
        return False

    def __le__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return self < other or self == other

    def __gt__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return other < self

    def __ge__(self, other):
        if not isinstance(other, Publication):
            return NotImplemented
        return other <= self

    def __repr__(self):
        return "Publication([\"{}\"], \"{}\", {})".format("\", \"".join(self.__authors), self.__title, self.__year)
