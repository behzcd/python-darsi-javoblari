# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 16:16:21 2022

@author: Bekhzod
"""

class Person:
    def __init__(self,name,surname,passport,byear):
        self.name = name
        self.surname = surname
        self.passport = passport
        self.byear = byear
    
    def get_info(self):
        info = f"{self.name} {self.surname}. "
        info += f"Passport:{self.passport}, born in {self.byear}"
        return info
        
    def get_age(self,current_year):
        return current_year - self.byear
    
    
class Student(Person):
    def __init__(self,name,surname,passport,byear,idnum,syear=1):
        super().__init__(name, surname, passport, byear)
        self.idnum = idnum
        self.syear = syear
    
    def get_id(self):
        return self.idnum
    
    def get_syear(self):
        return self.syear
    
    def get_info(self):
        info = f"{self.name} {self.surname}. "
        info += f"{self.get_syear()}st/nd/rd/th year student. ID number: {self.idnum}"
        return info
    
    def __repr__(self):
        info = f"{self.name} {self.surname}. "
        info += f"{self.get_syear()}st/nd/rd/th year student. ID number: {self.idnum}"
        return info
    
    def __lt__(self,y):
        return self.syear < y.syear
    
    def __eq__(self,y):
        return self.syear == y.syear

class Subject:
    def __init__(self,name,prof,room):
        self.name = name
        self.prof = prof
        self.room = room
        self.students = []
        
    def __repr__(self):
        return f"Subject: {self.name}, Professor: {self.prof}, Room: {self.room}"
    
    def add_student(self,*students):
        for x in students:
            if isinstance(x,Student):
                self.students.append(x)
            else:
                print("Insert object 'Student'")
            
    def __getitem__(self,index):
        return self.students[index]
    
    def __setitem__(self,index,y):
        return self.students[index] == y
    
    def __len__(self):
        return len(self.students)
    
    def __add__(self,student):
        if isinstance(student,Student):
            self.add_student(student)
            
    def __sub__(self,idnum):
        for x in self.students:
            if idnum == x.get_id():
                self.students.remove(x)
                print("O'chirildi!")
    
    def __call__(self,*value):
        if value:
            return [value for value in self.students]
        else:
            return f"Subject: {self.name}, Professor: {self.prof}, Room: {self.room}"

student1 = Student('Behzod','Mukhammadaliev','FA0218822',1999,12194852,4)
student2 = Student('Farrukh','Marufjonov','FA3736763',2001,12194944,4)
student3 = Student('Sardor','Khabibullaev','FA4546623',2000,12200245,3)
sub1 = Subject('Supply Chain Management', 'Mehdi Shomohammad','6-326')

# print(student1<student3)
# print(student1==student2)

sub1.add_student(student1,student2,student3)

student4 = Student('Maruf','Abdurohirov','FA2344567',1999,12194836,4)
sub1 + student4

print(sub1())
print(sub1(student1))