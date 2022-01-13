'''
Created on 2021/12/19

@author: kentoo
'''
import itertools

N,M = map(int,input().split())

a = [[False]*N for i in range(N)]
b = [[False]*N for i in range(N)]

for i in range(M):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    a[u][v] = a[v][u] = True

for i in range(M):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    b[u][v] = b[v][u] = True
print(a)
print(b)
ans = False

for p in itertools.permutations(range(N)):
    ok = True
    print(p)
    for i in range(N):
        for j in range(N):
            if a[i][j] != b[p[i]][p[j]]:
                ok = False
    if ok :
        ans = True
print("Yes" if ans else "No")
    
'''
A = [list(map(int,input().split()))for i in range(M)]
C = [list(map(int,input().split()))for i in range(M)]

TA = {}
AO = {}

for i in range(len(A)):
    if A[i][0] in TA:
        TA[A[i][0]] += 1
    else:
        TA[A[i][0]] = 1
    if A[i][1] in TA:
        TA[A[i][1]] += 1
    else:
        TA[A[i][1]] = 1
        
             

for i in range(len(C)):
    if C[i][0] in AO:
        AO[C[i][0]] += 1
    else:
        AO[C[i][0]] = 1
    if C[i][1] in AO:
        AO[C[i][1]] += 1
    else:
        AO[C[i][1]] = 1

ansTA = []
ansAO = []
for i in TA.values():
    ansTA.append(i)

for i in AO.values():
    ansAO.append(i)
ansTA.sort()
ansAO.sort()
print(ansTA)
print(ansAO)
if ansTA == ansAO:
    print("Yes")
else:
    print("No")
'''
'''
for p in itertools.permutations(range(4)):
    print(p)
'''