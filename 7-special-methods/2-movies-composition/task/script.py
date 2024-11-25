#!/usr/bin/env python3

# The purpose of this file is illustrating the class usages. This script
# is irrelevant for the grading and you can freely change its contents.

from movie import Movie
from moviebox import MovieBox
from library import Library

a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
b = Movie("The Godfather", ["Brando", "Pacino"], 175)
c = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
y = Movie("xx hello", ["me", "you"], 67)
d = MovieBox("Top Movies", [a,b, c])
e = MovieBox("Baba films", [a,c,d,y])

l = Library()
l.add_movie(a)
l.add_movie(d)
l.add_movie(e)

#print(a)
print(e)

print(l.get_movies())
print(l.get_total_duration())

#print(repr(Movie("T", ["A", "B"], 123)) == 'Movie("T", ["A", "B"], 123)')
#print(repr(MovieBox("T2", [Movie("T", ["A", "B"], 123)]) == 'MovieBox("T2", [Movie("T", ["A", "B"], 123)])'))

print(e.get_movies())
