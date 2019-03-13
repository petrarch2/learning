#!/usr/bin/python3
import sys
from random import randint

# num = randint(1,1000)
# value=int(input('input value from 1 to 1000:'))
# while value != num:
    # if value>num:
        # print('Large',value)
    
    # if value<num:
        # print('Small',value)
    # value=int(input())
# print('equel',value)
num = [1,5,7,3,4]; 
l = ['meat', 'egg', 'fish', 'milk']
j = {'meat', 'egg', 'fish', 'milk'}
p = ('meat', 'egg', 'fish', 'milk')
q = ['meat', 'egg', 'fish', 6.7]
num.append(8)
del num[1]
for i in l:
	print(num[-3])

print(type(p))
print(type(q))
print(type(j))
print(type(i))
print(sys.argv)	

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
print(tinydict.keys()) 
print(tinydict.values())
print(tinydict['site']) 

try:
	c = open('test1.html','r',encoding='utf-8')
	d = c.read()
	c.close()
	print(d)
except:
	print('file not exist')
	
a = r'\\_v_//'
b = '\\\_v_//'
c = '''aa
cc
dd
ff'''
print(a,b,c,end='\n')
input(' '.join(l))
