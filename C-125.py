'''
Created on 2021/10/18

@author: kentoo
'''
import math 

N = int(input())
A = list(map(int,input().split()))
L = [ 0 for i in range(N)]
R = [ 0 for i in range(N)]
#print(math.gcd(1,8))

for i in range(N-1):
    L[i+1] = math.gcd(L[i],A[i])
print(L)
for i in range(N-1,-1,-1):
    R[i-1] = math.gcd(R[i],A[i])
print(R)   

ans = 1
for i in range(N):
    ans = max(ans,math.gcd(L[i],R[i]))
print(ans)
