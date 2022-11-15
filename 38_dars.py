# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 06:21:00 2022

@author: Bekhzod
"""

#http://docs.python.org/3/library
#iHateRegex

#1 

import datetime as dt

today = dt.date.today()
variance = 0
for x in range(10):
    another_days = today + dt.timedelta(days = variance)
    variance += 14
    print(another_days)
    

#2

eid_fitr = dt.date(2023,4,21)
eid_adha = dt.date(2023,6,29)

fitr_days = eid_fitr - today
adha_days = eid_adha - today

print(f"Ramazon hayitigacha {fitr_days.days} kun qoldi\n"
      f"Qurbon hayitigacha {adha_days.days} kun qoldi")

#3

bday = dt.date(1999,12,28)
lmonth = dt.date(2022,10,28)
lbday = dt.date(2021,12,28)
pdays = today - bday

days = (today -lmonth).days
years = int(pdays.days/365)
month = 10


print(f"It's been {years} years, {month} months, and {days} days since my birthday.")

#4 

import re

# pattern = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
# msg = "Insert your phone number.\n>>>"

# while True:
#     pnumber = input(msg)
#     if re.match(pattern, pnumber):
#         print("The phone number was accepted!")
#         break
#     else:
#         print("The phone number is invalid. Try again!")
        
#5

pattern = 'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)'
text = """Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"""

link = re.findall(pattern,text)
print(link)