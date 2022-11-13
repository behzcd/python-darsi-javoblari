# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 01:30:02 2022

@author: Bekhzod
"""

import unittest
from sonlarning_kattasi import sonlarning_kattasi

class KattaSonTest(unittest.TestCase):
    def test_kattaSon(self):
        formatted_son = sonlarning_kattasi(12,-7366.836734,12.01)
        self.assertEqual(formatted_son,12.01)
        
unittest.main()