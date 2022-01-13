'''
Created on 2021/07/01

@author: kentoo
'''
#うまくできてない

N=str(input())
n=len(N)
C=[0]*3

cnt=0
for i in range(3):
    cnt=0
    for j in range(n):
        
        if (int(N[j])%3==i):
            cnt+=1
        
    C[i]=cnt 

sum=0

for i in range(3):
    sum+=C[i]*i


ans=100000000
for i in range(3):
    for j in range(3):
        if C[1]<i :
            continue
        if C[2]<i :
            continue
        if i+j==n:
            continue
        nx=sum
        
        nx-=i*1
        nx-=j*2
        
        if nx%3==0:
            ans=min(ans,i+j)
'''
if ans==100000000:
    ans=-1
'''
print(ans)
            
        
        