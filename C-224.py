'''
Created on 2021/10/23

@author: kentoo
'''
N = int(input())
P = [list(map(int,input().split())) for i in range(N)]
cnt = 0
for i in range(N):
    for j in range(i,N):
        if i == j :
            continue
        for k in range(j,N):
            if j == k:
                continue
            #print(i,j,k)
            dx1= P[i][1]-P[j][1]
            dx2 = P[j][1]-P[k][1]
            dy1 = P[i][0]-P[j][0]
            dy2 = P[j][0]-P[k][0]
            if dx1 * dy2 != dx2 * dy1:
                cnt += 1
            
print(cnt)          