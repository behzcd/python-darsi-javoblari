# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 15:02:11 2022

@author: Bekhzod
"""

filename = 'new_data.txt'
new1 = "open('file.txt','w') - Faylni yozish uchun ochish. Fayl mavjud bo'lmasa yangi fayl yaratadi. Fayl mavjud bo'lsa tarkibi o'chib ketadi "
new2 = '''Faylni qatorma-qator o'qish:
    filename = 'data/talabalar.txt'
    with open(filename) as file:
        for line in file:
            print(line)'''
new3 = '''Papka ichidagi fayllarni ochish:
    with open('data/pi.txt') as fayl:
    pi = fayl.read()'''
new4 = "Qatorlarni ro'yxat ko'rinishida saqlab olish uchun, .readlines() metodidan foydalanamiz."

with open(filename, 'w') as file:
    file.write(new1+'\n'+'\n')
    file.write(new2+'\n'+'\n')
    file.write(new3+'\n'+'\n')
    file.write(new4+'\n'+'\n')

# with open(filename) as file:
#     for line in file:
#         print(line)

fname = 'pi_million_digits.txt'
with open(fname) as file:
    pi = file.read()
def byear_in_pi(x):
    if str(x) in pi:
        print("Tabrikalaman tug'ulgan kuningiz pi soni tarkibida uchraydi")
    else:
        print("Afsus, pi soni tarkibida bu sana yo'q")

import pickle
with open('new_pkl','wb') as file:
    pickle.dump(float(pi),file)

with open('new_pkl','rb') as file:
    f_pi = pickle.load(file)

print(f_pi)


flname = 'data.txt'
def new_data():
    while True:
        info = input("Insert data:\n>>>")
        with open(flname,'a') as file:
            file.write(info+'\n')
        again = input("Yana ma'lumot kiritasizmi?(yes/no):\n>>>")
        if again.lower() == 'no':
            break
        
def open_file():
    with open(flname) as file:
        data = file.read()
    print(data)
