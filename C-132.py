'''
Created on 2021/10/03

@author: kentoo
'''
N = int(input())
D = list(map(int,input().split()))

if N % 2 == 0:
    H = N//2-1
else:
    print("0")
    exit()
D.sort()
cnt = 0
for i in range(D[H]+1,D[H+1]+1):
    cnt += 1

print(cnt)
