'''
Created on 2021/10/02

@author: kentoo
'''
L ,R = map(int,input().split())

mod = 2019 

R = min(R,L+(2019*2))
#print(R)
ans = 2018
x = 0

for i in range(L,R+1):
    for j in  range(i+1,R+1):       
        #print(i,j)
        x = (i*j)%mod
        ans = min(ans,x)
        if ans == 0:
            break
print(ans)
