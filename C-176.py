'''
Created on 2021/07/23

@author: kentoo
'''


N=int(input())
A=list(map(int,input().split()))

sum=0
h=0
for i in range(0,N):
    h=max(h,A[i])
    sum+=h-A[i]
    

        
print(sum)
    
    
        

        

    