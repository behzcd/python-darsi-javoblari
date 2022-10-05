# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 00:55:12 2022

@author: Bekhzod
"""

# while True:
#     kitob = input("Yaxshi ko'rgan kitoblariz nomini kiriting(barcha kitoblarni kiritib bo'lgach 'stop' deb yozing): ").lower()
#     if kitob == 'stop':
#         break
# print('Rahmat!')

# while True:
#     narx = input("Yoshingizni kiriting(dasturdan chiqib ketish uchun 'exit'yoki 'quit' deb yozing): ")
#     if narx=='exit' or narx=='quit':
#         break
#     if int(narx)<=7:
#         print("2000 so'm")
#     elif 7<int(narx)<=18:
#         print("3000 so'm")
#     elif 18<int(narx)<=65:
#         print("10000 so'm")
#     elif int(narx)>65:
#         print('bepul')

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    if float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
        
        