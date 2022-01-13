'''
Created on 2021/09/28

@author: kentoo
'''
N = int(input())
S = [''.join(sorted(str(input()))) for i in range(N)]
ans = {}
for i in range(N):
    if S[i] in ans:
        ans[S[i]] += 1
    else:
        ans[S[i]] = 1
#print(ans)
sum = 0
for  i in ans.values():
    sum += (i*(i-1))//2
print(sum)
'''
for i in range(N):
    Q = {}
    for j in range(10):
        if S[i][j] in Q:
            Q[S[i][j]] +=1
        else:
            Q[S[i][j]] = 1
    ans.append(Q)
cnt = 0
for i in range(N):
    for j in range(i+1,N):
        if ans[i] == ans[j]:
            cnt += 1
'''
#print(cnt)
''' 
for i in range(10):
    if S[0][i] in S1:
        S1[S[0][i]] +=1
    else:
        S1[S[0][i]] = 1
ans.append(S1)
for i in range(10):
    if S[2][i] in S2:
        S2[S[2][i]] +=1
    else:
        S2[S[2][i]] = 1
ans.append(S2)
'''



