'''
Created on 2021/07/23

@author: kentoo
'''
X,N=map(int,input().split())
P=list(map(int,input().split()))

A=[0]*102
B=[100]*102
for i in P :
    A[i]=1

ans=1000000

for i in range(len(A)):
    if A[i]==0 :
        B[i]=abs(X-i)
print(B.index(min(B)))



    
