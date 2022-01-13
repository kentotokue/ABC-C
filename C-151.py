'''
Created on 2021/09/15

@author: kentoo
'''
N,M = map(int,input().split())
'''
A =[input().split() for i in range(M)]

WA = [0]*N
AC = [0]*N
miss = 0
id = 0

for i in range(M):
    print(int(A[i][0]))
    if AC[int(A[i][0])-1] ==1:
        continue
    if A[i][1] =="AC":
        AC[int(A[i][0])-1] = 1
    else:
        WA[int(A[i][0])-1] +=1

    
print(AC)
print(WA)
'''

AC=[0]*N
WA=[0]*N
for i in range(M):
    P,S=map(str,input().split())
    P=int(P)-1
    
    if AC[P] == 1:
        continue
    if S == "AC":
        AC[P]=1
    else:
        WA[P] += 1

ac=0
wa=0
for i in range(N):
    ac += AC[i]
    if AC[i]:
        wa +=WA[i]

print(ac,wa)

