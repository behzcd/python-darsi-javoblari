# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 02:13:20 2022

@author: Administrator
"""

class user:
    def __init__(self,name,username,byear,email,tel):
        self.name = name
        self.uname = username
        self.byear = byear
        self.mail = email
        self.tel = tel
        
    def get_info(self):
        return f"Foydalanuvchi: {self.uname}, ismi: {self.name}, emaili: {self.mail}, yoshi: {2022-self.byear}, telefon raqami: {self.tel}"
    
    def get_age(self,yil):
        return yil-self.byear
    def get_mail(self):
        return self.mail
    def get_num(self):
        return self.tel
    def get_uname(self):
        return self.uname
    
    
user1 = user('Behzod','behzcd.m',1999,'kingbehzod99@gmail.com',821039212299)
print(user1.get_info())
