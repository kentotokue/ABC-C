'''
Created on 2021/07/22

@author: kentoo
'''
import math
N=int(input())
S=set()
for x in range(1,math.floor(math.sqrt(N))+1):
    if N%x !=0:
        continue
    S.add(x)
    S.add(N//x)
S1=list(S) 
S1.sort()
for i in range(len(S1)):
    print(S1[i])
    
        
    