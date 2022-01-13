'''
Created on 2021/06/28

@author: kentoo
'''

N=int(input())

s=set()
for i in range(2,int(N**0.5)+1):
    x=i*i 
    while (x<=N):
        s.add(x)
        x*=i

print(N-len(s))
        
        
        