'''
Created on 2021/07/22

@author: kentoo
'''
N=int(input())

A=list(map(int,input().split()))

ans=0
mod=1000000007

x=0

for i in range(N):
    ans+=A[i]*x 
    x+=A[i]
    
print(ans%mod)
    
    

    

