'''
Created on 2021/08/05

@author: kentoo
'''
import math

def GCD (x,y):
    
    while y!=0:
        a=x%y
        x=y 
        y=a 
        
    return x

sum=0
K=int(input())
for i in range(1,K+1):
    for j in range(1,K+1):
        for k in range(1,K+1):
            sum+=math.gcd(math.gcd(i,j),k)
            

print(sum)
            