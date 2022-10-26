# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 02:35:30 2022

@author: Administrator
"""

class Avto:
    def __init__(self,model,color,korobka,price):
        self.model = model
        self.color = color
        self.korobka = korobka
        self.price = price
        self.distance = 0
        
    def get_info(self):
        return f"Modeli: {self.model}, rangi: {self.color}, korobka: {self.korobka}, narxi: {self.price}, yurgani: {self.distance} km"
    
    def update_km(self,km):
        self.distance = km
        

class Avtosalon:
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.avtos = []
        
    def add_avto(self,avto):
        self.avtos.append(avto)
        
    def avtos_info(self):
        return [x.get_info() for x in self.avtos]
    
avto1 = Avto('Genesis','Black','Auto','$80 000')
avto2 = Avto('Kia K7','Grey','Auto','$30 000')
avto3 = Avto('Lacetti','White','Mexanika', '$10 000')
gm = Avtosalon('General Motors','321,Boburshox street,Tashkent,Uzbekistan')
avto1.update_km(142971)
print(avto1.get_info())
print(avto2.price)
print(gm.name)
gm.add_avto(avto1)
gm.add_avto(avto2)
gm.add_avto(avto3)
print(gm.avtos_info())

def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]
print(see_methods(Avtosalon))
print(avto1.__dict__)
print(avto2.__dict__.keys())











