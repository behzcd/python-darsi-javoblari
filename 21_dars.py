# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 02:14:10 2022

@author: Bekhzod
"""

# def katta_harf(matn):
#     yangi_matn = []
#     while matn:
#         qiymat = matn.pop()
#         yangi_matn.append(qiymat.title())
#     return yangi_matn
        
# matn = ['behzod','sardor','maruf','farrux']
# katta_harfla = katta_harf(matn)
# print(katta_harfla)


# def katta_harf(matn):
#     yangi_matn = []
#     while matn:
#         qiymat = matn.pop()
#         yangi_matn.append(qiymat.title())
#     return yangi_matn
        
# matn = ['behzod','sardor','maruf','farrux']
# katta_harfla = katta_harf(matn[:])
# print(katta_harfla)
# print(matn)


def bahola(ismlar):
    baholar = {}
    for x in ismlar:
        baho = input(f"Talaba {x.title()}ning bahosini kiriting: ")
        baholar[x.title()]=baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar[:])
print(baholar)
print(talabalar)

