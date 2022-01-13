'''
Created on 2021/07/31

@author: kentoo
'''
N,M=map(int,input().split())
H=list(map(int,input().split()))

#R=[list(map(int,input().split())) for i in range(M)]
ok=[True]*N
for i in range(M):
    A,B=list(map(int,input().split()))
    if H[A-1]<=H[B-1]:
        ok[A-1]=False
    if H[B-1]<=H[A-1]:
        ok[B-1]=False

ans=0
for i in range(N):
    if ok[i]:
        ans+=1
print(ans)

'''
cnt=[0]*N

for i in range(1,M+1):
    if H[(R[i-1][0])-1]>H[(R[i-1][1])-1]:
        cnt[(R[i-1][0])-1]=1
    else:
        continue

for i in range(M,0,-1):
    if H[(R[i-1][1])-1]>H[(R[i-1][0])-1]:
        cnt[(R[i-1][1])-1]=1
    else:
        continue
flag=0
for i in cnt:
    flag+=int(i)

print(flag)

''' 