'''
Created on 2021/10/19

@author: kentoo
'''
S = str(input())
N = len(S)
S2 = []
for i in range(N):
    S2.append(int(S[i]))

#print(S2)
cnt = 0

for i in range(N-1):
    if S2[i] == S2[i+1]:
        cnt += 1
        if S2[i] == 0:
            
            S2[i+1] = 1
        else:
            S2[i+1] = 0
    #print(S2)

print(cnt)
