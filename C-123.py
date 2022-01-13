'''
Created on 2021/11/12

@author: kentoo
'''
N = int(input())
I = [int(input()) for i in range(5)]
L = min(I)
print((N+L-1)//L+4)