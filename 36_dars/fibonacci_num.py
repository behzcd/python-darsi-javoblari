# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 02:31:43 2022

@author: Bekhzod
"""

def fibonacci(n):
    sonlar = []
    for x in range(n+1):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x - 1] + sonlar[x - 2])
    if n in sonlar:
        return True
    else:
        return False