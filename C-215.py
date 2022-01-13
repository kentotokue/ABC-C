'''
Created on 2021/08/21

@author: kentoo
'''
import itertools
S,K=map(str,input().split())
K=int(K)

ans=list(itertools.permutations(S))
A=[]

for i in range(len(ans)):
    sum=""
    for j in range(len(S)):
        sum=sum+str(ans[i][j])
    A.append(sum)
A=set(A)
A=list(A)
A.sort()
print(A[K-1])
