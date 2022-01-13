'''
Created on 2021/08/14

@author: kentoo
'''
N=int(input())
S=list(map(int,input().split()))
T=list(map(int,input().split()))

ans=[0]*N 

for i in range(2*N):
    T[(i+1)%N]=min(T[(i+1)%N],T[i%N]+S[i%N])
    

for i in range(len(T)):
    print(T[i])