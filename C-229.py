'''
Created on 2021/11/27

@author: kentoo
'''
N,W = map(int,input().split())
C = [list(map(int,input().split())) for i in range(N)]

C.sort(reverse = True)
O = 0
for i in range(N):
    if W < C[i][1]:
        O +=C[i][0] * W
        W = 0
    else:
        W -= C[i][1]
        O += C[i][0] * C[i][1]
    if W <= 0:
        print(O)
        exit()


print(O)    