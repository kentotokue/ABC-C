'''
Created on 2021/11/13

@author: kentoo
'''
N,M = map(int,input().split())

D = [list(map(int,input().split())) for i in range(N)]

D.sort()

sum = 0
for i in range(N):
    if D[i][1] <= M:
        M -= D[i][1]
        sum += D[i][0]*D[i][1]

        
    else:
        sum += D[i][0]*M
        break


print(sum)