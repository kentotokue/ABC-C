'''
Created on 2021/10/17

@author: kentoo
'''
N = int(input())
D = [list(map(int,input().split())) for i in range(N)]
sum = 0
for i in range(N):
    sum += D[i][0]
H = sum/2 
cnt = 0
s = 0
for i in range(N):
    T = D[i][0]/D[i][1]
    
    H -= 1
    if H == 0:
        break
    s += T
H1 = sum/2
m = []
for i in range(N):
    m.append(1/D[i][1])
    
for i in range(N-1,-1,-1):

    if m[i]*s <= H1:
        print(H1+(H1-m[i]*s)/2)
        exit()
    H -= m[i]*1
    s -= 1

    