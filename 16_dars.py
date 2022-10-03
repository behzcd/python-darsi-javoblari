# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 21:59:40 2022

@author: Bekhzod
"""

# name1 = {
#     'ismi':'Bill Gates',
#     'yili':1955,
#     'joyi':'Seattle, USA',
#     'boyligi':'$132 billion'
#     }
# name2 = {
#     'ismi':'Elon Musk',
#     'yili':1971,
#     'joyi':'Pretoria, S.Africa',
#     'boyligi':'$264 billion'
#     }
# name3 = {
#     'ismi':'Jeff Bezos',
#     'yili':1964,
#     'joyi':'Albuquerque, USA',
#     'boyligi':'$183 billion'
#     }
# name4 = {
#     'ismi':'Warren Buffett',
#     'yili':1930,
#     'joyi':'Omaha, USA',
#     'boyligi':'$113 billion'
#     }

# people = [name1,name2,name3,name4]
# # for x in people:
# #     print(f"{x['ismi']} {x['yili']}-yili {x['joyi']} da tug'ulgan. Uning boyligi {x['boyligi']}.")


# people[0]['occup']='Software developer'
# people[1]['occup']='Engineer'
# people[2]['occup']='Entrepreneur'
# people[3]['occup']='Businessman'

# for y in people:
#     print(f"{y['ismi']}ning asil kasbi {y['occup']}.")


# kinolar = {
#     'Farrux':['Fall','Inception','Interstellar'],
#     'Sardor':['Avengers','Joker','Prison Break'],
#     'Maruf':['Mad Max','X-men','Gone girl'],
#     'Bek':['Harry Potter','The Hobbit','Who Am I']
#     }

# for ism,kino in kinolar.items():
#     print(f"\n{ism}ning sevimli kinolari: ", end = '')
#     for x in kino:
#         print(f"{x}, ", end = '')

davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }

# for davlat, info in davlatlar.items(): 
#     print(f"{davlat.title()}ning poytaxti {info['poytaxt']}.\n"
#           f"Maydoni {info['maydon']} kvadrat kilometr.\n"
#           f"Aholi soni {info['aholi']} nafar.\n"
#           f"Pul birligi: {info['pul birligi']}.\n")

davlat = input("Biror davlat nomini kiriting:").lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"{davlat.title()}ning poytaxti {info['poytaxt']}.\n"
                  f"Maydoni {info['maydon']} kvadrat kilometr.\n"
                  f"Aholi soni {info['aholi']} nafar.\n"
                  f"Pul birligi: {info['pul birligi']}.\n")
else:
    print("Bizda bu davlat haqida ma'lumot yo'q")
    
