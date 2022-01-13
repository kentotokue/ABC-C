'''
Created on 2021/10/15

@author: kentoo
'''
N,K = map(int,input().split())
ans = 0
for i in range(1,N+1):
    X = i 
    cnt = 0
    while X < K :
        cnt += 1 
        X *= 2
    ans += (1/N)*(0.5**cnt)
print(ans)
    
    