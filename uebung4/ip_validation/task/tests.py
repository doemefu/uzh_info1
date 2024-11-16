#!/usr/bin/env python3
from unittest import TestCase

from task import script

# You'll probably want to write at least two tests for each of the functions,
# one passing a valid and one passing an invalid value to confirm that each
# individual function works on its own.

# Here' we've already provided a few examples. You should be able to fill
# in the empty strings by yourself by studying the task description:

IPv4_OCTET = "255"
IPv4_OCTET_INVALID = "256"

IPv4 = ""                 # fill this in yourself
IPv4_INVALID = ""         # fill this in yourself

IPv6_HEXTET = "fff"
IPv6_HEXTET_INVALID = ""  # fill this in yourself

IPv6 = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
IPv6_INVALID = ""         # fill this in yourself

IP = "192.168.1.1"
IP_INVALID = "A string that is not a valid IP"


class TasksTestSuite(TestCase):

    # we already provide 2 tests for the first two examples (valid/invalid octet)
    def test_ipv4_octet_valid(self):
        actual = script.is_valid_IPv4_octet(IPv4_OCTET)
        self.assertEqual(actual, True)

    def test_ipv4_octet_invalid(self):
        actual = script.is_valid_IPv4_octet(IPv4_OCTET_INVALID)
        self.assertEqual(actual, False)

    # write more test cases, one for each of the examples above!

