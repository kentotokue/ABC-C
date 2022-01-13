'''
Created on 2021/06/29

@author: kentoo
'''
N=int(input())
A=list(map(int,input().split()))
a=A
while (len(A)>2):
    
    na=[]
    
    for i in range(0,len(A),2):
        na.append(max(A[i],A[i+1]))
    
    A=na

ans=min(A[0],A[1])
print(a.index(ans)+1)

    