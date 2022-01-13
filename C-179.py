'''
Created on 2021/07/22

@author: kentoo
'''
N=int(input())

cnt=0
for i in range(1,N):
    #print((N-1)//i)
    cnt+=(N-1)//i

print(cnt)
        