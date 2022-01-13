'''
Created on 2021/09/14

@author: kentoo
'''
N = int(input())
P = list(map(int,input().split()))

m = 1001001001
mx = 0
cnt = 0
for i in range(N):
    if m >= P[i]:
        cnt += 1
        m = min(m,P[i])
        
        
print(cnt)