#!/usr/bin/env python3
from unittest import TestCase

from script import BankAccount


class PublicTestSuite(TestCase):

    def test_str_method(self):
        account = BankAccount("Melon Tusk", 269800000000.0)
        expected_str = "Account owner: Melon Tusk\nAccount balance: CHF 269800000000.0"
        self.assertEqual(str(account), expected_str,
                         msg=f"__str__ method should return 'Account owner: Melon Tusk\nAccount balance: CHF 269800000000.0' but returned {str(account)}")

