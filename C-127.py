'''
Created on 2021/10/12

@author: kentoo
'''
N,M = map(int,input().split())

G = []
for i in range(M):
    L,R = map(int,input().split())
    G.append([L,R])


L = 0
H = 1000000
for i in range(M):
    TL = G[i][0]
    TH = G[i][1]
    
    L = max(L,TL)
    H = min(H,TH)

    if L > H:
        print("0")
        exit()

print(H-L+1)


    
