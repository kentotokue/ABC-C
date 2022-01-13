'''
Created on 2021/07/24

@author: kentoo
'''

S = str(input())

N = len(S)

dp = [[0 for i in range(N+1)]for j in range(9)]
for i in range(N+1):
    dp[0][i]=1

mod = 1000000007

T = "chokudai"

for i in range(8):
    print(" ")
    for j in range(N):
        
        if T[i] != S[j]:
            dp[i+1][j+1] = dp[i+1][j]
            
        else:
            dp[i+1][j+1] = (dp[i][j]+dp[i+1][j])%mod
            
'''
for k in range(9):
    print(dp[k])
'''   
print(dp[8][N])
        