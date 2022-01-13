'''
Created on 2021/10/02

@author: kentoo
'''
import itertools
N = list(input())
N.sort()
print(N)
K = len(N)
ans = 0

for i in itertools.permutations(N):
    
    i = list(i)
    #print(i)
    for j in range(1,K):
        if i[0] == 0:
            continue
        if i[j] == 0:
            continue
        l = 0
        r = 0
        for g in range(j):
            l = l*10+int(i[g])
        for h in range(j,K):
            r = r*10+int(i[h])
        ans = max(ans,l*r)
print(ans)