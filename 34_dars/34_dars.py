# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 22:47:22 2022

@author: Bekhzod
"""
import json
#1
data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
data_json = json.dumps(data)
# print(data_json)

#2
talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba = json.loads(talaba_json)
# print(talaba['ism']+' '+talaba['familiya'])

#3
filename = 'data_json'
with open(filename,'w') as f:
    json.dump(data,f)
    
with open("talaba_json.json","w") as f:
    json.dump(talaba,f)
    
with open("talaba_json.json") as f:
    data = json.load(f)
# print(data)

#4
# filename = 'students.json'
# with open(filename) as f:
#     students = json.load(f)
    
# for x in students['student']:
#     print(f"{x['name']} {x['lastname']}, {x['year']}-kurs, {x['faculty']} talabasi")
    
#5
fname = 'api-result.json'
with open(fname) as f:
    python = json.load(f)
print(python['query']['pages']['13801']['title'])
print(python['query']['pages']['13801']['extract'])