# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 19:55:32 2022

@author: Bekhzod
"""

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for x in cars:
#     if x == 'gm':
#         print(x.upper())
#     else:
#         print(x.title())

# for n in cars:
#     if n != 'gm':
#         print(n.title())
#     else:
#         print(n.upper())

# login = input("Iltimos, loginingizni kiriting:")
# if login.lower() == 'admin':
#     print(f"Hush kelibsiz, {login.title()}. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Hush kelibsiz,{login.title()}!")
    
# print('Iltimos ikkita son kiriting:')
# son1 = float(input('Birinchi sonni kiriting:'))
# son2 = float(input('Ikkinchi sonni kiriting:'))
# if son1 == son2:
#     print('Sonlar teng ekan')
# else:
#     print('Ajoyib')

# son = float(input('Istangan sonni kiriting:'))
# if son>0:
#     print('Musbat son')
# elif son<0:
#     print('Manfiy son')
# else:
#     print('0 musbat son ham manfiy son ham emas')

import math
son = float(input('Iltimos biror son kiriting:'))
if son>0:
    print(f"Bu sonning ildizi {math.sqrt(son)} ga teng")
elif son<0:
    print('Iltimos musbat son kiriting!')
else:
    print('0 ildizga ega emas')
    