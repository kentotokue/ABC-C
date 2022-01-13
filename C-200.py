'''
Created on 2021/06/26

@author: kentoo
'''
N=int(input())
A=list(map(int,input().split()))

cnt=[0]*200

for i in range(200):
    sum=0
    for j in range(N):
        if i==(A[j]%200):
            sum+=1
    cnt[i]=sum

ans=0
for i in range(200):
    ans+=cnt[i]*(cnt[i]-1)//2
    
print(ans)       