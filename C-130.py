'''
Created on 2021/10/05

@author: kentoo
'''
W,H,X,Y = map(int,input().split())

ans = (W*H)/2
num = 0 
if  W/2 == X and H/2 == Y:
    num = 1
else:
    num = 0 

print(ans,num)