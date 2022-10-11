# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 19:06:53 2022

@author: Bekhzod
"""

# def kopaytma(*sonlar):
#     """Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya"""
#     hisoblash = 1
#     for x in sonlar:
#         hisoblash = hisoblash * x
#     return hisoblash

# print(kopaytma(1,2,3,4))


def talabalar(ism,familiya,**malumotlar):
    malumotlar['Ismi'] = ism
    malumotlar['Famimliyasi'] = familiya
    return malumotlar

print(talabalar('Behzod','Muhammadaliyev', Department='IBT',Year='4th year', Course='AI'))