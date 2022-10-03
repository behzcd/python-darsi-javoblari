# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 15:07:44 2022

@author: Bekhzod
"""

#names = ['Farrux','Sardor','Maruf','Bahodir']
#print(names[0], "bugun darsing nechigacha bo'ladi?")
#print(names[1],"sen",names[0]+"ga 6k berishing kerak. Ok?")
#print(names[2],"bugun ish borakanmi CJ da? Bo'lsa men bilan",names[3]+"ni yozib qo'y!")
#print("Professor,",names[3],"went to the immigration office to extend his visa.")

#numbers = [25,-73,3.14,100.0,354,798.2]
#print(numbers[1]+numbers[-2])
#print(numbers[-1]//numbers[2])
#numbers[1]=numbers[1]+3
#numbers[2]=2.17
#print(numbers)

#t_shaxslar=['Imom Buxoriy','Abu Hanifa','Muhammad sav','Ali ra','Alisher Navoiy','Rumiy','Yusuf as','MuhammadSodiq Muhammad Yusuf rahimahullohi alayh']
#z_shaxslar=['Abror Muxtor Aliy','MrBeast','Elon Musk','Khabib','Cr Ronaldo']
#print("Men buyuk tarixiy insonlardan qaniydi payg'ambarimiz",t_shaxslar.pop(2),"bilan zamonaviy shaxslardan",z_shaxslar[0],"bilan suhbat qursaydim.")

friends=[]
friends.append('Sardor')
friends.append('Farrux')
friends.append('Maruf')
friends.append('Bahodir')
friends.append('Momintoy')
friends.append('Nazarbek')
friends.append('Gofurjon')
friends.append('Ayubxon')
friends.append('Teddy')
friends.append('Jasur')
friends.remove('Momintoy')
friends.remove('Ayubxon')
friends.remove('Jasur')
friends.append('Asliddin')
friends.insert(0,'Abdurahmat')
friends.insert(4,'Azamat')
mehmonlar=[]
mehmonlar.append(friends.pop())
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(2))
print(f"Kelgan mehmonlar quyidagilar:{mehmonlar}")
