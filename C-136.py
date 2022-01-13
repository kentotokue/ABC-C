'''
Created on 2021/09/29

@author: kentoo
'''
N = int(input())
H = list(map(int,input().split()))

pre = -999
for i in range(N):
    if pre <= (H[i]-1):
        pre = H[i]-1
    elif pre <= H[i]:
        pre = H[i]
    else:
        print("No")
        exit()
print("Yes")
    
    