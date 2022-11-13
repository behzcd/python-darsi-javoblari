# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 02:00:40 2022

@author: Bekhzod
"""

import unittest
from list_title import text_title

class List_Title_Test(unittest.TestCase):
    def test_listTitle(self):
        x = ['salom, mening ismim Behzod','men hozirda Koreyadaman','sening isming nima?']
        formatted_list = text_title(x)
        output_list = ['Salom, Mening Ismim Behzod','Men Hozirda Koreyadaman','Sening Isming Nima?']
        self.assertEqual(formatted_list,output_list)

unittest.main()
