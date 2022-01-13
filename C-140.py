'''
Created on 2021/09/26

@author: kentoo
'''

N = int(input())
B = list(map(int,input().split()))

A = [0]*N 
A[0] = B[0]

for i in range(N-1):
    A[i] = min(B[i],B[i-1])

A[N-1] = B[N-2]

ans = 0
for i in range(N):
    ans += A[i]

print(ans)