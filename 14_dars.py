# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 15:50:12 2022

@author: Bekhzod
"""

# otam = {'ismi':'alisher','yili':1973,'joyi':'namangan','kasbi':'haydovchi'}
# print(f"Otamning ismi {otam['ismi'].title()},{otam['yili']}-yili {otam['joyi'].title()}da tug'ilgan. Kasbi {otam['kasbi']}lik.")

# taom = {
#         'alisher':'osh',
#         'munavvar':'mastava',
#         'umidjon':'manti',
#         'behzod':'moshxorda',
#         'mohichehra':'shavla'
#         }
# print(f"Alisherning sevimli taomi {taom['alisher']},\
#       \nUmidjonning sevimli taomi {taom['umidjon']},\
#          \nMohichehraning sevimli taomi {taom['mohichehra']}.")

lugat = {
    'integer':'butun son',
    'float':"o'nlik son",
    'string':'matn',
    'if':'agar',
    'else':'aks holda',
    'parenthesis':'qavs',
    'list':"ro'yxat",
    'del':"o'chirish",
    'remove':'olib tashlash',
    'variable':"o'zgaruvchi",
    'dictionary':"lug'at"
    }
soz = input("Biror so'z kiriting:")

# print(lugat.get(soz, "Bunday so'z mavjud emas"))

if soz in lugat:
    print(f"'{soz}' so'zining tarjimasi - {lugat[soz]}")
else:
    print("Kechirasiz lug'atda bunday so'z mavjud emas")
    

