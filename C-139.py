'''
Created on 2021/09/27

@author: kentoo
'''

N = int(input())
H = list(map(int,input().split()))

cnt = 0
m = 0


for i in range(1,N):

    if H[i-1] >= H[i]:
        cnt += 1
    else:
        m = max(cnt,m)
        cnt = 0
m = max(cnt,m)
print(m)