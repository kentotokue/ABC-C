'''
Created on 2021/09/22

@author: kentoo
'''
import itertools
import math


N = int(input())
C = [list(map(int,input().split())) for i in range(N)]

id = []
for i in range(N):
    id.append(i)

per_list = list(itertools.permutations(id))

sum = 0
s = 0
for i in range(len(per_list)):
    s=0
    for j in range(N-1):
        
        s += math.sqrt((C[per_list[i][j+1]][0]-C[per_list[i][j]][0])**2+(C[per_list[i][j+1]][1]-C[per_list[i][j]][1])**2)
        
    sum += s

print(sum/len(per_list))
        
        