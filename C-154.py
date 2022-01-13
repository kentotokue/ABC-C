'''
Created on 2021/09/11

@author: kentoo
'''

N = int(input())
A = list(map(int,input().split()))
A2 = {}
for i in A :
    
    if i in A2:
        A2[i] +=1
    else:
        A2[i] = 1

if len(A)==len(A2):
    print("YES")
else:
    print("NO")