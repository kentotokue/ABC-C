'''
Created on 2021/09/24

@author: kentoo
'''
import math
N = int(input())
j = 0 
ans = 1e18
for i in range(1,int(math.sqrt(N)+1)):
    if N%i != 0:
        continue
    j = N/i
    ans = min(ans,i+j-2)
print(math.floor(ans))