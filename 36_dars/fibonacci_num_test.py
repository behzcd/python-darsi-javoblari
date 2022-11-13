# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 02:52:21 2022

@author: Bekhzod
"""

import unittest
from fibonacci_num import fibonacci

class fibonacciTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(fibonacci(89))
        self.assertTrue(fibonacci(610))

unittest.main()
