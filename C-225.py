'''
Created on 2021/10/30

@author: kentoo
'''
N,M = map(int,input().split())
B = [list(map(int,input().split())) for i in range(N)]

'''
ans = []
for i in range(N):
    A = []
    for j in range(M):
        A.append(B[i][j]%7)
    ans.append(A)
#print(ans)
#ans[i]*(i+1) != ans[i+1]*(i+1)
for i in range(N-1):


    if ans[i] != ans[i+1] :
        print("No")
        exit()
for i in range(N-1):
    for j in range(M):
        if B[i][j]+7 != B[i+1][j]:
            print('No')
            exit()
print("Yes")
'''
BH = (B[0][0]-1)//7
BW = (B[0][0]-1)%7

if (BW+M-1) >= 7:
    print("No")

for i in range(N):
    for j in range(M):
        NB = (BH+i)*7 + (BW+j)
        if (B[i][j]-1) != NB:
            print("No")
            exit()
print("Yes")
        

