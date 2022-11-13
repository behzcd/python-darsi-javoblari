# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 05:14:46 2022

@author: Bekhzod
"""

class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    
    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil
    
class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
class Fan:
    def __init__(self,fan,teacher,room):
        self.fan = fan
        self.teacher = teacher
        self.room = room
        
    def fan_info(self):
        return f"Fan nomi: {self.fan}, o'qituvchi: {self.teacher}, xona: {self.room}"
    def fan_nomi(self):
        return self.fan


class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil,fanlar):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []
    
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info
    
    def fanga_yozil(self,sub):
        self.fanlar.append(sub)
        if len(self.fanlar):
            print('qoshildi')
        else:
            print('qoshilmadi')
        
    def get_fanlar(self):
        return self.fanlar
        
    def remove_fan(self,fan):
        if fan not in self.fanlar:
            ans = "Siz bu fanga yozilmagansiz"
            return ans
        else:
            self.fanlar.remove(fan)
            ans = 'Bu fan ochirildi'
            return ans

manzil1 = Manzil(46,'Mustaqillik','Namangan','Namangan')
fan1 = Fan('AI','Kakani Vijay','6-326')
fan2 = Fan('Supply Management','So Won Jiong','M-224')
fan3 = Fan('Database Management','Mehdi','6-326')
talaba1 = Talaba('Behzod','Muhammadaliyev','FA0228821',1999,12194852,manzil1,fan1)
talaba1 = Talaba('Behzod','Muhammadaliyev','FA0228821',1999,12194852,manzil1,fan2)
talaba1 = Talaba('Behzod','Muhammadaliyev','FA0228821',1999,12194852,manzil1,fan3)    