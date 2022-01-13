'''
Created on 2021/09/25

@author: kentoo
'''

N = int(input())
A = list(map(int,input().split()))
ans = {}
for i in range(1,N+1):
    ans[A[i-1]] = i
print(ans)
#ans = sorted(ans.items())
#print(ans)
for i in range(1,len(A)+1):
    print(ans[i],end=" ")