'''
Created on 2021/07/01

@author: kentoo
'''

N=int(input())

P=[list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(i):
        for k in range(j):
            
            x1=P[i][0]
            y1=P[i][1]
            x2=P[j][0]
            y2=P[j][1]
            x3=P[k][0]
            y3=P[k][1]
            
            x1-=x3
            x2-=x3 
            y1-=y3
            y2-=y3 
            
            if x1*y2 ==x2*y1:
                print("Yes")
                exit()
            
print("No")

            