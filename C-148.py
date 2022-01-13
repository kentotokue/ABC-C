'''
Created on 2021/09/20

@author: kentoo
'''


A,B = map(int,input().split())


def gcd  (a,b):
    X = max(a,b)
    Y = min(a,b)
    
    tmp = X%Y 
    while tmp :
        X = Y
        Y = tmp
        tmp = X%Y 
        
    return Y 

print(A*B//(gcd(A,B)))
         
        

