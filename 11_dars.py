# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 21:45:24 2022

@author: Bekhzod
"""

# son = float(input('Iltimos, juft son kiriting:'))
# if son%2==0:
#     print('Rahmat')
# else:
#     print('Bu son juft emas')


# yosh = int(input('Yoshingiz nechchida?:'))
# if yosh<=4 or yosh>=60:
#     narx = "bepul"
# elif yosh<=18:
#     narx = 10000
# else:
#     narx = 20000
# print(f"Siz uchun muzeyga kirish chipta narxi {narx}")


# print('Iltimos ikkita son kiriting!')
# son1 = float(input('Birinchi sonni kiriting:'))
# son2 = float(input('Ikkinchi sonni kiriting:'))
# if son1>son2:
#     print(f"Siz kiritgan birinchi son ikkinchi sondan katta, {son1}>{son2}")
# elif son1<son2:
#     print(f"Siz kiritgan birinchi son ikkinchi sondan kichkina, {son1}<{son2}")
# else:
#     print(f"Siz kiritgan sonlar teng, {son1}={son2}")


# mahsulotlar = ['shampun','sovun','non','kola','kartoshka','piyoz','sabzi','karam','uzum','olma','nok']
# savat=[]
# print("Iltimos, savatga 5 ta mahsulot kiriting!")
# mah1 = input('Birinchi mahsulot nomini kiriting:')
# savat.append(mah1.lower())
# mah2 = input('Ikkinchi mahsulot nomini kiriting:')
# savat.append(mah2.lower())
# mah3 = input('Uchinchi mahsulot nomini kiriting:')
# savat.append(mah3.lower())
# mah4 = input('To\'rtinchi mahsulot nomini kiriting:')
# savat.append(mah4.lower())
# mah5 = input('Beshinchi mahsulot nomini kiriting:')
# savat.append(mah5.lower())
# for x in savat:
#     if x in mahsulotlar:
#         print(f"{x.title()} do'konimizda bor")
#     else:
#         print(f"{x.title()} do'konimizda yo'q")


# mahsulotlar = ['shampun','sovun','non','kola','kartoshka','piyoz','sabzi','karam','uzum','olma','nok']
# savat=[]
# print("Iltimos, savatga 5 ta mahsulot kiriting!")
# mah1 = input('Birinchi mahsulot nomini kiriting:')
# savat.append(mah1.lower())
# mah2 = input('Ikkinchi mahsulot nomini kiriting:')
# savat.append(mah2.lower())
# mah3 = input('Uchinchi mahsulot nomini kiriting:')
# savat.append(mah3.lower())
# mah4 = input('To\'rtinchi mahsulot nomini kiriting:')
# savat.append(mah4.lower())
# mah5 = input('Beshinchi mahsulot nomini kiriting:')
# savat.append(mah5.lower())
# bor_mahsulotlar = []
# mavjud_emas = []
# for x in savat:
#     if x in mahsulotlar:
#         bor_mahsulotlar.append(x)
#     else:
#         mavjud_emas.append(x)
# if len(mavjud_emas)==0:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
# else:
#     print(f"Quyidagi mahsulotlar do'konimizda yo'q:{mavjud_emas.title()}")


# foydalanuvchilar = ['anvar','sobir','bekzod','genius','nex1level','onlyforward']
# login = input("Yangi login tanlang:")
# if login.lower() not in foydalanuvchilar:
#     print("Login band, yangi login tanlang!")
# else:
#     print("Xush kelibsiz, foydalanuvchi!")


son = int(input('Biror butun son kiriting:'))
boluvchi = range(2,11)
for x in boluvchi:
    if son%x==0:
        print(f"Bu son {x} soniga qoldiqsiz bo'linadi")
        