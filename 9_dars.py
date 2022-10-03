# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 16:11:12 2022

@author: Bekhzod
"""

# ismlar = ['Maruf','Farrux','Sardor','Jasur','Nodir']
# for x in ismlar:
#     print(f"Assalomu alaykum {x}.Yaxshimisiz? Bugun kechki payt 22:00 da futbol qilyapmiz. Kelasizmi?")
# print(f"Kod {len(ismlar)} marta takrorlandi")

# sonlar = list(range(11,100,2))
# for x in sonlar:
#     print(x**3)
    
# kinolar = []
# print('5 ta eng sevimli kinoyingiz nomini kiriting.')
# for x in range(5):
#     kinolar.append(input(f"{x+1}-eng sevimli kinoyingiz:"))
# print(kinolar)

odamlar = []
soni = int(input("Bugun nechta odam bilan suhbatlashdingiz?\n>>>"))
for n in range(soni):
    odamlar.append(input(f"{n+1}-suhbatdoshingizni ismi:"))
print(odamlar)
