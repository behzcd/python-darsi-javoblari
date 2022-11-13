# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 02:26:44 2022

@author: Bekhzod
"""

import unittest
from even_numbers import even_numbers

class evenNumTest(unittest.TestCase):
    def numTest(self):
        formatted_list = even_numbers([474,587,37,4,847,85,858786])
        self.assertEqual(formatted_list, [474,4,8858786])
        
unittest.main()