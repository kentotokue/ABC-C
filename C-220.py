'''
Created on 2021/09/26

@author: kentoo
'''

N = int(input())
A = list(map(int,input().split()))
X = int(input())

SUM = sum(A)
K = N*(X//SUM)

G = X-(SUM*(X//SUM))

for  i in range(N):
    G -= A[i]
    if G < 0:
        print(K+i+1)
        exit()
        

        
