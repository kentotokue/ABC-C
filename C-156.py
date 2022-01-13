'''
Created on 2021/09/11

@author: kentoo
'''
N = int(input())

X = list(map(int,input().split()))

MX = max(X)
MN = min(X)
ans = 1001001001
for i in range(MN,MX+1):
    sum = 0
    for j in range(N):
        sum += (X[j]-i)**2
    ans =min(ans,sum)

print(ans)