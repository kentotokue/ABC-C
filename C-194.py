'''
Created on 2021/06/28

@author: kentoo
'''
N=int(input())

A=list(map(int,input().split()))

d=[0]*((200*2)+1)


for i in range(400):
    cnt=0
    for j in range(N):
        if i==(A[j]+200):
            cnt+=1

    d[i]=cnt 

ans=0

for i in range(400):
    
    
    
    c=d[i]
    x=i-200
    
    
    ans+=x*x*c 
        

print(ans)
     

        
        
