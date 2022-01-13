'''
Created on 2021/09/11

@author: kentoo
'''

N,M = map(int,input().split())

S =[]

for i in range(M):
    s,c = map(int,input().split())
    S.append([s,c])


for i in range(1,1000):
    nx = i //10
    d = [i%10]
    
    while nx:
        d.append(nx%10)
        nx=nx//10
    d.reverse()
    if len(d) != N:
        continue
    flag = True
    for n in range(M):
        if d[S[n][0]-1] != S[n][1]:
            flag = False
    if flag :
        print(i)
        exit()

print("-1")
 
    