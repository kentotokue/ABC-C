'''
Created on 2021/08/06

@author: kentoo
'''
N,K=map(int,input().split())

A=N%K 

print(min(A,abs(K-A)))