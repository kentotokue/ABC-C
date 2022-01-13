'''
Created on 2021/11/13

@author: kentoo
'''

N = int(input())

ans = 0
A = 1
while A*A*A <= N:
    B = A
    while A*B*B <= N :
        maxC = N//(A*B)
        ans += maxC-B+1
        
        B += 1
    A += 1
print(ans)

'''
N=int(input())
ans=0
for a in range(1,N+1):
    if a*a*a>N: break
    for b in range(a,N+1):
        if a*b*b>N: break
        ans+=N//a//b-b+1
print(ans)
'''