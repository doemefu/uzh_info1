#!/usr/bin/env python3

from unittest import TestCase
from script import factorial


class PublicTestSuite(TestCase):

    def test1(self):
         self.assertEqual(120, factorial(5))

    def test2(self):
        a = 8*7*6*5*4*3*2*1
        self.assertEqual(a, factorial(8))
