'''
Created on 2021/12/25

@author: kentoo
'''
import itertools
N,X = map(int,input().split())

L = [list(map(int,input().split())) for i in range(N)]
for i in  range(N):
    del L[i][0]
print(L)
sum = 0
cnt = 0



'''
for i in range(1,L[0][0]+1):
    sum = X //L[0][i]
    print(sum)
    for j in range(1,N):
        for k in range(1,L[j][0]+1):
            sum = X//L[j][k]
            if L[j][k] == sum:
                cnt += 1
print(cnt)
'''