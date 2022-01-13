'''
Created on 2021/11/07

@author: kentoo
'''
N = int(input())
T = [list(map(int,input().split())) for i in range(N)]
#print(T[N-1][2])
'''
print(T[N-1][2:])
Q = list(T[N-1][2:])
print(Q)
sum = 0

for i in range(len(Q)):
    sum += T[Q[i]-1][0]

    if T[Q[i]-1][1] >0 :
        for j in range(T[Q[i]-1][1]):
          
print(sum+T[N-1][0])
print(len(K))
'''

need = [ False for i in range(N) ]
need[N-1] = True
#print(need)
for i in range(N-1,-1,-1):
    if need[i]:
        for j in range(len(T[i])-1,1,-1):
            #print(T[i][j])
            need[T[i][j]-1] = True 
#print(need)
ans = 0
for i in range(N):
    if need[i]:
        ans += T[i][0]
print(ans)