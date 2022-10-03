# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 16:11:17 2022

@author: Bekhzod
"""

#davlatlar = ['Fransiya','Turkiya','USA','Italiya','Korea','Xitoy']
#print(davlatlar)
#print(len(davlatlar))
#print(sorted(davlatlar))
#print(sorted(davlatlar,reverse=True))
#print(davlatlar)
#davlatlar.reverse()
#print(davlatlar)
#davlatlar.sort()
#print(davlatlar)
#davlatlar.sort(reverse=True)
#print(davlatlar)

#sonlar= list(range(120,1200,2))
#print(sonlar)
#print(sum(sonlar))
#print('Ayirma:',max(sonlar)-min(sonlar))
#rint(len(sonlar))
#print(sonlar[:20])
#print(sonlar[-20:])
#print(sonlar[260:280])

taomlar = ['osh','manti','norin','shashlik','mastava']
nonushta = taomlar[:]
nonushta.remove('osh')
nonushta.remove('shashlik')
nonushta.append('asal')
nonushta.append('qatiq')
print(taomlar)
print(nonushta)
nonushta = tuple(nonushta)
print(nonushta)
nonushta[0]='qaymoq va non'
print(nonushta)
