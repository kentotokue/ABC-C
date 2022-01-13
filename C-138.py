'''
Created on 2021/09/27

@author: kentoo
'''
N = int(input())
V = list(map(int,input().split()))

V.sort()

for i in range(N-1):
    V.sort()
    A = (V[0]+V[1])/2
    V.append(A)

    del V[0],
    del V[0]


print(V[0])
    