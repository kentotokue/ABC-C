'''
Created on 2021/08/06

@author: kentoo
'''
K,N=map(int,input().split())
A=list(map(int,input().split()))
A.append(A[0]+K)

L=0

for i in range(len(A)-1):
    L=max(L,A[i+1]-A[i])

print(K-L)