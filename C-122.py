'''
Created on 2021/11/12

@author: kentoo
'''
N,Q = map(int,input().split())
S = str(input())
W = []
for i in range(Q):
    l,r = map(int,input().split())
    W.append([l,r])
#print(W)
cnt =[0 for i in range(N)]


for i in range(1,N):
    if S[i-1] == "A" and S[i] == "C":
        cnt[i] = cnt[i-1]+1
    else:
        cnt[i] = cnt[i-1]

#print(cnt)
for i in range(Q):
    ans = cnt[W[i][1]-1] - cnt[W[i][0]-1]
    print(ans)

    