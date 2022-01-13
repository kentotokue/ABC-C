'''
Created on 2021/11/20

@author: kentoo
'''
N,K = map(int,input().split())
P = [list(map(int,input().split())) for i in range(N)]
S = []
for i in range(N):
    S.append(sum(P[i]))
S.sort(reverse = True)
SO = S[K-1]

for i in range(N):
    if SO - sum(P[i]) <= 300:
        print("Yes")
    else:
        print("No")
    
