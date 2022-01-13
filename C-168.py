'''
Created on 2021/07/25

@author: kentoo
'''
import math 

A,B,H,M=map(int,input().split())


CM=(M/60)*(2*math.pi)

CH=((H*60+M)/720)*(2*math.pi)


xh=A*math.cos(CH)
yh=A*math.sin(CH)

xm=B*math.cos(CM)
ym=B*math.sin(CM) 

dx=xh-xm 
dy=yh-ym

ans=math.sqrt(dx*dx+dy*dy)

print(ans)