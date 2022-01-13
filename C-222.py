'''
Created on 2021/10/09

@author: kentoo
'''

N,M = map(int,input().split())

A = [str(input()) for i in range(2*N)]

ans = {}
for i in range(2*N):
    ans[i] = 0


for i in range(M):
    key = []
    for j in range(N):
        key = list(ans.keys()) 
        if A[key[2*j]][i] =="G" and  A[key[2*j+1]][i] == "C":
            ans[key[2*j]] += 1
        elif  A[key[2*j]][i] =="C" and  A[key[2*j+1]][i] == "P":
            ans[key[2*j]] += 1
        elif  A[key[2*j]][i] =="P" and  A[key[2*j+1]][i] == "G":
            ans[key[2*j]] += 1
        elif  A[key[2*j]][i] == A[key[2*j+1]][i]:
            continue
        else:
            ans[key[2*j+1]] += 1
    ans = sorted(ans.items(), key=lambda i: i[1],reverse=True)
    ans =dict(ans)
   
ans = dict(sorted(ans.items()))

for i in range(2*N):
    K = max(ans,key = ans.get)
    print(K+1)
    del ans[K]
    
   
