# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 18:01:11 2022

@author: Bekhzod
"""

# def sh_malumot(ism, familiya, t_yili, t_joyi, email="mavjud emas", tel="mavjud emas"):
#   info = {"ism":ism,
#       "familiya":familiya,
#       "t_yili":t_yili,
#       "t_joyi":t_joyi,
#       "yoshi":2022-t_yili,
#       "email":email,
#       "tel":tel}
#   return info

# print("Mijozlar haqida ma'lumot kiriting:")
# mijozlar = []
# while True:
#     ism = input("Ismini kiriting: ")
#     familiya = input("Familiyasi: ")
#     t_yili = int(input("Tug'ulgan yili: "))
#     t_joyi = input("Tug'ulgan joyi: ")
#     email = input("Emaili: ")
#     tel = input("Telefon raqami: ")
#     mijozlar.append(sh_malumot(ism,familiya,t_yili,t_joyi,email,tel))
#     yana = input("Yana mijoz kiritasizmi?(yes/no): ")
#     if yana!="yes":
#         break
    
# print("\nMijozlar:\n")
# for x in mijozlar:
#     print(f"{x['ism'].title()} {x['familiya'].title()}, yoshi {x['yoshi']} da\nEmaili: {x['email']}, Telefon raqami: {x['tel']}\n")
    

# def kattasi(x,y,z):
#     max = x
#     if y>=max:
#         max = y
#     if z>=max:
#         max = z
#     return max

# # kattasi(46,4874,6)

    
# def aylana_radiusi(x):
#     info = {'radiusi':x,
#             'diametri':2*x,
#             'parimetri':2*3.14*x,
#             'yuzi':3.14*(x**2)}
#     return info
# y = aylana_radiusi(3)
# print(y)

# def oraliq(x,y):
#     tub_sonlar = []
#     for n in range(x,y+1):
#         tub = True
#         if (n==1):
#             tub = False
#         elif (n==2):
#             tub = True
#         else:
#             for z in range(2,n):
#                 if (n%z==0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
    
#     return tub_sonlar

# h = oraliq(30,100)
# print(h)

def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)        
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar

son = fibonacci(20)
print(son)

    