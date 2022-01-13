'''
Created on 2021/07/27

@author: kentoo
'''
N,K=map(int,input().split())
C=list(map(int,input().split()))

dic={}


now=0
ans=0

for i in range(N):
    
    if (dic[C[i]]==0):
        now+=1
    dic[C[i]]+=1
    if (i>=K):
        dic[C[i-K]]-=1
        if dic[C[i-K]]==0:
            now-=1
    
    ans=max(ans,now)

print(ans)
            
        
        
    
    
    