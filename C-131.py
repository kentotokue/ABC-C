'''
Created on 2021/10/04

@author: kentoo
'''
import math
def lcm (A,B):
    return (A*B)//math.gcd(A,B)

def f (X,A,B):
    return X - (X//A)-(X//B)+(X//lcm(A,B))

A,B,C,D = map(int,input().split())


print(f(B,C,D)-f(A-1,C,D))

