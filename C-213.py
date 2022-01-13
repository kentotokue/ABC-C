'''
Created on 2021/08/11

@author: kentoo
'''

def comp(a):
    N=len(a)
    mp={}
    for i in range(N):
        mp[a[i]]=0
    mp=dict(sorted(mp.items()))
    id=1
    for i in mp.keys():
        mp[i]+=id
        id+=1
    for i in range(N):
        a[i]=mp[a[i]]
    return a
        
        
H,W,N=map(int,input().split())
A=[]
B=[]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

A=comp(A)
B=comp(B)

for i in range(len(A)):
    print(f"{A[i]} {B[i]}")
