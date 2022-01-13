'''
Created on 2021/06/21

@author: kentoo
'''

N=int(input())

A=list(map(int,input().split()))

cnt=dict()

ans=0

for i in range(N):
    ans+=i-cnt[A[i]]
    cnt[A[i]]+=1

print(cnt)