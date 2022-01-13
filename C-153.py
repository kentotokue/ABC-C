'''
Created on 2021/09/13

@author: kentoo
'''

N,K = map(int,input().split())
H = list(map(int,input().split()))

H.sort(reverse = True)
sum=0
for i in range(K,len(H)):
    
    sum += H[i]
print(sum)