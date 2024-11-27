#!/usr/bin/env python3
from unittest import TestCase
import task.script as script

class MyTestSuite(TestCase):

    def test_add_stock(self):
        warehouse = {"Phone": 12}
        script.add_stock(warehouse, "Phone")
        self.assertEqual(warehouse["Phone"], 13)

    # Note that you can copy paste the function above and rewrite it to test
    # your other functions!

