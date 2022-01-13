'''
Created on 2021/09/10

@author: kentoo
'''
import math
A,B = map(int,input().split())



for i in range(10000):
    za=math.floor(i*(8/100))
    zb=math.floor(i*(10/100))
    
    if A ==za and B==zb:
        print(i)
        exit()
print("-1")