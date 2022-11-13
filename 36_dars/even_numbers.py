# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 02:09:15 2022

@author: Bekhzod
"""

def even_numbers(x):
    even_nums = []
    for n in x:
        if n%2 == 0:
            even_nums.append(n)
    print(even_nums)
