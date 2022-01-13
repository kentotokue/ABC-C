'''
Created on 2021/09/11

@author: kentoo
'''

N = int(input())

S = {}

for i in range(N):

    y = str(input())
    if y in S:
        S[y] += 1
    else:
        S[y] =1
    
Smax = max(S.values())
'''指定したvalueを取得'''
keys = [k for k ,v in S.items() if v==Smax]
keys.sort()

for i in keys:
    print(i)