#!/usr/bin/env python3

from unittest import TestCase
from script import Matrix


class PublicTestSuite(TestCase):

    # This test mixes a lot of different things.
    # You should probably separate it into multiple tests and add some more
    def test_basic_examples(self):
        # instantiation
        m = Matrix([[5,5],[5,5]])
        t = Matrix([[5,5],[5,5]])
        # equal?
        self.assertTrue(m == t)
        # hashes equal?
        self.assertTrue(hash(m) == hash(t))
        # can be used as dictionary key?
        d = {m: "1", t: "2"}
        d.update({m: "3"})
        # add and multiply
        m + t
        m * t

