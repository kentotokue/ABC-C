'''
Created on 2021/07/31

@author: kentoo
'''
N=int(input())
A=list(map(int,input().split()))

U=[0]*N 

for i in A:
    U[i-1]+=1
    
for i in U:
    print(i)