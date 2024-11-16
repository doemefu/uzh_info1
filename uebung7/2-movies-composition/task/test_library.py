#!/usr/bin/env python3

from unittest import TestCase
from movie import Movie
from moviebox import MovieBox
from library import Library


class LibraryTest(TestCase):
    def test_repr_movie(self):
        actual = repr(Movie("T", ["A", "B"], 123))
        expected = 'Movie("T", ["A", "B"], 123)'
        self.assertEqual(expected, actual)

    def test_repr_moviebox(self):
        actual = repr(MovieBox("T", [Movie("T2", ["A", "B"], 234)]))
        expected = 'MovieBox("T", [Movie("T2", ["A", "B"], 234)])'
        self.assertEqual(expected, actual)

    def test_library(self):
        a = Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        b = Movie("The Godfather", ["Brando", "Pacino"], 175)
        c = Movie("12 Angry Men", ["Fonda", "Cobb"], 96)
        y = Movie("Angry Men", ["Haus", "Thun"], 400)
        z = Movie("12 Men", ["Auto", "Cobb"], 1)

        d = MovieBox("Top Movies", [a, b])
        e = MovieBox("Top filmli", [b, c, d])
        g = MovieBox("Top moviiez", [y, z, e])

        l = Library()
        l.add_movie(d)
        l.add_movie(e)
        l.add_movie(g)

        expected_movies = [
            Movie("12 Angry Men", ["Fonda", "Cobb"], 96),
            Movie("12 Men", ["Auto", "Cobb"], 1),
            Movie("Angry Men", ["Haus", "Thun"], 400),
            Movie("The Godfather", ["Brando", "Pacino"], 175),
            Movie("The Shawshank Redemption", ["Robbins", "Freeman"], 142)
        ]

        self.assertEqual(l.get_movies(), expected_movies,
                         "The list of movies should be unique and sorted alphabetically.")

    # This current test suite only contains very basic test cases. By now,
    # you have some experience in writing test cases. We strongly encourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
