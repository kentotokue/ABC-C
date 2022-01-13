'''
Created on 2021/10/02

@author: kentoo
'''
import copy

N = int(input())
A = [int(input()) for i in range(N)]

AS = sorted(A,reverse = True)

for i in range(N):
    ans = AS[0]
    if A[i] == AS[0]:
        ans = AS[1]
    print(ans)

'''
for i in range(N):
    ans = copy.copy(A)
    del ans[i]
    print(max(ans))
'''    


