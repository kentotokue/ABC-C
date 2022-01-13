'''
Created on 2021/07/28

@author: kentoo
'''
N=int(input())
C=list(map(int,input().split()))
mod=1000000007

C.sort()

ans=1

for i in range(N):
    ans=(ans*max(C[i]-i,0))%mod 
    

print(ans)

