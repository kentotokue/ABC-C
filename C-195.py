'''
Created on 2021/06/28

@author: kentoo
'''

N=int(input())

cnt=0

if (N>=1000):
    cnt+=N-999
if (N>=1000000):
    cnt+=N-999999
if (N>=1000000000):
    cnt+=N-999999999
if N>=1000000000000:
    cnt+=N-999999999999
if N>=1000000000000000:
    cnt+=N-999999999999999 
print(cnt)
