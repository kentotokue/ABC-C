'''
Created on 2021/07/31

@author: kentoo
'''

N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

A.sort()
B.sort()

AI=0
BI=0
ans=1001001001
while (AI<N and BI<M):
    ans=min(ans,abs(A[AI]-B[BI]))
    if (A[AI]<B[BI]):
        AI+=1
    else:
        BI+=1

print(ans)
    



