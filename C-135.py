'''
Created on 2021/10/01

@author: kentoo
'''
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

cnt = 0

for i in range(N):
    left = min(A[i],B[i])
    cnt += left 
    A[i] -= left 
    B[i] -= left 
    
    right = min(A[i+1],B[i])
    cnt += right 
    A[i+1] -= right
    B[i] -= right 

print(cnt)