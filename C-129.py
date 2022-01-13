'''
Created on 2021/10/11

@author: kentoo
'''
N,M = map(int,input().split())
broken = [ 0 for i in range(N+1)]
for i in range(M):
    A = int(input())
    broken[A] = 1
#print(broken)

dp = [ 0 for i in range(N+2)]
mod = 1000000007
dp[N] = 1
#print(dp)
for i in range(N-1,-1,-1):
    if broken[i]:
        dp[i] = 0
        continue
    dp[i] = (dp[i+1] + dp[i+2]) % mod 
print(dp[0])
        