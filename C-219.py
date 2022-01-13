'''
Created on 2021/09/18

@author: kentoo
'''
X = str(input())
N = int(input())
S = []
for i in range(N):
    S.append(str(input()))
    
F = {} 
G = {}

for i in range(26):
    F[X[i]] = f"a+{i}"
    
for i in range(26):
    G[f"a+{i}"] = X[i]


V = []
for i in range(N):

    A = []
    for j in range(len(S[i])):
        A.append(F[S[i][j]])

    V.append(A)

V.sort()

ans = []
for i in range(N):
    B = ""
    for j in range(len(V[i])):
        B = B + str(G[V[i][j]])
    ans.append(B)
     
for i in range(len(ans)):
    print(ans[i])
    
