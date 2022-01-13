'''
Created on 2021/09/04

@author: kentoo
'''
N = int(input())

P = list(map(int,input().split()))

ans = {}
for  i in range(N):
    ans[P[i]] = i+1
    
ans=sorted(ans.items())


for i in range(N):
    print(ans[i][1],end=" ")
 