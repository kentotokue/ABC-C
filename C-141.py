'''
Created on 2021/09/26

@author: kentoo
'''
N,K,Q = map(int,input().split())

A = [K-Q]*N 
ans = {}
for i in range(1,N+1):
    ans[i] = 0

for i in range(Q):
    k = int(input())
    ans[k] += 1

ans_values = list(ans.values())

for i in range(len(ans)):
    A[i] += ans_values[i]
    if A[i] > 0:
        print("Yes")
    else:
        print("No")

