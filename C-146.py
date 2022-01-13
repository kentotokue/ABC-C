'''
Created on 2021/09/21

@author: kentoo
'''
A,B,X = map(int,input().split())

l = 0
r = 1000000001
def f (N):
    return (A*N+B*len(str(N)))


while (r-l > 1):
    c = (l+r)//2
    
    if f(c) <= X :
        l = c 
    else:
        r = c
print(l)
