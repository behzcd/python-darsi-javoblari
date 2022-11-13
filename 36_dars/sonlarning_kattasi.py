# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 01:15:23 2022

@author: Bekhzod
"""

def sonlarning_kattasi(x,y,z):
    if x>y and x>z:
        kattasi = x
    elif y>z and y>x:
        kattasi = y
    else:
        kattasi = z
    return kattasi
    