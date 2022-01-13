'''
Created on 2021/06/26

@author: kentoo
'''
N=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
cnt=[0]*(N+1)

for i in range(N):
    sum=0
    for j in range(N):
        if i==A[j]:
            sum+=1
    cnt[i]=sum
    
ans=0
for j in range(N):
    ans+=cnt[B[C[j]-1]]
print(ans)
'''
for j in range(N):
    ans+
    
'''
