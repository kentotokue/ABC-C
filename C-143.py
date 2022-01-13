'''
Created on 2021/08/04

@author: kentoo
'''
N=int(input())
S=str(input())
cnt=1

for i in range(len(S)-1):
    if S[i]!=S[i+1]:
        cnt+=1
    else:
        continue
print(cnt)
    