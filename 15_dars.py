# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 17:28:57 2022

@author: Bekhzod
"""

# lugat = {
#     'integer':'butun son',
#     'float':"o'nlik son",
#     'string':'matn',
#     'if':'agar',
#     'else':'aks holda',
#     'parenthesis':'qavs',
#     'list':"ro'yxat",
#     'del':"o'chirish",
#     'remove':'olib tashlash',
#     'variable':"o'zgaruvchi",
#     'dictionary':"lug'at"
#     }
# for x,y in sorted(lugat.items()):
#     print(f"{x.title()} - {y}")

davlatlar = {
    'Uzbekistan':'Tashkent',
    'S.Korea':'Seoul',
    'USA':'Washington',
    'Russia':'Moscow',
    'Turkey':'Instanbul',
    'France':'Paris',
    'Germany':'Berlin',
    'China':'Beijing',
    'Finland':'Helsinki',
    'India':'New Delhi',
    }
# print('\nWorld countries:\n')
# for x in sorted(davlatlar.keys()):
#     print(x.upper())
# print('\nCapital cities of those Countries:\n')
# for y in sorted(davlatlar.values()):
#     print(y)
    
# davlat = input("Istalgan bir davlat nomini kiriting: ").title()
# if davlat in davlatlar:
#     print(f"Bu davlatning poytaxti {davlatlar[davlat]}")
# else:
#     print("Bizda bunday ma'lumot yo'q")

menu = {
        'shashlik':20000,
        'qozonkabob':15000,
        'osh':22000,
        'manti':18000,
        'chuchvara':18000,
        "lag'mon":17000,
        'mastava':15000,
        'norin':20000,
        'somsa':10000,
        'shorva':15000,
        }
buyurtma = []
print('Uchta ovqat buyurtma bering.')
for y in range(3):
    buyurtma.append(input(f"{y+1}-ovqatni kiriting: ").lower())

for x in buyurtma:
    if x in menu:
        print(f"{x.title()}ning narxi {menu[x]} so'm")
    else:
        print(f"Uzur, bizda {x.title()} yo'q edi")