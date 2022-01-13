'''
Created on 2021/12/11

@author: kentoo
'''

import bisect
N,Q = map(int,input().split())
A = list(map(int,input().split()))
x = [int(input())for i in range(Q)]
A.sort()

for i in range(Q):
    print(N-bisect.bisect_left(A,x[i]))
    #print(A)
#print(N-bisect.bisect(A,x[0]))
'''
ST = {}
for i in range(N):
    if A[i] in ST:
        ST[A[i]] += 1
    else:
        ST[A[i]] = 1
#print(ST)
ST = dict(sorted(ST.items()))
#print(ST[130])

sum = [0]*(A[0]-1)+[1]
cnt = 1
for i in range(1,len(A)):
    d = A[i]-A[i-1]
    cnt += ST[A[i]]
    sum += ([cnt]*d)
#print(sum[99])

#sum.reverse()
print(sum)
for i in range(Q):
    if x[i] > A[-1]:
        print("0")
    else:
        print(sum[x[i]-1])
'''

 