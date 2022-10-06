# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 20:57:25 2022

@author: Bekhzod
"""
# print("Buyurtma qabul qiluvchi dastur.")
# buyurtmalar = []
# while True:
#     mahsulot = "Buyurtma bermoqchi bo'lgan mahsulotingiz nomini yozing:"
#     buyurtma = input(mahsulot).lower()
#     buyurtmalar.append(buyurtma)
#     yana = input("Yana mahsulot qo'shmoqchimisiz(ha/yo'q): ").lower()
#     if yana != "ha":
#         break
# print("Sizning buyurtmangiz quyidagilar:")
# for x in buyurtmalar:
#     print(x.title())
    
# mahsulotlar = {}
# while True:
#     mahsulot = input("Mahsulot nomini kiriting: ").lower()
#     narx = input("Mahsulot narxini kiriting: ")
#     mahsulotlar[mahsulot] = narx
#     yana = input("Yana mahsulot kiritishni hohlaysizmi?(ha/yo'q): ").lower()
#     if yana != 'ha':
#         break
# for x, y in mahsulotlar.items():
#     print(f"{x.title()} - {y} so'm")
    
mahsulotlar = {
    'olma':10000,
    'tarvuz':20000,
    'fanta':11000,
    'shampun':30000,
    'sovun':10000,
    'non':5000,
    'muzqaymoq':7000,
    'piyoz':5000
    }
savat = []
while True:
    mahsulot = input("Mahsulot nomini kiriting: ").lower()
    savat.append(mahsulot)
    yana = input("Yana mahsulot qo'shmoqchimisiz?(ha/yo'q): ").lower()
    if yana != 'ha':
        break
for x in savat:
    if x in mahsulotlar:
        print(f"{x.title()} - {mahsulotlar[x]} so'm")
    else:
        print(f"Uzur, bizda {x.title()} yo'q")

    